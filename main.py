with open('input.txt', 'r', encoding='utf-8') as f:
    text = f.read()

print ("length of dataset in characters: ", len(text))

chars = sorted(list(set(text)))
vocab_size = len(chars)
print(''.join(chars))
print(vocab_size)

# Translating individual characters into integers
stoi = { ch:i for i,ch in enumerate(chars) }
itos = { i:ch for i,ch in enumerate(chars) }
encode = lambda s: [stoi[c] for c in s]             # encoder: takes a string, outputs a list of integers
decode = lambda l: ''.join([itos[i] for i in l] )   # decoder: takes a list of integers, outputs a string

print(encode("thees iS a MY striNG"))
print(decode(encode("thees iS a MY striNG")))
