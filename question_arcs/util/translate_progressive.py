import time

from translator.question_translator import UminekoQuestionTranslator
from util.translation_status import print_translation_status

def translate_progressive(
        translator: UminekoQuestionTranslator,
        lines: str,
        iterations: int,
        iteration_delay: int
    ):
    """Uses a translator to translate the game script from english to spanish progressively.

    Args:
        lines: Number of lines to translate each iteration.
        iterations: Number of iterations.
        iteration_delay: Number of seconds to wait between each iteration.

    """

    for i in range(iterations):
        finished_translating = translator.translate_script(lines, fresh=False)
        print_translation_status(translator.english_path, translator.data_path)
        if finished_translating:
            print("Translation is completed!")
            break
        if i != iterations - 1:
            print(f"Another {lines} lines will be translated in {iteration_delay} seconds...")
            time.sleep(iteration_delay) 
    