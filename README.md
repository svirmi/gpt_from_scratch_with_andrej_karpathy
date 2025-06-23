# gpt_from_scratch_with_andrej_karpathy

### Building Character-level language model

Coded after YT video by Andrej Karpathy - https://youtu.be/kCc8FmEb1nY?si=lXm5JiRPQxoWt5Pb

Run this command to get dataset
```
wget https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt
```

Run this command to get first 550 symbols of text file:
```
head -c 550 input.txt
```

#### OpenAI tokeniser
(https://github.com/openai/tiktoken)[https://github.com/openai/tiktoken]

#### Estonian National Corpus 2021: Morphologically Tagged and Clean Text 
(https://huggingface.co/datasets/siimh/estonian_corpus_2021)[https://huggingface.co/datasets/siimh/estonian_corpus_2021]


#### Tokenizer Evaluation on European Languages
(https://occiglot.eu/posts/eu_tokenizer_perfomance/)[https://occiglot.eu/posts/eu_tokenizer_perfomance/]

#### The Importance of Tokenizers for Multilingual LLMs: A Case Study on Greek
(https://medium.com/@geosar/the-importance-of-tokenizers-for-multilingual-llms-a-case-study-on-greek-af5301b0bacf)[https://medium.com/@geosar/the-importance-of-tokenizers-for-multilingual-llms-a-case-study-on-greek-af5301b0bacf]

Byte-level Byte-Pair Encoding (BPE): This is a variant of subword tokenization that operates at the byte level, making it more language-agnostic and suitable for multilingual models.