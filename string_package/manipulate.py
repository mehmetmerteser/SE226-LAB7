
import string

def reverse_string(s):
    return s[::-1]

def capitalize_words(s):
    return ' '.join(word.capitalize() for word in s.split())

def remove_punctuation(s):
    return ''.join(c for c in s if c not in string.punctuation)

if __name__ == "__main__":
    print(reverse_string("merhaba dünya!"))
