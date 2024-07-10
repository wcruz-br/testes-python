def reverse_words(sentence):
    words = sentence.split(" ")
    reversed_sentence = " ".join(reversed(words))
    return reversed_sentence

print(reverse_words("Essa é uma frase de teste"))