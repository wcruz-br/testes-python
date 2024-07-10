S = input()
alphanumeric = False
alphabetical = False
digits = False
lowercase = False
uppercase = False
for i in range(len(S)):
    substring = S[i]
    if substring.isalnum():
        alphanumeric = True
    if substring.isalpha():
        alphabetical = True
    if substring.isdigit():
        digits = True
    if substring.islower():
        lowercase = True
    if substring.isupper():
        uppercase = True

print(alphanumeric)
print(alphabetical)
print(digits)
print(lowercase)
print(uppercase)
