# make sure you have a hello.txt in your current working director
# same directory as your python script
helloFile = open("hello.txt", "w")
char_written = helloFile.write("THis is also another line\n")
print("No of character written:",char_written)
helloFile.close()

# reopen to display content
helloFile = open("hello.txt")
print(helloFile.read())
helloFile.close()
 
# open the file for adding next text
helloFile = open("hello.txt", "a")
char_written = helloFile.write("Hello world again\n")
print("No of character written:",char_written)
helloFile.close()

# reopen to display content
helloFile = open("hello.txt")
print(helloFile.read())
helloFile.close()
