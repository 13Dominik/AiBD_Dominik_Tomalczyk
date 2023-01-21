from app import hello, extract_sentiment, text_contain_word, bubblesort
import pytest


def test_hello():
    got = hello("Aleksandra")
    want = "Hello Aleksandra"

    assert got == want


def test_extract_sentiment():
    text = "I think today will be a great day"

    sentiment = extract_sentiment(text)

    assert sentiment > 0


testdata = ["I think today will be a great day", "I do not think this will turn out well"]


@pytest.mark.parametrize('sample', testdata)
def test_extract_sentiment(sample):
    sentiment = extract_sentiment(sample)

    assert sentiment > 0


testdata = [
    ('There is a duck in this text', 'duck', True),
    ('There is nothing here', 'duck', False)
]


@pytest.mark.parametrize('sample, word, expected_output', testdata)
def test_text_contain_word(sample, word, expected_output):
    assert text_contain_word(word, sample) == expected_output


test_bubble = [
    ([1, 2, 3, 4, 5], ([1, 2, 3, 4, 5], 4)),
    ([2, 1, 3], ([1, 2, 3], 3)),
    ([64, 34, 25, 12, 22, 11, 90], ([11, 12, 22, 25, 34, 64, 90], 21)),
    ([8,7,3,1,8], ([1,3,7,8,8], 10)),
    ([7, 1, 6, 3, 2], ([1, 2, 3, 6, 7], 10))
]

@pytest.mark.parametrize('array, expected_output', test_bubble)
def test_bublesort(array, expected_output):
    assert bubblesort(array) == expected_output