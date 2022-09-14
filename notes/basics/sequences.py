# python sequence types
# string
# list
# touple
# range
# byte and bytearray

# sequences are an ordered set of items
# you can index a list to get a string and then index that string

computer_parts = ["computer", "monitor"]
print(computer_parts[1])
print(computer_parts[1][0])

# most operations that can be done on a str can be done on the other sequence items
# a range cannot be concatenated or multiplied

string1 = 'hello '
string2 = 'world'

print(string1 + string2)    #concatenate
print(string1 * 5)          #multiiply

#operation precendence still applies
#print(string1 * 5 + 4) will result in an error because it will multiply the string 5 times then try to add and int to a str

#you can check for substrings within a string

today = 'friday'
print('day' in today)   #true
print('thur' in today)  #false