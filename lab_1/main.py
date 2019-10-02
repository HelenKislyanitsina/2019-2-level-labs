"""
Labour work #1
Count frequencies dictionary by the given arbitrary text
"""


def calculate_frequences(text: str) -> dict:
    """
    Calculates number of times each word appears in the text
    """
    if text is None or text == '':
        return {}
    if isinstance(text, int):
        return {}
    text_without_trash = ''
    for i in text:
        if i.isalpha():
            text_without_trash += i
        elif i == ' ' or i == '\n':
            text_without_trash += i
        else:
            text_without_trash += ' '
    text_without_trash = text_without_trash.lower()
    list_of_words = text_without_trash.split()
    words_dictionary = {}
    for i in list_of_words:
        count = list_of_words.count(i)
        words_dictionary[i] = count
    sort_list = words_dictionary.items()
    sort_list = sorted(sort_list, key=lambda a: a[1], reverse=True)
    final_dictionary = {}
    for i in sort_list:
        final_dictionary[i[0]] = i[1]
    return final_dictionary


def filter_stop_words(frequencies: dict, stop_words: tuple) -> dict:
    """
    Removes all stop words from the given frequencies dictionary
    """
    if frequencies is not None and stop_words is None:
        return frequencies
    if frequencies is None and stop_words is not None:
        return {}
    if frequencies is None and stop_words is None:
        return {}
    shadow_dictionary = frequencies.copy()
    for i in range(0, 10):
        if i in shadow_dictionary:
            del shadow_dictionary[i]
    for i in stop_words:
        if i in shadow_dictionary:
            del shadow_dictionary[i]
    return shadow_dictionary


def get_top_n(frequencies: dict, top_n: int) -> tuple:
    """
    Takes first N popular words
    """
    if frequencies is None or frequencies == {}:
        return ()
    final_tuple = ()
    list_of_words = frequencies.keys()
    list_of_words = list(list_of_words)
    if top_n > len(frequencies):
        top_n = len(frequencies)
    for i in range(top_n):
        final_tuple = final_tuple + (''.join(list_of_words[i]),)
    return final_tuple


def read_from_file(path_to_file: str, lines_limit: int) -> str:
    if path_to_file is None or lines_limit is None:
        return ''
    text = open(path_to_file, 'r')
    result = ''
    for line in text:
        if lines_limit == 0:
            break
        elif lines_limit > 0:
            result += line
            lines_limit -= 1
    return result


def write_to_file(path_to_file: str, content: tuple):
    if path_to_file is None or content is None or isinstance(content, int):
        return None
    file = open(path_to_file, 'w')
    for word in content:
        file.write(word + '\n')
    file.close()



