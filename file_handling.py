import os

# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists

class CreateFiles:

    def __init__(self, directory_path, table_start, table_end, start, end):
        self.directory_path = directory_path
        self.table_start = table_start
        self. table_end = table_end
        self.start = start
        self.end = end
        self.file_name = ''

    def write_file(self, table_num):
        write_file = open(self.file_name, 'w')
        write_file.write(f"This is table of {table_num}{self.table_start * '\n'}")
        write_file.close()

    def append_file(self, table_num):
        append_file = open(self.file_name, "a")
        for num in range(self.start, self.end):
            append_file.write(f'{table_num} * {num} = {table_num * num} \n')
        append_file.close()

    def read_file(self):
        read_file = open(self.file_name, "r")
        print(read_file.read())
        read_file.close()

    def remove_file(self):
        os.remove(self.file_name)

    def is_file_removed(self):
        if os.path.exists(self.file_name):
            read_file = open(self.file_name, "r")
            print(read_file.read())
        else:
          print("The file has already been removed. Therefore, fhe file does not exist.")

    def write_tables(self):
        for table_num in range(self.table_start, self.table_end):
            self.file_name = f'{self.directory_path}table_of_{table_num}.txt'
            if not os.path.exists(self.file_name):
                create_file = open(self.file_name, "x")
                create_file.close()

            self.write_file(table_num)
            self.append_file(table_num)
            self.read_file()

            self.remove_file()
            self.is_file_removed()

DIRECTORY_PATH = "C:/Users/DELL/OneDrive/Documents/shaheer/"
table_start = 2
table_end = 201
start = 1
end = 11

create_files = CreateFiles(DIRECTORY_PATH, table_start, table_end, start, end)
create_files.write_tables()