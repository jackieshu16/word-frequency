# pass in an article, find occurrences of each word and output the occurrences

# steps
# 1. strip leading and trailing whitespaces
# 3. lower case all words
# 2. remove punctuations
# 4. split the article into list of words
# 5. create a dictionary to store word-occurrence key-value pairs
# 6. sort desc by occurrence
import regex
import sys


def remove_punctuations(initial_string):
    str_a = initial_string.strip().lower()
    w_list = regex.findall("\w+", str_a)
    return w_list


def create_word_occurrence_dict(word_list):
    word_dict = {}
    for word in word_list:
        if word not in word_dict.keys():
            word_dict[word] = 1
        else:
            word_dict[word] = word_dict.get(word) + 1
    return word_dict


def sort_occurrence_descending(dict):
    for word in sorted(dict, key=dict.get, reverse=True):
        print(word, dict[word])


if __name__ == "__main__":
    """a sample article: "One more thing that you can do with the group() method is to have the matches returned as
                          a tuple by specifying the associated group numbers in between the group() method’s 
                          parentheses. This is useful when we want to extract the range of groups."
    """
    if len(sys.argv) != 2:
        print(f'Usage: python3 {sys.argv[0]} "the article here"')
    else:
        sort_occurrence_descending(create_word_occurrence_dict(remove_punctuations(sys.argv[1])))
