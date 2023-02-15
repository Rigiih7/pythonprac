def string_to_int(string):
  numbers = {
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
  words = string.split()
   # Initialize the result to 0
  result = 0
  # Initialize a temporary variable to hold the current value
  temp = 0
  for word in words:
    if word in numbers and numbers[word] < 100:
      temp += numbers[word]
    elif word == "hundred":
      result += temp * 100
      temp = 0
    elif word in ["thousand", "million"]:
      result *= numbers[word]
      result += temp
      temp = 0
   
    else:
      raise ValueError("Invalid input string")
  
  result += temp

  return result
print(string_to_int("one"))
print(string_to_int("seventeen"))
print(string_to_int("one hundred twenty three"))
print(string_to_int("one hundred ninety nine"))
print(string_to_int("nine hundred ninety nine"))
print(string_to_int("two hundred twenty one"))
print(string_to_int("two hundred ninety nine"))
