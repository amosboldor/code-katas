Code-Katas
----------

--------------------
**Double Char**
- **Module:** double_char.py
- **Tests:** test_double_char.py
- **Link:** [https://www.codewars.com/kata/double-char/python](https://www.codewars.com/kata/double-char/python)

**Interesting Solution:**
```
def double_char(s):
    return ''.join(c * 2 for c in s)
```

--------------------
**Even or Odd**
- **Module:** even_or_odd.py
- **Tests:** test_even_or_odd.py
- **Link:** [https://www.codewars.com/kata/even-or-odd/python](https://www.codewars.com/kata/even-or-odd/python)

**Interesting Solution:**
```
def even_or_odd(number):
    return 'Odd' if number % 2 else 'Even'
```

--------------------
**Sum of Positive**
- **Module:** sum_of_positive.py
- **Tests:** test_sum_of_positive.py
- **Link:** [https://www.codewars.com/kata/sum-of-positive/python](https://www.codewars.com/kata/sum-of-positive/python)

**Interesting Solution:**
```
def positive_sum(arr):
    ''' I really hate these one line codes, but here I am...
        trying to be cool here... and writing some'''
    return sum(map(lambda x: x if x > 0 else 0, arr))
```

--------------------
**Convert Number to Reversed Array of Digits**
- **Module:** reversed_list_of_digits.py
- **Tests:** test_reversed_list_of_digits.py
- **Link:** [https://www.codewars.com/kata/convert-number-to-reversed-array-of-digits/python](https://www.codewars.com/kata/convert-number-to-reversed-array-of-digits/python)

**Interesting Solution:**
```
def digitize(n):
    return map(int, str(n)[::-1])
```

--------------------
**Opposite Number**
- **Module:** opposite_number.py
- **Tests:** test_opposite_number.py
- **Link:** [https://www.codewars.com/kata/opposite-number/python](https://www.codewars.com/kata/opposite-number/python)

**Interesting Solution:**
```
def opposite(number):
    return -number
```

--------------------
**Counting Sheep**
- **Module:** counting_sheep.py
- **Tests:** test_counting_sheep.py
- **Link:** [https://www.codewars.com/kata/counting-sheep-dot-dot-dot/python](https://www.codewars.com/kata/counting-sheep-dot-dot-dot/python)

**Interesting Solution:**
```
def count_sheeps(arrayOfSheeps):
    return arrayOfSheeps.count(True)
```

--------------------
**Jenny's Secret Message**
- **Module:** jennys_secret_message.py
- **Tests:** test_jennys_secret_message.py
- **Link:** [https://www.codewars.com/kata/jennys-secret-message/python](https://www.codewars.com/kata/jennys-secret-message/python)

**Interesting Solution:**
```
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)
```

--------------------
**A Needle in the Haystack**
- **Module:** needle_in_the_haystack.py
- **Tests:** test_needle_in_the_haystack.py
- **Link:** [https://www.codewars.com/kata/a-needle-in-the-haystack/train/python](https://www.codewars.com/kata/a-needle-in-the-haystack/train/python)

**Interesting Solution:**
```
def find_needle(haystack): return 'found the needle at position %d' % haystack.index('needle')
```

--------------------
**Sum Without Highest and Lowest Number**
- **Module:** sum_without_high_and_low.py
- **Tests:** test_sum_without_high_and_low.py
- **Link:** [https://www.codewars.com/kata/sum-without-highest-and-lowest-number/python](https://www.codewars.com/kata/sum-without-highest-and-lowest-number/python)

**Interesting Solution:**
```
def sum_array(arr):
    if arr == None or len(arr) < 3:
        return 0
    return sum(arr) - max(arr) - min(arr)
```

--------------------