def get_word_count(book_text):
    return len(book_text.split())


def get_character_count(book_text):
    result_dict = dict()
    for char in book_text:
        ch = char.lower()
        if ch in result_dict:
            result_dict[ch] += 1
        else:
            result_dict[ch] = 1

    return result_dict


def sort_by_char(char_dict):
    def sort_on_dict(input_dict):
        return input_dict['num']
    result_list = list()
    for key, value in char_dict.items():
        result_list.append({
            'char': key,
            'num': value
        })
    result_list.sort(reverse=True, key=sort_on_dict)
    return result_list
