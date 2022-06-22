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

## [Common Sequence Operations][common sequence operations]

All sequence data types in Python support certain functions and operators and
possess certain methods. For a sequence `s`:

- `x in s` returns `True` if `x` is equal to at least one element of `s`.

- `s + s2` returns a single sequence of the elements of `s` followed by the
elements of `s2`.

- `s * n` returns a single sequence of `s` repeated `n` times.

- `s[i]`returns the `i`th element of `s` (starting at 0).
    > NOTE: Python also supports negative indices. `-1` represents the last
    element in a sequence.

- `s[i:j]` returns a _slice_ of `s` from index `i` to index `j`.

- `s[i:j:k]` returns a slice of `s` from `i` to `j` with steps of `k` in
between.

- `len(s)` returns the number of elements in `s`.

- `min(s)` and `max(s)` return the minimum and maximum values in `s`,
respectively.
    > NOTE: this requires the elements of `s` to be of
the same data type, either `str` or numerical.

- `s.index(x)` returns the index of the first `x` in `s`.

- `s.count(x)` returns the number of instances of `x` in `s`.

Open up the Python shell and test each of these operations for yourself:

```py
s = [4, 6, 3, 9, 3, 5, 1, 2]
1 in s
# True
s + s
# [4, 6, 3, 9, 3, 5, 1, 2, 4, 6, 3, 9, 3, 5, 1, 2]
s * 2
# [4, 6, 3, 9, 3, 5, 1, 2, 4, 6, 3, 9, 3, 5, 1, 2]
s[1]
# 6
s[-1]
# 2
s[2:5]
# [3, 9, 3]
s[2:5:2]
# [3, 3]
len(s)
# 8
min(s)
# 1
max(s)
# 9
s.index(3)
# 2
s.count(9)
# 1
```

<div style="border: 3px solid #00EEE0; margin: 15px; padding: 15px; width: 65%;">
    <p style="color: #00EEE0; font-size: 1.5em;"><strong>Check for Understanding</strong></p>
    <p>How would you retrieve the last two elements of a sequence if you don't
    know the length?</p>
    <div id="dialog_for_link2" class="enhanceable_content dialog" title="Answer">
        <p>s[-1:-3:-1]</p>
        <p><em>Though you can always check the length first with len()!</em></p>
    </div>
    <p class="visible-desktop"><a id="link2" class="Button"
    href="#dialog_for_link2">Check Your Answer</a></p>
</div>

## Lists

We've encountered lists in several of our lessons so far. Lists are the most
common data structure you will see as a Python developer and provide a number
of different tools for manipulating data.

### Sorting Lists

Python provides two straightforward solutions for sorting lists: the
`list.sort()` method and the `sorted()` function. Both of these solutions
require that all elements of the list be of the same data type.

`list.sort()` rearranges the elements of a list so that they are in order
alphanumerically.

```py
my_list = [3, 6, 4, 2, 1, 5]
my_list.sort()
print(my_list)
# [1, 2, 3, 4, 5, 6]
```

`sorted()` returns an alphanumerically sorted copy of the original list. This
function should be used when you want to preserve the integrity of your
original list, but you need a sorted version for a separate task.

```py
my_list = [3, 6, 4, 2, 1, 5]
sorted_list = sorted(my_list)
print(my_list)
# [3, 6, 4, 2, 1, 5]
print(sorted_list)
# [1, 2, 3, 4, 5, 6]
```

### 

## Tuples

## Strings

## Instructions

## Resources

- [Common Sequence Operations][common sequence operations]
- [Sequence Types](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range)
- [More on Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)

[common sequence operations]: https://docs.python.org/3/library/stdtypes.html#common-sequence-operations