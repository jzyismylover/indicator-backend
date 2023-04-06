import nltk
from utils.useForFactory import BaseUtils

class ItalianUtils(BaseUtils):
  def get_sentences(self, text):
    tokenizer = nltk.data.load('tokenizers/punkt/italian.pickle')
    sentences = tokenizer.tokenize(text)
    return sentences