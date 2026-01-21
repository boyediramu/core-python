# Create a string variable called name and store your name. Print it
name="ram"
print(name)

# Find the length of the string 
text="python"
print(len(text))

# Print the first character of the string
text="hello"
print(text[0])

# Print the last character of the string
text="world"
print(text[-1])

# Print each character of the string
text="ramu"
for character in text:
    print(character)

# convert string to uppercase
text="hello world"
print(text.upper())

# join two strings with space 
a="hello"
b="world"
print(a+" "+b)

# repeat a string
text="hello"
for i in range(0,4):
    print(i,text)

# check the string type
text="python"
print(type(text))

# changing the string
text="ram"
text="R"
print(text)

# challange
word="code with python"
print(word[0])
print(word[-1])
print(len(word))
print(word.upper())

#challange
word="think code with python is easy to learn and understand"
text=word.split()
length=len(text)
for i in range(0,length):
    print(i,text[i])
print(text[3])

# string slicing
text="pythonprograming"
length=len(text)
print(length)
print(text[0:6])
print(text[7:])
print(text[-17:])
print(text[6:9])
print(text[::6])
print(text[::-1])

# challange
text="learningpython"
length=len(text)
print(length)
print(text[0:8])
print(text[8:])
print(text[5:9])
print(text[::-1])
    

# methods in string
text="   learning python is fun"
print(text.strip())
print(text)
print(text.upper())
print(text.lower())
print(text.replace("fun","easy"))
print(text.find("is"))
print(text.split())
word=text.split()
new_text="-".join(word)
print(new_text)

# user input with strings
name=input("enter your name")
print("helloo",name,"how are you")

# converting string to integer 
age=int(input("enter your age"))
print("your age is",(age +5))

challange
sentence=input("enter a any sentence")
words=sentence.upper()
word=words.lower()
total=sentence.split()
length=len(total)
print(total)
print("total number of words is",length)
print(sentence)
print(words)
print(word)


