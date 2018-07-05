import nltk
input_sentence = "The mark of the local Thieves Guild has appeared in the locations of a pair of major heists within the city. The child of an important king has been kidnapped and must be rescued. In a creepy little town in which everyone seems cold and distant, they say a visit to the little old lady in the woods can solve all your problems. The man in black fled across the desert, and the hunter followed."
text = nltk.word_tokenize(input_sentence)
list_of_tokens = nltk.pos_tag(text)
print(list_of_tokens)
