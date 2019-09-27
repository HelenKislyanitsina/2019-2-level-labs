"""
Labour work #1
Count frequencies dictionary by the given arbitrary text
"""


def calculate_frequences(text: str) -> dict:
    """
    Calculates number of times each word appears in the text
    """
    if text is None or text == '':
        print({})
        return {}
    elif isinstance(text, int):
        print({})
        return {}
    text_without_trash = ''
    for i in range(len(text)):
        if text[i].isalpha():
            text_without_trash += text[i]
        elif text[i] == ' ' or text[i] == '\n':
            text_without_trash += text[i]
        else:
            text_without_trash += ' '
    text_without_trash = text_without_trash.lower()
    list_of_words = text_without_trash.split()
    words_dictionary = {}
    for i in range(len(list_of_words)):
        count = list_of_words.count(list_of_words[i])
        words_dictionary[list_of_words[i]] = count
    sort_list = words_dictionary.items()
    sort_list = sorted(sort_list, key=lambda i: i[1], reverse=True)
    final_dictionary = {}
    for i in range(len(sort_list)):
        final_dictionary[sort_list[i][0]] = sort_list[i][1]
    print(final_dictionary)
    return final_dictionary
    pass


def filter_stop_words(frequencies: dict, stop_words: tuple) -> dict:
    """
    Removes all stop words from the given frequencies dictionary
    """
    if frequencies is not None and stop_words is None:
        print(frequencies)
        return frequencies
    elif frequencies is None and stop_words is not None:
        print({})
        return {}
    elif frequencies is None and stop_words is None:
        print(None)
        return {}
    shadow_dictionary = frequencies.copy()
    for i in range(0, 10):
        if i in shadow_dictionary:
            del shadow_dictionary[i]
    for i in range(len(stop_words)):
        if stop_words[i] in shadow_dictionary:
            del shadow_dictionary[stop_words[i]]
    print(shadow_dictionary)
    return shadow_dictionary
    pass


def get_top_n(frequencies: dict, top_n: int) -> tuple:
    """
    Takes first N popular words
    """
    if frequencies is None or frequencies == {}:
        print(())
        return ()
    final_tuple = ()
    list_of_words = frequencies.keys()
    list_of_words = list(list_of_words)
    if top_n > len(frequencies):
        top_n = len(frequencies)
    for i in range(top_n):
        final_tuple = final_tuple + (''.join(list_of_words[i]),)
    print(final_tuple)
    return final_tuple
    pass

