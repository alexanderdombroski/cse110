'''
books = open("week11/books.txt", "r") # works if python folder is opened in vscode
books = open("books.txt", "r") # works if week 11 folder is opened in vs code
print(books.read())
books.close()
'''

# This does the exact same thing
with open("books.txt") as bookfile: # You won't have to close the file if you do it like this. It's important to close the file so that if it's edited the data will be saved.
    for line in bookfile:
        print(line.strip())