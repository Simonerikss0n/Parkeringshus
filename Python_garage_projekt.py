

def menu(title, prompt, options):
    print(f"{title}\n")
    for key in options:
        print(f"{key}) {options[key]}")
    print()
    while True:
        choice = input(f"{prompt}")
        if choice in options:
            print()
            return choice



def log_in(users):
    user = input("User: ")
    password = input("Password: ")
    while True:
        if user in users and users[user] == password:
            return user
        else:
            menu_choice = menu("\nInvalid username or password", "Option: ", {"r":"Try again", "q":"Quit"})
            if menu_choice == "q":
                return None
            

def register_car(users, cars, logged_in_user):
    while True:
        if logged_in_user in cars:
            print("User has already registered a car")
            return
    cars[logged_in_user] = input("Register your car: ")
    print(cars)



def create_new_user(users):
    while True:
        new_user = input("Username: ")
        new_password = input("Password: ")
        if new_user in users:
            print("Username already taken, choose another")
        else:
            users[new_user] = new_password
            return users


def main():
    users = {}
    user_data = {}
    cars = {}

    while True:
        choice_menu = menu("Welcome to the garage", "Option: ", {"l":"Log in", "c":"Create new user", "q":"Quit"})
        if choice_menu == "l":
            login_choice = log_in(users)
            second_choice = menu(f"Welcome {users[login_choice]}", "Option: ", {"d":"Drive in", "c":"Check time", "l":"Log out"})
            if second_choice == "d":
                register_car(users, cars, login_choice)
        elif choice_menu == "c":
            create_new_user(users)
            print(users)
        else:
            return

main()

#Yadayada