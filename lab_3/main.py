"""
Labour work #3
 Building an own N-gram model
"""

import math

REFERENCE_TEXT = ''
if __name__ == '__main__':
    with open('not_so_big_reference_text.txt', 'r') as f:
        REFERENCE_TEXT = f.read()


class WordStorage:
    def __init__(self):
        self.storage = {}

    def put(self, word: str) -> int:
        if word not in self.storage and isinstance(word, str):
            id_word = hash(word)
            self.storage[word] = id_word
            return id_word
        return -1

    def get_id_of(self, word: str) -> int:
        if word in self.storage:
            return self.storage[word]
        return -1

    def get_original_by(self, word_id: int) -> str:
        if word_id in self.storage.values():
            index = list(self.storage.values()).index(word_id)
            return list(self.storage.keys())[index]
        return 'UNK'

    def from_corpus(self, corpus: tuple):
        if not isinstance(corpus, tuple):
            return -1
        for word in corpus:
            if isinstance(word, str):
                self.put(word)


class NGramTrie:
    def __init__(self, n):
        self.size = n
        self.gram_frequencies = {}
        self.gram_log_probabilities = {}

    def fill_from_sentence(self, sentence: tuple) -> str:
        ok = 'OK'
        error = 'ERROR'
        gramm = []
        if not isinstance(sentence, tuple):
            return error
        if sentence is None:
            return error
        if len(sentence) < self.size:
            return error
        for num, _ in enumerate(sentence[:-self.size + 1]):
            gramm = []
            i = 0
            while i < self.size:
                gramm.append(sentence[num + i])
                i += 1
            gramm = tuple(gramm)
            if gramm in self.gram_frequencies:
                self.gram_frequencies[gramm] += 1
            else:
                self.gram_frequencies[gramm] = 1
        if not gramm:
            return error
        return ok

    def calculate_log_probabilities(self):
        for gramm in self.gram_frequencies:
            summ = 0
            for base_gramm in self.gram_frequencies:
                if gramm[:-1] == base_gramm[:-1]:
                    summ += self.gram_frequencies[base_gramm]
            self.gram_log_probabilities[gramm] = math.log(self.gram_frequencies[gramm] / summ)

    def predict_next_sentence(self, prefix: tuple) -> list:
        if not isinstance(prefix, tuple) or len(prefix) + 1 != self.size:
            return []
        sentence = list(prefix)
        example = []
        for gramm in self.gram_log_probabilities:
            example.append(gramm[0: self.size - 1])
        while prefix in example:
            predict = []
            for i, k in self.gram_log_probabilities.items():
                if prefix == i[0: self.size - 1]:
                    predict.append((k, i))
            predict.sort(reverse=True)
            affix = predict[0][1][-1]
            sentence.append(affix)
            prefix = predict[0][1][1:]
        return sentence


def encode(storage_instance, corpus) -> list:
    result = []
    for num, sentence in enumerate(corpus):
        result.append([])
        for word in sentence:
            if isinstance(word, str):
                result[num] += [storage_instance.get_id_of(word)]
    return result


def split_by_sentence(text: str) -> list:
    if text is None:
        return []
    if not text:
        return []
    if ' ' not in text:
        return []
    signs_of_end = '.!?'
    split_sentences = []
    new_text = ''
    new_text_split = ''
    if '\n' in text:
        text = text.replace('\n', ' ')
        text = text.replace('   ', ' ')
        text = text.replace('  ', ' ')
    for symbol in text:
        if symbol.isalnum() or symbol == ' ':
            before_symbol = text[text.index(symbol) - 2]
            if symbol.isupper() and before_symbol in signs_of_end:
                new_text += '#'
                new_text += symbol.lower()
            else:
                new_text += symbol.lower()
        new_text_split = new_text.split('#')
    for sentence in new_text_split:
        sentence = sentence.split()
        sentence.insert(0, '<s>')
        sentence.append('</s>')
        split_sentences.append(sentence)
    return split_sentences