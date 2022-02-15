"""https://open.kattis.com/problems/piglatin"""

VOWEL = {'a', 'e', 'i', 'o', 'u', 'y'}


def is_begin_with_consonant(word, vowel=VOWEL):
    return word[0] not in vowel


def is_begin_with_vowel(word, vowel=VOWEL):
    return word[0] in vowel


def get_next_vowel_index(word, vowel=VOWEL):
    index = 0
    for i in word:
        index += 1
        if i in vowel:
            return index


text = input('')
text = text.split()
ans = []

for word in text:
    if is_begin_with_consonant(word):
        index = get_next_vowel_index(word)
        new_word = word[index-1:] + word[:index-1] + "ay"
        ans.append(new_word)
    else:
        ans.append(word + "yay")

print(" ".join(ans))
