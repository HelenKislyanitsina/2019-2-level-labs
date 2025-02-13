import math


REFERENCE_TEXTS = []
if __name__ == '__main__':
    texts = ['5_7.txt', '15_2.txt', '10547_3.txt', '12230_7.txt']
    for text in texts:
        with open(text, 'r') as f:
            REFERENCE_TEXTS.append(f.read())


def clean_tokenize_corpus(texts: list) -> list:
    if not texts or not isinstance(texts, list):
        return []
    clean_corpus = []
    corpus_with_split_sentence = []
    for textt in texts:
        if not isinstance(textt, str):
            continue
        textt = textt.replace('<br />', ' ')
        split_sentence = textt.split()
        corpus_with_split_sentence.append(list(split_sentence))
    clean_text = []
    clean_text_v_2 = []
    for words in corpus_with_split_sentence:
        for i in words:
            clean_words = ''
            for k in i:
                if k.isalpha():
                    clean_words += k.lower()
            clean_text.append(clean_words)
        clean_text_v_2.append(clean_text)
        clean_text = []
    clean_corpus += clean_text_v_2
    for symbols in clean_corpus:
        while '' in symbols:
            symbols.remove('')
    return clean_corpus


class TfIdfCalculator:
    def __init__(self, corpus):
        self.corpus = corpus
        self.tf_values = []
        self.idf_values = {}
        self.tf_idf_values = []
        self.file_names = ['5_7.txt', '15_2.txt', '10547_3.txt', '12230_7.txt']

    def calculate_tf(self):
        if not isinstance(self.corpus, list):
            return
        for textt in self.corpus:
            if not isinstance(textt, list):
                continue
            count_word = len(textt)
            tf_dict = {}
            for symbol in textt:
                if not isinstance(symbol, str):
                    count_word -= 1
            for word in textt:
                if not isinstance(word, str):
                    continue
                if word not in tf_dict:
                    tf_dict[word] = textt.count(word) / count_word
            if tf_dict:
                self.tf_values.append(tf_dict)

    def calculate_idf(self):
        if not isinstance(self.corpus, list):
            return
        all_docs = len(self.corpus)
        for doc in self.corpus:
            if not isinstance(doc, list):
                all_docs -= 1
        for textt in self.corpus:
            if not isinstance(textt, list):
                continue
            if textt is None:
                continue
            for word in textt:
                if not isinstance(word, str):
                    continue
                if word in self.idf_values:
                    continue
                word_in_texts_counter = 0
                for doc in self.corpus:
                    if not isinstance(doc, list):
                        continue
                    if word in doc:
                        word_in_texts_counter += 1
                self.idf_values[word] = math.log(all_docs / word_in_texts_counter)

    def calculate(self):
        if not self.tf_values or not self.idf_values:
            return
        for element in self.tf_values:
            dictionary = {}
            for word, value in element.items():
                dictionary[word] = value * self.idf_values[word]
            self.tf_idf_values.append(dictionary)

    def report_on(self, word, document_index):
        if not self.tf_idf_values:
            return ()
        if document_index >= len(self.corpus):
            return ()
        dict_tf_idf = self.tf_idf_values[document_index]
        if word not in dict_tf_idf:
            return ()
        list_tf_idf = sorted(self.tf_idf_values[document_index], key=lambda x: self.tf_idf_values[document_index][x],
                             reverse=True)
        res = (dict_tf_idf.get(word), list_tf_idf.index(word))
        return res


# test_texts = clean_tokenize_corpus(REFERENCE_TEXTS)
# tf_idf = TfIdfCalculator(test_texts)
# tf_idf.calculate_tf()
# tf_idf.calculate_idf()
# tf_idf.calculate()
# print(tf_idf.report_on('good', 0))
# print(tf_idf.report_on('and', 1))
