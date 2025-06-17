from operator import le


with open('input.txt', 'r', encoding='utf-8') as f:
    text = f.read()

print ("length of dataset in characters: ", len(text))

chars = sorted(list(set(text)))
vocab_size = len(chars)
print(''.join(chars))
print(vocab_size)