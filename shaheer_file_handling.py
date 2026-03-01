import os

# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists

FILE_PATH = "C:/Users/DELL/OneDrive/Documents/Arisha Website/story.txt"

if not os.path.exists(FILE_PATH):
    create_file = open(FILE_PATH, "x")
    create_file.close()

write_file = open(FILE_PATH, "w")
write_file.write('This is my new content. ')
write_file.close()

append_file = open(FILE_PATH, "a")
append_file.write('Going to add new line BLABLABLA.')
append_file.close()

read_file = open(FILE_PATH, "r")
print(read_file.read())
read_file.close()

os.remove(FILE_PATH)

if os.path.exists(FILE_PATH):
    read_file = open(FILE_PATH, "r")
    print(read_file.read())
else:
  print("The file has already been removed. Therefore, fhe file does not exist.")


