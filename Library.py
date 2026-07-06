Books = []

while True:
    print("Please choose the option you want. Use the numbers")
    print("1.Add books")
    print("2.Show the books")
    print("3.Remove the books")
    print("4.Search the books")
    print("5.Exit")

    choose = input("Insert The Operation: ")

    if choose.strip() == "1":
        get_book = input("What Book Do You Want To Add? ").strip()

        if get_book.lower() in [book.lower() for book in Books]:
            print("This Book Already Exists")
        else:
            Books.append(get_book)
            print("The Book Added Successfully")

    elif choose.strip() == "2":
        if len(Books) == 0:
            print("No Books Available")
        else:
            print("Books List:")
            for book in Books:
                print(book)

    elif choose.strip() == "3":
        while True:
            Delete_book = input(
                "Write The Book Name That You Want To Delete. Insert 00 to exit: "
            ).strip()

            if Delete_book == "00":
                print("We Got Out")
                break

            found = False

            for book in Books:
                if book.lower() == Delete_book.lower():
                    Books.remove(book)
                    print("It Deleted Successfully")
                    found = True
                    break

            if not found:
                print("The Book Wasn't Found")

    elif choose.strip() == "4":
        while True:
            search_book = input(
                "Write The Book Name To Search. Insert 00 to exit: "
            ).strip()

            if search_book == "00":
                break

            elif search_book.lower() in [book.lower() for book in Books]:
                print("Available")

            else:
                print("We Couldn't Find Out The Book")

    elif choose.strip() == "5":
        print("Exit Successfully")
        break

    else:
        print("Wrong")