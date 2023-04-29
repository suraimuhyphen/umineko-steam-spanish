import bisect
import re
import json
from dotenv import load_dotenv
from pathlib import Path
from google.cloud import translate_v2 as translate

from util.fixes import post_fixes
from util.logging import log_error

load_dotenv('../.env')

class UminekoQuestionTranslator:
    """Spanish Translator for the Umineko Question Arcs"""
    
    def __init__(
        self,
        english_path: str = '0.u',
        spanish_path: str = '0.u.spanish',
        data_path: str = './data',
        logs_path: str = './logs'
    ):
        self.english_path = english_path
        self.spanish_path = spanish_path
        self.data_path = data_path
        self.logs_path = logs_path

    def translate_script(self, line_limit: int, fresh: bool=False):
        """Translates a number of lines from game script from english into spanish.
        
        This function will start translating from the first line it finds unprocessed,
        unless the `fresh` flag is True.

        Args:
            line_limit: Number of lines to translate.
            fresh: Flag that indicates if the translation should force start from the beginning.

        """

        game_script = ""
        lines_history = {'lines': []}

        with open(self.english_path if fresh else self.spanish_path, 'r', encoding="utf-8") as infile:
            game_script = infile.read()

        if not Path(self.data_path).is_dir() or fresh:
            Path(self.data_path).mkdir(parents=True, exist_ok=True)
            with open(f'{self.data_path}/lines_history.json', 'w', encoding="utf-8") as outfile:
                json.dump(lines_history, outfile, indent=4)
        else:
            with open(f'{self.data_path}/lines_history.json', 'r', encoding="utf-8") as infile:
                lines_history = json.load(infile)
        
        translator = translate.Client()

        lines = re.findall(r"langen.*\^.*\^", game_script)

        lines = {idx: line for idx, line in enumerate(lines)}

        partial_lines = {}

        line_count = 0
        idx = 0
        while line_count < line_limit and idx < len(lines):
            if idx not in lines_history['lines']:
                partial_lines.update({idx: lines[idx]})
                line_count += 1
            else:
                print(f"Line {idx} has already been proccesed")
            idx += 1

        partial_lines_translated = {}

        for i, (idx, line) in enumerate(partial_lines.items()):
                sentences = re.findall(r"\^((?!\^|\!).+?)\^", line) # captures all english text
                translated_line = line

                for sentence in sentences:
                    
                    try:
                        translation_result = translator.translate(sentence, target_language='es', format_='text')
                        translated_sentence = translation_result["translatedText"]
                        translated_sentence = post_fixes(translated_sentence, line)

                        translated_line = re.sub(re.escape(sentence), translated_sentence, translated_line)
                        
                        if translated_line == line:
                            log_error(
                                Exception("Sentence could not be translated"),
                                translated_sentence,
                                self.logs_path
                            )
                        
                    except ValueError as ve:
                        log_error(
                            ve,
                            translated_sentence,
                            self.logs_path
                        )

                bisect.insort(lines_history['lines'], idx)
                with open('./data/lines_history.json', 'w', encoding="utf-8") as outfile:
                    json.dump(lines_history, outfile, indent=4)

                partial_lines_translated.update({idx: translated_line})
                print(f"Translating: {i+1}/{len(partial_lines)}")      

        parsed_game_script = game_script
        for i, (line, line_translated) in enumerate(zip(partial_lines.values(), partial_lines_translated.values())):
            parsed_game_script = re.sub(re.escape(line), re.sub('\\\\', '', line_translated), parsed_game_script)
            print(f"Updating: {i+1}/{len(partial_lines_translated)}")

        with open(self.spanish_path, 'w') as outfile:
            outfile.write(parsed_game_script)

        for idx, line_translated in partial_lines_translated.items():
            print(f"{idx}. {line_translated}")