# Prompt 1 Tuples Sort List Ascending ---
subjects = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

# Handler for ascending order output based on number
sorted_subjects = sorted(subjects, key=lambda x: x[1])

print(sorted_subjects) # Output: [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]

# Prompt 2 Lambda Cube of each item ---
numbers = [3, 6, 9, 2]

# Handler for Cubing each item in array/list
cubed_numbers = list(map(lambda x: x**3, numbers))

print(cubed_numbers) # Output: [27, 216, 729, 8]

# Prompt 3 True False & Even Odd lambda  using number array from prompt 2 ---
## Handler for if number is even or not
is_even = lambda x: x % 2 == 0

## Making a list of True or False
boolean_list = [is_even(num) for num in numbers]

print(boolean_list) #Output: [False, True, False, True]

# Prompt 4 List to 100 ---
numbers = [x for x in range(1, 101)]
# Must be set to 101 otherwise output will only reach 99

print(numbers) # Output: 1-100 in an array/list

# Prompt 5 Dictionary Comprehension ---
sentence = "The quick brown fox jumped over the fence."

# Handler for outputting the words phonetically in order
word_lengths = {word: len(word) for word in sentence.split()}

print(word_lengths) # Output: {'The': 3, 'quick': 5, 'brown': 5, 'fox': 3, 'jumped': 6, 'over': 4, 'the': 3, 'fence.': 6}