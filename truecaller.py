from sys import argv

choice = input("Tell us if you want to 'search' a particular contact or 'add' a contact (s / a): ")
if choice.lower() == "s" or choice.lower() == "search":
    with open(argv[1], "r") as phone_book:
        search_type = input("search by name or number: ")
        try:
            a = int(search_type)
            for line in phone_book:
                bucket = line.split(":")
                if int(bucket[1]) == a:
                    print(bucket[0])
        except ValueError:
            for line in phone_book:
                bucket = line.split(":")
                if bucket[0].lower() == search_type.lower():
                    print(bucket[1])
elif choice.lower() == "a" or choice.lower() == "add":
    with open(argv[1], "a") as phone_book:
        name = input("enter person's name: ")
        number = int(input("enter person's number: "))
        phone_book.writelines(f"\n{name}:{number}")

else:
    print("You need to type 'search' or 'add' to perform the desired operation!" )
