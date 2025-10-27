import time

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
            

def register_car(cars, car_spot, logged_in_user):
    while True:
        if logged_in_user in cars:
            print("User has already registered a car")
            return None
        cars[logged_in_user] = input("Register your car: ")
        print(cars)
        car_spot
        choose_parking_spot(car_spot)
        spot = input("Choose a parking spot: ")
        car_spot[cars[logged_in_user]] = spot
        print(car_spot)


def choose_parking_spot(car_spot):
    print(car_spot)
    print("Available parking spots")
    print()
    for spot in car_spot:
        if len(car_spot) > 3:
            print(f"{car_spot[spot]} \n |*|")
        else:
            print(f"{car_spot[spot]} \n | |")
    return

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
    car_spot = {"1":"D1", "2":"D2", "3":"D3", "4":"D4", "5":"D5"}
    cars = {}
    in_tid = None

    while True:
        choice_menu = menu("Welcome to the garage", "Option: ", {"l":"Log in", "c":"Create new user", "q":"Quit"})
        if choice_menu == "l":
            login_choice = log_in(users)

            if login_choice is None:
                continue



            second_choice = menu(f"Welcome {login_choice}", "Option: ", {"d":"Drive in", "c":"Check time", "do":"Drive out", "l":"Log out"})
            if second_choice == "d":
                register_car(users, cars, login_choice)
        elif choice_menu == "c":
            create_new_user(users)
            print(users)
        else:
            continue

register_car({"user1":"CarA"}, {"1":"D1", "2":"D2", "3":"D3"}, "user2")


#main()

#Yadayada