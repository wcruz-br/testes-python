string = input()

def splitjoin(string):
    words = string.split(" ")
    return "-".join(words)

print(splitjoin(string))
