
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import spacy

from torchtext.data import Field, TabularDataset, BucketIterator


class FakeNewsNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.init_weights()

    def init_weights(self):
        initrange = 0.5
        self.embedding.weight.data.uniform_(-initrange, initrange)
        self.fc.weight.data.uniform_(-initrange, initrange)
        self.fc.bias.data.zero_()

    def forward(self, text, offsets):
        return self.fc()

eng = spacy.load('en')

def tokenize(text):
    return [tok.text for tok in eng.tokenizer(text)]


text = Field(sequential=True, use_vocab=True, tokenize=tokenize, lower=True)
truth = Field(sequential=False, use_vocab=False)
fields = {"text": ('text', text), "truth": ('truth', truth)}

trainData, testData = TabularDataset.splits(path="data", train="train.csv", test="test.csv", format="csv", fields=fields)
print(trainData[0].__dict__.keys())
text.build_vocab(trainData, max_size=10000, min_freq=3)

train_iterator, test_iterator = BucketIterator.splits((trainData, testData), batch_size=10)

for batch in train_iterator:
    print(batch)