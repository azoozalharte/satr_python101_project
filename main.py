user_input = input(
    "To find the user by number type 'num', to find my the name type 'name'")


numbers = {
    1111111111: "Amal",
    2222222222: "Mohamed",
    3333333333: "Azooz",
    4444444444: 'Ali'
}


def find_by_name(user_input):
    for key in numbers:
        if numbers[key] == user_input:
            return key
        else:
            return 'Sorry, the name is not found'


def find_by_number(user_input):
    if len(user_input) < 10 or len(user_input) > 10:
        return "This is invalid number"

    for key in numbers:
        if int(user_input) == key:
            return numbers[key]
        else:
            return 'Sorry, the number is not found'


if user_input == 'num':
    number = input("type the number you want to find: ")
    print(find_by_number(number))
else:
    name = input("type the user name you want to find: ")
    print(find_by_name(name))
