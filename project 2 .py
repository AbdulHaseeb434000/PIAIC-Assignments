text_in = input("Enter text: ")
a= []
for i in text_in:
    a.insert(0,i)
for i in a:
    print(i,end="")
