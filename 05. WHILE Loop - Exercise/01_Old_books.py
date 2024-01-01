favourite_book = input()
book_name = input()
number_of_books = 0
is_found = False

while book_name != "No More Books":

    if favourite_book == book_name:
        is_found = True
        break

    number_of_books += 1
    book_name = input()

if is_found:
    print(f"You checked {number_of_books} books and found it.")
else:
    print(f"The book you search is not here!")
    print(f"You checked {number_of_books} books.")
