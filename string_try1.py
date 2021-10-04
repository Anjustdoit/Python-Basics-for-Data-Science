name = "hello"
print(type(name))
message = 'john said to me "I\'ll see you later"'
print(message)

paragraph = ''' Hi , I'm writing a book.
                I will certainly do'''
print(paragraph)

hello = "Hello World!"
print(hello)
name = input('What is your name ? --> ')
print(name)

# What is your age 

age = input('What is your age ? --> ')
print(age)

string = "you name is {} and you age is {}"
output = string.format(name,age)
print(output)

A = "part"
B=1
#print(A+str(B))
AF = "{} - {}".format(A,B)
print(AF)