
example1 = "C:\\apps\\Books-List\\Training\\subtitle-1.txt"
file1 = open(example1, "r")
FileContent = file1.readlines()
#print(FileContent)
file1.close()

with open(example1,"r") as file1:
    content = file1.readlines()
   # print(content)

print(file1.closed)



with open("C:\\apps\\Books-List\\Training\\temp.txt","w") as wFile1:
    wFile1.write("Hello")


with open("C:\\apps\\Books-List\\Training\\temp.txt",'a+') as testwritefile:
    testwritefile.write("This is line E\n")
    print(testwritefile.read())


with open("C:\\apps\\Books-List\\Training\\temp.txt", 'a+') as testwritefile:
    print("Initial Location: {}".format(testwritefile.tell()))
    
    data = testwritefile.read()
    if (not data):  #empty strings return false in python
            print('Read nothing') 
    else: 
            print(testwritefile.read())
            
    testwritefile.seek(0,0) # move 0 bytes from beginning.
    
    print("\nNew Location : {}".format(testwritefile.tell()))
    data = testwritefile.read()
    if (not data): 
            print('Read nothing') 
    else: 
            print(data)
    
    print("Location after read: {}".format(testwritefile.tell()) )

