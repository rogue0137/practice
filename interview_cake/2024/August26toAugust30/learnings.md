# Weekly Learnings: August26toAugust30

Back after COVID! I'm doing InterviewCake + Leetcode + Meta specific prep. My goal is to now document all my learnings and weak spots in no particular order!

# Learnings

## Python
- Duh, I forgot `zip` is a thing:
```Python
# LOWERCASE LETTER
  for original, ciphered in zip(lowercase_letters, rotated_lowercase_alphabet):
    ciphered_dictionary[original] = ciphered
```
- The following exist:
    - .isalpha()
    - .isalnum()
    - .upper()
    - .lower()
    - string.ascii_lowercase()
    - string.ascii_uppercase()
    - string.ascii_digits()
- Verbose versus Pythonic reminders
```Python
# MORE PYTHONIC:
def rotate_alphabet(rotation_factor, letters):
  rotation_factor = rotation_factor % len(letters)
  return letters[rotation_factor:] + letters[:rotation_factor]


# MORE VERBOSE
def rotate_alphabet(rotation_factor, letters):
  # rotated alphabet
  is_greater_than_26 = rotation_factor > 26
  # if number is greater than 26, divide by 26 and use the remainder
  if is_greater_than_26:
    alphabet_rotation_factor = rotation_factor % 26
  else:
    alphabet_rotation_factor = rotation_factor
  
  # split the list in two, ex. 9 is the remainder
  # take last 9 apart from group
  before_rotation = letters[:alphabet_rotation_factor]
  after_rotation = letters[alphabet_rotation_factor:]
  new_alphabet_order = after_rotation + before_rotation

  return new_alphabet_order
```
- Ooooh, I can specify defaults:
```Python
# if char is not found in the dictionary, use the original char
ciphered_dictionary.get(char, char)
```
- This is a generator
```Python
ciphered_dictionary.get(char, char) for char in input_str
```

## TODO

### Arrays
- [ ] redo `Passing Yearbooks` by only going through the array once. Use cycles
- [ ] redo `Contiguous Subarrays` using forward pass and backwards pass

### Strings
- I am very weak in the strings section; come back to

### 
