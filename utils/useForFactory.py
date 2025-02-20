import re
import os
import torch
from hanlp.utils.torch_util import gpus_available
from utils.hanlp import UNIVERSAL_HANLP as Hanlp

# 设置 pytorch占用显存
if os.path.exists('/.dockerenv'):
    gpu_memory_fraction = float(os.environ['GPU_THRESHOLD'])
else:
    gpu_memory_fraction = 0.5
if gpus_available():
    torch.cuda.empty_cache()
    torch.cuda.set_per_process_memory_fraction(gpu_memory_fraction, 0)


# 通用分句规则
_SEPARATOR = r'@'
_RE_SENTENCE = re.compile(r'(\S.+?[.!?])(?=\s+|$)|(\S.+?)(?=[\n]|$)', re.UNICODE)
_AB_SENIOR = re.compile(r'([A-Z][a-z]{1,2}\.)\s(\w)', re.UNICODE)
_AB_ACRONYM = re.compile(r'(\.[a-zA-Z]\.)\s(\w)', re.UNICODE)
_UNDO_AB_SENIOR = re.compile(r'([A-Z][a-z]{1,2}\.)' + _SEPARATOR + r'(\w)', re.UNICODE)
_UNDO_AB_ACRONYM = re.compile(r'(\.[a-zA-Z]\.)' + _SEPARATOR + r'(\w)', re.UNICODE)


def _replace_with_separator(text, separator, regexs):
    replacement = r"\1" + separator + r"\2"
    result = text
    for regex in regexs:
        result = regex.sub(replacement, result)
    return result


def split_sentence(text, best=True):
    text = re.sub(r'([。！？?])([^”’])', r"\1\n\2", text)
    text = re.sub(r'(\.{6})([^”’])', r"\1\n\2", text)
    text = re.sub(r'(…{2})([^”’])', r"\1\n\2", text)
    text = re.sub(r'([。！？?][”’])([^，。！？?])', r'\1\n\2', text)
    for chunk in text.split("\n"):
        chunk = chunk.strip()
        if not chunk:
            continue
        if not best:
            yield chunk
            continue
        processed = _replace_with_separator(chunk, _SEPARATOR, [_AB_SENIOR, _AB_ACRONYM])
        sents = list(_RE_SENTENCE.finditer(processed))
        if not sents:
            yield chunk
            continue
        for sentence in sents:
            sentence = _replace_with_separator(sentence.group(), r" ", [_UNDO_AB_SENIOR, _UNDO_AB_ACRONYM])
            yield sentence


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
        sentences = [sentence for sentence in split_sentence(text)]
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
                # Gpus = GPUtil.getGPUs()
                # gpu0 = Gpus[0]
                # if (gpu0.memoryUsed / gpu0.memoryTotal) > 0.55:
                #     useSentryCaptureMessage('显存使用率高于60%, 任务中断')
                #     raise MemoryError('GPU Memory usage bigger than 60 percent')
                # def transform_bytes_to_gb(val):
                #     return val / 1024 / 1024 / 1024
                # print(transform_bytes_to_gb(torch.cuda.memory_allocated()))
                # print(transform_bytes_to_gb(torch.cuda.memory_cached()))
                # print(transform_bytes_to_gb(torch.cuda.max_memory_allocated()))
                # print(torch.cuda.memory_summary())

                sentence = sentences[i : i + SENTENCES_LIMIT]
                ans = Hanlp(sentence, tasks='ud')
                words.extend([i for j in ans['tok'] for i in j])
                tags.extend([i for j in ans['pos'] for i in j])
            except Exception as e:
                if isinstance(e, MemoryError):
                    torch.cuda.empty_cache()
                pass
            finally:
                i = i + SENTENCES_LIMIT

        self.tags = tags
        return words

    # GET 词性标注
    def get_word_character(self, words):
        return self.tags
