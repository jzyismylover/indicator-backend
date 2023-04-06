import nltk
from utils.useForFactory import BaseUtils

class GermanyUtils(BaseUtils):
  def get_sentences(self, text):
    tokenizer = nltk.data.load('tokenizers/punkt/german.pickle')
    sentences = tokenizer.tokenize(text)
    return sentences