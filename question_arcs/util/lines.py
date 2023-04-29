import re
import json

def dump_lines(
        script_path: str = '0.u',
        lines_dump_path: str = 'english_lines.txt'
    ):
    """Dumps all lines into a file"""

    with open(script_path, 'r', encoding="utf-8") as infile:
        game_script = infile.read()

    lines = re.findall(r"langen.*\^.*\^", game_script)

    line_dump  = ""

    for idx, line in enumerate(lines):
        line_dump += f"\n{idx}. {line}"
    
    with open(lines_dump_path, 'w', encoding="utf-8") as outfile:
        outfile.write(line_dump)

def get_total_lines_amount(script_path: str = '0.u') -> int:
    """Get number of lines from a script file"""

    with open(script_path, 'r', encoding="utf-8") as infile:
        game_script = infile.read()

    lines = re.findall(r"langen.*\^.*\^", game_script)
    
    return len(lines)

def get_translated_lines_amount(data_path: str = './data') -> int:
    """Get number of translated lines from a script file"""

    with open(f'{data_path}/lines_history.json', 'r', encoding="utf-8") as infile:
        lines_history = json.load(infile)

    return len(lines_history['lines'])
