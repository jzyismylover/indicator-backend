import hanlp
import torch
import GPUtil
from utils.hanlp import UNIVERSAL_HANLP as Hanlp
from plugins._sentry import useSentryCaptureError, useSentryCaptureMessage

class BaseUtils(object):
    # GET 词频list
    def get_word_frequency(self, words):
        hapax = []
        frequency = []
        words_set = set(words)

        for word in words_set:
            frequency.append({'num': words.count(word), 'word': word})
            if words.count(word) == 1:
                hapax.append(word)

        frequency = sorted(
            frequency, key=lambda row: (row['num'], row['word']), reverse=True
        )


        return {
            'frequency': [i for i in map(lambda row: row['num'], frequency)],
            'frequency_words': [i for i in map(lambda row: row['word'], frequency)],
            'hapax': hapax,
        }

    def is_verb_word(self, tag):
        if tag == 'VERB':
            return True
        else:
            return False

    def is_adjective_word(self, tag):
        if tag == 'ADJ':
            return True
        else:
            return False

    def is_real_word(self, tag):
        REAL_WORD_LIST = ['ADJ', 'NOUN', 'NUM', 'PRON', 'PROPN', 'VERB']
        if tag in REAL_WORD_LIST:
            return True
        else:
            return False

    def get_verb_words(self, tags, words=[]):
        verb_words = []
        for i, tag in enumerate(tags):
            if self.is_verb_word(tag):
                verb_words.append(words[i])

        return verb_words

    # GET 形容词列表
    def get_adjective_words(self, tags, words=[]):
        adjective_words = []
        for i, tag in enumerate(tags):
            if self.is_adjective_word(tag):
                adjective_words.append(words[i])

        return adjective_words

    # GET 实词列表
    def get_real_words(self, tags, words=[]):
        real_words = []
        for i, tag in enumerate(tags):
            if self.is_real_word(tag):
                real_words.append(words[i])

        return [i for i in set(real_words)]

    # GET 分句列表
    def get_sentences(self, text):
        # 沿用 hanlp 多任务分词模型
        SENTENCE_SPILIT = hanlp.load(hanlp.pretrained.eos.UD_CTB_EOS_MUL)
        sentences = SENTENCE_SPILIT(text)
        return sentences

    # GET 分词列表
    def get_words(self, sentences):
        # 显存占用大的函数，应对此进行相关优化
        words = []
        tags = []
        SENTENCES_LIMIT = 5  # 单次处理的句子数
        i = 0

        while i < len(sentences):
            try:
                Gpus = GPUtil.getGPUs()
                gpu0 = Gpus[0]
                if (gpu0.memoryUsed / gpu0.memoryTotal) > 0.6:
                    useSentryCaptureMessage('显存使用率高于60%, 任务中断')
                    raise MemoryError('GPU Memory usage bigger than 60 percent')

                sentence = sentences[i : i + SENTENCES_LIMIT]
                ans = Hanlp(sentence, tasks='ud')
                words.extend([i for j in ans['tok'] for i in j])
                tags.extend([i for j in ans['pos'] for i in j])
            except Exception as e:
                print('hahahahahahaha')
                if isinstance(e, MemoryError):
                    torch.cuda.empty_cache()
                useSentryCaptureError(e)
                pass
            finally:
                i = i + SENTENCES_LIMIT

        self.tags = tags
        return words

    # GET 词性标注
    def get_word_character(self, words):
        return self.tags
