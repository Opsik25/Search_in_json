import json
import os


def read_json(file: str, word_max_len=6, top_words_amt=10) -> list:
    """
    Return a list with whe most common words in the description in the .json file.
    """
    words_count_dict = {}
    return_list = []
    description_list = []
    with open(file, encoding='UTF-8') as json_file:
        json_data = json.load(json_file)
    for news in json_data['rss']['channel']['items']:
        description_list.extend(news['description'].split())
    for word in description_list:
        if len(word) > word_max_len:
            if word not in words_count_dict:
                words_count_dict[word] = 1
            else:
                words_count_dict[word] += 1
    top_words = sorted(words_count_dict.items(), key=lambda x: x[1], reverse=True)[:top_words_amt]
    for word in top_words:
        return_list.append(word[0])
    return return_list


file_path = os.path.join(os.getcwd(), 'newsafr.json')
print(read_json(file_path))



