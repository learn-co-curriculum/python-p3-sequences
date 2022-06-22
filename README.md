# Sequences

## Learning Goals

- Utilize Python's `list`, `tuple`, and `str` data types to accomplish
several common programming tasks.

- Execute and test Python code using the Python shell and `pytest`.

## Introduction

A _sequence_ is a simple data structure that is present in all programming
languages in which data is stored in a specified order. The elements of a
sequence can be accessed by their _index_. Just as in JavaScript, indices
of a sequence begin at 0 and increase by 1 with each step down the sequence:

```js
// JavaScript
const my_list = [1, 2, 3, 4]
console.log(my_list[0])
// 1
```

```py
# Python
my_list = [1, 2, 3, 4]
print(my_list[0])
# 1
```

`list` and `tuple` objects can store any type of data, while `str` objects
can only store unicode characters.

## When Are Sequences Used?

Whenever values are logically connected to one another and it is important to
keep them in order, you should store them in a sequence data structure.

```py
# A dynamic sequence of values that allows duplicates
fibonacci_list = [1, 1, 2, 3, 5, 8, 13, 21]

# An immutable, ordered sequence of months
month_tuple = (
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December',
)

# A grammatical sentence
sentence_string = "Strings are immutable sequences of Unicode code points."
```

After being defined, sequences can be used as more complex data structures such as
_queues_ and _stacks_. We will discuss these more later on in this module.

<div style="border: 3px solid #00EEE0; margin: 15px; padding: 15px; width: 65%;">
    <p style="color: #00EEE0; font-size: 1.5em;"><strong>Check for Understanding</strong></p>
    <p>Which sequence type is surrounded by parentheses?</p>
    <div id="dialog_for_link1" class="enhanceable_content dialog" title="Answer">
        <p>Tuples!</p>
    </div>
    <p class="visible-desktop"><a id="link1" class="Button"
    href="#dialog_for_link1">Check Your Answer</a></p>
</div>

## Lists

We've encountered lists in several of our lessons so far. Lists are the most
common data structure you will see as a Python developer and provide a number
of different tools for manipulating data.

## Tuples

## Strings

## Instructions

## Resources

- [Defining Your Own Python Function](https://realpython.com/defining-your-own-python-function/)
