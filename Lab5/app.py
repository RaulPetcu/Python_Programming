from utils import process_item

while True:
    user_input = input("Enter input:")
    if user_input == "q":
        break
    else:
        number = int(user_input)
        print(process_item(number))


