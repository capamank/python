data=True
line=1
word=str(input("enter the word you have to find in the data.txt file"))
with open ("data.txt","r") as f:
    while data:
        data=f.readline()
        print(data)
        if (word in data):
            print(f"your {word} found at line no. {line}")
        line+=1    