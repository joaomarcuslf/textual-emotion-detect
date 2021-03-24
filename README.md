# Textual Emotion Detect

## Getting Started

- Start the vitual env

```sh
$ source ./bin/activate
```

- Installing dependencies

```sh
$ pip install -r requirements.txt
```

## Choosing desired strategy

### Simple one

```sh
$ python text2emotions.py
```

or

```python
from text2emotions import get_sorted_emotions, get_main_emotion, get_least_emotion

txt = "Your phrase here"

get_least_emotion(txt)
get_main_emotion(txt)
get_sorted_emotions(txt)
```