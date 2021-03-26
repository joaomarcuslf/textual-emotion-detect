import pytest

from text2emotions import get_sorted_emotions, get_main_emotion, get_least_emotion

# get_least_emotion(txt)
# get_main_emotion(txt)
# get_sorted_emotions(txt)

def test_get_least_emotion_1():
    least_emotion = get_least_emotion("I'm very happy today!")

    assert least_emotion is 'Angry'

def test_get_least_emotion_2():
    least_emotion = get_least_emotion("I'm very sad today")

    assert least_emotion is not 'Angry'

def test_get_main_emotion_1():
    least_emotion = get_main_emotion("I'm very happy today!")

    assert least_emotion is 'Happy'

def test_get_main_emotion_2():
    least_emotion = get_main_emotion("I'm very sad today")

    assert least_emotion is not 'Happy'

def test_get_sorted_emotions_1():
    sorted_emotions = get_sorted_emotions("I'm very happy today!")

    assert sorted_emotions[0]['emotion'] is 'Angry'
    assert sorted_emotions[0]['value'] == 0.0

def test_get_sorted_emotions_2():
    sorted_emotions = get_sorted_emotions("I'm very happy today!")

    assert sorted_emotions[-1]['emotion'] is 'Happy'
    assert sorted_emotions[-1]['value'] > 0.0
