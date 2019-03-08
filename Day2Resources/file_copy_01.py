import shutil

# copy file
shutil.copy("folder1/hello.txt", "folder2")

# recursively copy an entire directory 
shutil.copytree("folder2", "folder2_backup")

# move file
shutil.move("folder2/hello.txt","folder2/anotherfolder")

# move and renamve file
shutil.move("folder2/anotherfolder/hello.txt","folder2/anotherfolder/newhello.txt")
