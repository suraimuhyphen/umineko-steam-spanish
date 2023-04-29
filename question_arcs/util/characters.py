import re

def get_total_character_amount(script_path: str = '0.u') -> int:
    """Gets total number of characters in a game script"""

    with open(script_path, 'r', encoding="utf-8") as infile:
        game_script = infile.read()

    lines = re.findall(r"langen.*\^.*\^", game_script)

    chars = 0

    for raw_text in lines:
        sentences = re.findall(r"\^(.*?)\^", raw_text)
        for sentence in sentences:
            parsed_sentence = re.sub(r"(\.+)", r"\g<1> ", sentence)
            chars += len(parsed_sentence)
    
    return chars