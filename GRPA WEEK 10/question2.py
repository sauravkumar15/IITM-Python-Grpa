'''
GRPA 2 - String Manipulation Class - GRADED

Problem statement:
Implement a class `StringManipulation` that provides various operations on a 
list of words. The class should support the following methods:

1. total_words(): returns the total number of words
2. count(some_word): returns how many times some_word occurs (case insensitive)
3. words_of_length(length): returns all words of a given length
4. words_start_with(char): returns all words that start with a given character
5. longest_word(): returns the longest word
6. palindromes(): returns all palindrome words

Function Specification:
class StringManipulation:
    __init__(self, words):
        Initialize the object with a list of words (case insensitive)

    total_words(self):
        Returns the total number of words

    count(self, some_word):
        Returns the number of times some_word appears

    words_of_length(self, length):
        Returns a list of words of given length

    words_start_with(self, char):
        Returns words starting with the given character

    longest_word(self):
        Returns the longest word

    palindromes(self):
        Returns a list of palindrome words
'''

# Solution

class StringManipulation:
    def __init__(self, words):
        # Store words in lowercase for uniformity
        self.words = [word.lower() for word in words]

    def total_words(self):
        return len(self.words)

    def count(self, some_word):
        return self.words.count(some_word.lower())

    def words_of_length(self, length):
        return [word for word in self.words if len(word) == length]

    def words_start_with(self, char):
        return [word for word in self.words if word.startswith(char.lower())]

    def longest_word(self):
        return max(self.words, key=len)

    def palindromes(self):
        return [word for word in self.words if word == word[::-1]]


# Example usage
words = ["Madam", "level", "apple", "banana", "noon", "data", "science"]
obj = StringManipulation(words)

print("Total words:", obj.total_words())                 # 7
print("Count of 'apple':", obj.count("apple"))           # 1
print("Words of length 5:", obj.words_of_length(5))      # ['level', 'apple']
print("Words starting with 'b':", obj.words_start_with("b"))  # ['banana']
print("Longest word:", obj.longest_word())               # 'banana'
print("Palindromes:", obj.palindromes())                 # ['madam', 'level', 'noon']
