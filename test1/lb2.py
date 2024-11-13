pages = 100
rows = 50
characters = 25
bytess = 4
page_size = rows * characters * bytess
book = pages * page_size
diskette_size = 1.44 * 1024 * 1024
number_of_books = diskette_size // book
print("Количество книг, помещающихся на дискету:", int(number_of_books))
