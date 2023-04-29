from util.lines import get_total_lines_amount, get_translated_lines_amount

def print_translation_status(
        script_path: str = '0.u',
        data_path: str = './data'
    ):
    """Print status of translation"""

    total_lines = get_total_lines_amount(script_path)
    translated_lines = get_translated_lines_amount(data_path)

    percent_translated = round(100 * (float(translated_lines) / float(total_lines)), 4)

    print(f"Lines Translated / Total Lines = {translated_lines}/{total_lines}")
    print(f"Percentage of the game translated = {percent_translated}%")