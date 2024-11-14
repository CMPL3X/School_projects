import os

file = open("Webpages\\Test_File.txt", "a")
file.write("Heee Heeee!")
file.close()

file = open("Webpages\\Test_File.txt", "r")
print(file.read())

file.close()
os.remove("Webpages\\Test_File.txt")
