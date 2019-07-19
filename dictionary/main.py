import difflib
import json

data = json.load(open('data.json'))


def translate(word):
    try:
        return data[word]
    except KeyError:
        if len(difflib.get_close_matches(word, data)) > 0:
            close_match = difflib.get_close_matches(word, data)[0]
            answer = input(
                'There is no such word in a dictionary.'
                ' Maybe you meant {}? (Y/N) '.format(close_match)
                ).lower()
            if answer == 'y':
                return translate(close_match)
            else:
                return "Bye"
        else:
            return "Can't find such word"


word = input("Enter word: ")
if word.isupper():
    pass
elif not (word[0].isupper() and word[1].islower()):
    word.lower()

output = translate(word)

if type(output) == list:
    for word in output:
        print(word)
else:
    print(word)
