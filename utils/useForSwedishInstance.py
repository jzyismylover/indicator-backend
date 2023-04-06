import nltk
from utils.useForFactory import BaseUtils

class SwedishUtils(BaseUtils):
  def get_sentences(self, text):
    tokenizer = nltk.data.load('tokenizers/punkt/swedish.pickle')
    sentences = tokenizer.tokenize(text)
    return sentences