file=open("notes.txt","a+")# file create
# file.write("This is python programing ")# writing the content of file

# file.write("""Hello world
#           how are you
#            I am studying in k.k wagh polytechnic nashik""")
# print(file.tell()) # to check the pointer position
# file.seek(0)# used to set the pointer position as require
# print(file.read())
# file.close()
# print(file.readlines())
with open("notes.txt","w+")as file:
    file.write("This is python programing ")
    file.write("""Hello world
          how are you
          I am studying in k.k wagh polytechnic nashik""")
   
# print(file.readlines())
    file.seek(0)
    count=0
    for i in file:
        count+=1
    print(f"Total number of lines in file:" ,count)
    file.seek(0)
    r=file.read()
    demo=r.split()
    print(f"Total number of word in file:",len(demo))
    
    print(f"Total number of character in file:",len(r))
    

