# strings : ordered, immutable, allows duplicate elements, test representation of text data, can be declared using single or double quotes
my_strings = "HELLO WORLD"

my_strings = my_strings.lower() #convert to lowercase
print(my_strings)

substring = my_strings[0:5] #slicing
print(substring)

substring = my_strings[-5:] #slicing
print(substring)

substring = my_strings[::2] #slicing
print(substring)

substring = my_strings[1::2] #slicing
print(substring)

greeting = "Hello"
name = "Ali"

sentence = greeting + " " + name #concatenation
print(sentence)

for i in my_strings:
    print(i)

if "hello" in my_strings:
    print("Yes, 'hello' is in the string")
else:
    print("No, 'hello' is not in the string")

my_strings = "   hello world   "
print(my_strings.strip()) #removes whitespace from the beginning and end of the string

print(my_strings.replace("hello", "hi")) #replaces a specified phrase with another specified phrase
print(my_strings.split(" ")) #splits the string into a list where each word is a list item
print(my_strings.upper()) #converts the string to uppercase
print(my_strings.lower()) #converts the string to lowercase
print(my_strings.capitalize()) #converts the first character of the string to uppercase
print(my_strings.title()) #converts the first character of each word to uppercase
print(my_strings.count("l")) #returns the number of times a specified value occurs in a string
print(my_strings.find("world")) #returns the index of the first occurrence of a specified value in a string
print(my_strings.startswith("hello")) #returns True if the string starts with the specified value
print(my_strings.endswith("world")) #returns True if the string ends with the specified value
print(my_strings.isalpha()) #returns True if all characters in the string are alphabetic
print(my_strings.isdigit()) #returns True if all characters in the string are digits
print(my_strings.isalnum()) #returns True if all characters in the string are alphanumeric
print(my_strings.islower()) #returns True if all characters in the string are lowercase
print(my_strings.isupper()) #returns True if all characters in the string are uppercase

#strings can also be formatted using f-strings, which allow you to embed expressions inside string literals, using curly braces {}.
print(f"My name is {name} and I am {28} years old.")
print(f"The sum of 5 and 10 is {5 + 10}.")


#strings and lists can be converted to each other using the list() and join() methods.

my_string = 'how, are, you, doing'
my_list = my_string.split(', ')
print(my_list)

new_string = ', '.join(my_list)
print(new_string)


