import transformers
from transformers import BertTokenizer

#BerttTokenizer is a tokenizer for subword tokens

# Initialize the tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

# Define a list of sentences to tokenize
sentences = ["This is a sentence.", "Another sentence here."]

# Tokenize the sentences using subword tokenization
encoded_sentences = tokenizer(sentences, padding=True, truncation=True, return_tensors="pt")

# Print the tokenized sentences
print(encoded_sentences)
