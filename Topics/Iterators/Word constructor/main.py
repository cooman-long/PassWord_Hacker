words_1, words_2 = input(), input()
band_name = ''
for word_1, word_2 in zip(words_1, words_2):
    band_name += word_1 + word_2
print(band_name)
