
def post_fixes(sentence: str, line: str) -> str:
    """Series of sentence fixes to be performed post-translation

    It takes a line argument for additional context.

    Args:
        sentence: The sentence to fix.
        line: The original english line which contains the sentence.

    Returns:
        The fixed line.

    """

    post_fixed_sentence = sentence

    # Characters' name fix if translated into spanish equivalent ; caps supported as well

    post_fixed_sentence = post_fixed_sentence.replace("Batallador", "Battler")
    post_fixed_sentence = post_fixed_sentence.replace("BATALLADOR", "BATTLER")
    post_fixed_sentence = post_fixed_sentence.replace("Jorge", "George")
    post_fixed_sentence = post_fixed_sentence.replace("JORGE", "GEORGE")
    post_fixed_sentence = post_fixed_sentence.replace("Rodolfo", "Rudolf")
    post_fixed_sentence = post_fixed_sentence.replace("RODOLFO", "RUDOLF")
    post_fixed_sentence = post_fixed_sentence.replace("María", "Maria")
    post_fixed_sentence = post_fixed_sentence.replace("MARÍA", "MARIA")

    post_fixed_sentence = post_fixed_sentence.replace("Asmodeo", "Asmodeus")
    post_fixed_sentence = post_fixed_sentence.replace("ASMODEO", "ASMODEUS")
    post_fixed_sentence = post_fixed_sentence.replace("Belcebú", "Beelzebub")
    post_fixed_sentence = post_fixed_sentence.replace("BELCEBÚ", "BEELZEBUB")
    post_fixed_sentence = post_fixed_sentence.replace("Satán", "Satan")
    post_fixed_sentence = post_fixed_sentence.replace("SATÁN", "SATAN")
    post_fixed_sentence = post_fixed_sentence.replace("Leviatán", "Leviathan")
    post_fixed_sentence = post_fixed_sentence.replace("LEVIATÁN", "LEVIATHAN")
    post_fixed_sentence = post_fixed_sentence.replace("Mamón", "Mammon")
    post_fixed_sentence = post_fixed_sentence.replace("MAMÓN", "MAMMON")
    post_fixed_sentence = post_fixed_sentence.replace("Belfegor", "Belphegor")
    post_fixed_sentence = post_fixed_sentence.replace("BELFEGOR", "Belphegor")

    # Substitue "Guau" in Maria's speech with "Uuu"

    if 'mar_' in line:
        post_fixed_sentence = post_fixed_sentence.replace("Guau", "Uuu")

    # Head Family ; substitute with "Rokkenjima", I think it makes the more sense in this case

    post_fixed_sentence = post_fixed_sentence.replace("de Head Family", "de Rokkenjima")
    post_fixed_sentence = post_fixed_sentence.replace("en Head Family", "en Rokkenjima")
    post_fixed_sentence = post_fixed_sentence.replace("Head Family", "Rokkenjima")

    # Aunt Rosa

    post_fixed_sentence = post_fixed_sentence.replace("Aunt Rosa", "Tía Rosa")

    # Sweetfish

    post_fixed_sentence = post_fixed_sentence.replace("sweetfish", "de agua dulce")
    post_fixed_sentence = post_fixed_sentence.replace("Sweetfish", "de agua dulce")

    return post_fixed_sentence
