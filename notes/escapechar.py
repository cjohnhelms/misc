# the escapte character is python is the \

splitString = "This string has been\nsplit over\nseveral\nlines"
print(splitString)

# \t is used to tab over
# escapaping can be useful with special characters

print('The pet shop owner said "No, he\'s resting."')

# triple quotes will allow you to not escape any quotes inside of the string

print("""The pet shop owner said "No, he's resting." """)

# triple quotes will also steings to be split over several lines without \n

anotherSplitString = """This string has been
split over
several
lines"""
print(anotherSplitString)

# how to include the \ charachter in a string, like in a Windows file path?
# you can escape a \ with another backslash, like \\

print('\\')

# or you can use a raw string, indicated by an r placed before the string

print(r"path\to\file")

# preferably just escape the backslash