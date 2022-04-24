counter = 0
many_char = []
lists = []
text = list(" ".join(input().lower().split()))
for index in ''.join(text):
    if index.isalpha():
        counter = max(counter, text.count(index))
        for i in ''.join(text):
            if i.isalpha() or i == ' ':
                lists += [i]
for i in range(len(text)):
    if text[i] == '.' and i + 1 != len(text):
        text[i + 2] = text[i + 2].upper()
    if text[i].isalpha() and counter == text.count(text[i]):
        many_char += [text[i]]
big_word = ''.join(lists).split()
text[0] = text[0].upper()
print("Clear text: ", ''.join(text),
      "\nBig word: ", max(big_word, key=len),
      "\nMore used character:", 'and '.join(set(many_char)))
