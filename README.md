# tooth-python
[![PyPI Downloads](https://static.pepy.tech/personalized-badge/tooth-python?period=total&units=INTERNATIONAL_SYSTEM&left_color=BLACK&right_color=GREEN&left_text=downloads)](https://pepy.tech/projects/tooth-python)
`tooth-python` is a very basic library that allows you to generate text with basic functions.

# How to use
```python
from tooth import Tooth # Importing `Tooth` class

tooth = Tooth()

tooth.generate("Hello") # Returns 'Toothハ'
```

# Customize vocabulary
```python
tooth = Tooth(vocab=[
    "a", "b", "c"
])
```
