from indicnlp.tokenize import sentence_tokenize
from utils.useForFactory import BaseUtils

class HindiUtils(BaseUtils):
    def get_sentences(self, text):
      sentences=sentence_tokenize.sentence_split(text, lang='hi')
      return sentences

if __name__ == '__main__':
  indic_string="""तो क्या विश्व कप 2019 में मैच का बॉस टॉस है? यानी मैच में हार-जीत में \
    टॉस की भूमिका अहम है? आप ऐसा सोच सकते हैं। विश्वकप के अपने-अपने पहले मैच में बुरी तरह हारने वाली एशिया की दो टीमों \
    पाकिस्तान और श्रीलंका के कप्तान ने हालांकि अपने हार के पीछे टॉस की दलील तो नहीं दी, लेकिन यह जरूर कहा था कि वह एक अहम टॉस हार गए थे।"""
  hidi_util = HindiUtils()
  sentences = hidi_util.get_sentences(indic_string)
  print(sentences) 