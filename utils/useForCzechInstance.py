# 捷克
import nltk
from utils.useForFactory import BaseUtils

class CzechUtils(BaseUtils):
  def get_sentences(self, text):
    tokenizer = nltk.data.load('tokenizers/punkt/czech.pickle')
    sentences = tokenizer.tokenize(text)
    return sentences