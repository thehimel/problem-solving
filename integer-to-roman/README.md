# Integer to Roman Numeral Conversion

## Problem Statement

Write a function to convert an Integer to Roman numeral.

## Roman Numerals

According to Wikipedia, Roman numerals are a numeral system that originated in ancient Rome and remained the usual way of writing numbers throughout Europe well into the Late Middle Ages. Numbers in this system are represented by combinations of letters from the Latin alphabet. Modern usage employs seven symbols, each with a fixed integer value. [More Information](https://en.wikipedia.org/wiki/Roman_numerals)

Value | Symbol
--- | ---
1000 | M
900 | CM
500 | D
400 | CD
100 | C
90 | XC
50 | L
40 | XL
10 | X
9 | IX
5 | V
4 | IV
1 | I

## Example Conversions of Integer to Roman Numerals

Integer | Roman
--- | ---
15 | XV
16 | XVI
18 | XVIII
28 | XXVIII
37 | XXXVII
48 | XLVIII
58 | LVIII
74 | LXXIV
86 | LXXXVI
89 | LXXXIX
800 | DCCC
2596 | MMDXCVI
3000 | MMM
4889 | MMMMDCCCLXXXIX
6000 | MMMMMM

## How to Convert?

Let's convert 58.

```python
num = 58
result = ''

(value, symbol) = (50, 'L')
58 // 50 = 1
result = result + 'L'
result = 'L'
num = 58 % 50
num = 8

(value, symbol) = (5, 'V')
8 // 5 = 1
result = result + 'V'
result = 'LV'
num = 8 % 5
num = 3

(value, symbol) = (1, 'I')
3 // 1 = 3
result = 'LV' + 'III'
result = 'LVIII'
```

## Running the Program

- `python run.py`

## Test

pytest is used to test the solution.

- Install pytest: `pip install pytest`
- While being in the directory. Simply type: `pytest`
- You can also type: `pytest -q test_solution.py`

## Time Complexity

Time complexity of this algorithm is O(n).

## Edge Cases

- Input must me an integer.
- Roman numbers can only be positive. Thus, input must be a positive number.
