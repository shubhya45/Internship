txt="Hello world binary"
txt1="\nThis is python programing Language"
with open ("binary.bin","wb") as file:
    file.write(txt.encode())
    file.write(txt1.encode())
    
with open ("binary.bin","rb") as file:
    decodei=file.read()
    print(decodei.decode())
    