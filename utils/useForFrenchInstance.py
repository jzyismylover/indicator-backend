import nltk
from utils.useForFactory import BaseUtils

class FrenchUtils(BaseUtils):
  def get_sentences(self, text):
    tokenizer = nltk.data.load('tokenizers/punkt/french.pickle')
    sentences = tokenizer.tokenize(text)
    return sentences