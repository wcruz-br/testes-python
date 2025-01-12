def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def is_palindrome(word):
    if len(word) == 0:
        return True
    elif first(word) != last(word):
        return False
    return is_palindrome(middle(word))

print(is_palindrome("abacate"))
print(is_palindrome("coco"))
print(is_palindrome("ovo"))
print(is_palindrome("socorrammesubinoonibusemmarrocos"))
print(is_palindrome("pqp"))
print(is_palindrome("poop"))
print(is_palindrome("a"))
print(is_palindrome("aa"))
print(is_palindrome(""))
