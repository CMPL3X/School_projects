import os

file = open("Webpages\\Test_File.txt", "a")
file.write("Heee Heeee!")
file.write("\nhttps://www.youtube.com/watch?v=dQw4w9WgXcQ")
file.close()

file = open("Webpages\\Test_File.txt", "r")
print(file.read())

link = file.readline()
print(link)

file.close()
os.remove("Webpages\\Test_File.txt")