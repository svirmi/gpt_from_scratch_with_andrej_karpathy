from decimal import Context
import torch

with open('input.txt', 'r', encoding='utf-8') as f:
    text = f.read()

print ("length of dataset in characters: ", len(text))

chars = sorted(list(set(text)))
vocab_size = len(chars)
print(''.join(chars))
print(vocab_size)

# Translating individual characters into integers and back (done on a character level)
stoi = { ch:i for i,ch in enumerate(chars) }
itos = { i:ch for i,ch in enumerate(chars) }
encode = lambda s: [stoi[c] for c in s]             # encoder: takes a string, outputs a list of integers
decode = lambda l: ''.join([itos[i] for i in l] )   # decoder: takes a list of integers, outputs a string

print(encode("thees iS a MY striNG"))
print(decode(encode("thees iS a MY striNG")))

# Lets now encode the entire text dataset and store it into torch.Tensor
data = torch.tensor(encode(text), dtype=torch.long)
# print(data.shape, data.dtype)
# print(data[:1000])

# Let's now split up the data into train and validations sets
n = int(0.9 * len(data))  # the first 90% will be train, the rest - validation set
train_data = data[:n]
val_data = data[n:]

block_size = 8 # sometimes called "context length"
train_data[:block_size+1]


x = train_data[:block_size]
y = train_data[1:block_size+1]

for t in range(block_size):
    context = x[:t+1]
    target = y[t]
    print(f"when input {context} the target: {target}")

torch.manual_seed(1337)    
batch_size = 4 # how many independent sequences will we process in parallele?
block_size = 8 # what is the maximum context length for predictions?

def get_batch(split):
    # generaye a small batch of data inputs x and targets y
    data = train_data if split == 'train' else val_data
    ix = torch.randint(len(data) - block_size, (batch_size,))