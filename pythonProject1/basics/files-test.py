import os.path

file_path = "C:/Users/chand/Downloads/demo.txt"
file1 = open(file_path, "r")

print(file1.readline())
print(file1.readline())

print(file1.read())

for x in file1:
    print(x)

file1.close()

wrt = open("C:/Users/chand/Downloads/demo2.txt", 'a')
wrt.write("Hello i am writing to you")

wrt.close()
read1 = open("C:/Users/chand/Downloads/demo2.txt")
print(read1.read())

wrt1 = open("C:/Users/chand/Downloads/demo2.txt", 'w')
wrt.write("OOPS")
wrt1.close()

read2 = open("C:/Users/chand/Downloads/demo2.txt", "r")
print(read2.read())

if os.path.exists("C:/Users/chand/Downloads/demo2.txt"):
    print("File is there")
else:
    print("File is not there")

