from numbers import Real
from typing import Tuple, List

from textblob import TextBlob


def hello(name):
    output = f'Hello {name}'
    return output


def extract_sentiment(text):
    text = TextBlob(text)

    return text.sentiment.polarity


def text_contain_word(word: str, text: str):
    return word in text


def bubblesort(array) -> Tuple[List[Real], int]:
    swapped = True
    comparison = 0
    for i in range(len(array) -1):
        if swapped:
            swapped = False
            for j in range(1, len(array)-i):
                comparison += 1
                if array[j - 1] > array[j]:
                    swapped = True
                    array[j - 1], array[j] = array[j], array[j - 1]
        else:
            break
    return array, comparison
