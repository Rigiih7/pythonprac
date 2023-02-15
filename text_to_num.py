def string_to_number(string):
# Create a dictionary with the string values and their corresponding numeric values
number_dict = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    "eleven": 11,
    "twelve": 12,
    "thirteen": 13,
    "fourteen": 14,
    "fifteen": 15,
    "sixteen": 16,
    "seventeen": 17,
    "eighteen": 18,
    "nineteen": 19,
    "twenty": 20,
    "thirty": 30,
    "forty": 40,
    "fifty": 50,
    "sixty": 60,
    "seventy": 70,
    "eighty": 80,
    "ninety": 90,
    "hundred": 100,
    "thousand": 1000,
    "million": 1000000
}

# Split the string into a list of words
words = string.split()

# Initialize the result to 0
result = 0

# Iterate through the list of words
for i, word in enumerate(words):
# Check if the word is a number word
if word in number_dict:
# If the word is "hundred", multiply the result by 100
if word == "hundred":
result *= 100
# If the word is "thousand" or "million", add the result so far to the final result and reset the result to the value of the word
elif word == "thousand" or word == "million":
result += number_dict[word]
result *= number_dict[word]
# Otherwise, add the value of the word to the result
else :
result += number_dict[word]

# Return the final result
return result

# Test the function
print(string_to_number("one"))
print(string_to_number("twelve"))
print(string_to_number("one hundred"))
print(string_to_number("one thousand"))
print(string_to_number("one million"))