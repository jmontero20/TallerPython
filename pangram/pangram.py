def is_pangram(sentence):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    for caracter in alfabeto:
        if not(caracter in sentence.lower()):
            return False
    return True
