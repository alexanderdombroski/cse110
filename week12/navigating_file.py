with open("books_and_chapters.txt") as cd:
    
    max_chapters = 0
    max_chapters_book = ""

    bom_max_chapters = 0
    bom_max_chapters_book = ""
    
    target_scripture = ""
    tar_max_chapters = 0
    tar_max_chapters_book = ""

    while target_scripture not in ["Book of Mormon", "Pearl of Great Price", "Doctrine and Covenants", "New Testament", "Old Testament"]:
        target_scripture = input("Enter a book of scripture you want to learn about: ")
    for line in cd:
        line = line.strip()
        data = line.split(":")
        book, chapters, scripture = data[0], int(data[1]), data[2]
        # print(f"Scripture: {scripture}, Book {book}, Chapters: {chapters}")
        if  max_chapters < chapters:
            max_chapters = chapters
            max_chapters_book = book

        # Stretch Challenge
        if scripture == "Book of Mormon":
            # print(f"Scripture: {scripture}, Book {book}, Chapters: {chapters}")
            if  bom_max_chapters < chapters:
                bom_max_chapters = chapters
                bom_max_chapters_book = book
        
        if scripture == target_scripture:
            if tar_max_chapters < chapters:
                tar_max_chapters = chapters
                tar_max_chapters_book = book

print(f"\nThe longest book in the scriptures is the book of {max_chapters_book} with {max_chapters} chapters.")
print(f"The longest book in the Book of Mormon is the book of {bom_max_chapters_book} with {bom_max_chapters} chapters.")
print(f"The longest book in the {target_scripture} is the book of {tar_max_chapters_book} with {tar_max_chapters} chapters.\n")