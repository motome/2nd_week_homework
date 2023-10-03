from db_config import Customer_list

print("===== Welcome to CRM Application =====")
print("[S]how: Show all users info")
print("[A]dd: Add new user")
print("[Q]uit: Quit The Application")
print("======================================")

def order_selection():
    select = input(
        "=======================================\n"
        "Please select your order, S, A, or Q \n"
        "==========================================\n"
        ">"
    )
    return select


def display_all():
    print("Your command > S ")
    for customer in Customer_list.select():
        print(f"Customer's Name: {customer.customer} Age: {customer.age}")


def add_data():
    print("Your command > A ")

    user_name = input("New user name >")
    user_age = input("New user age >")
    new_customer = Customer_list(customer=user_name, age=user_age)
    new_customer.save()
    print(f"Add new user: {user_name}")


def finish_operation():
    print("Bye!")


def main():
    while True:
        select = order_selection()

        if select == "S":
            display_all()
            continue

        elif select == "A":
            add_data()
            continue

        elif select == "Q":
            print("Your command > Q ")
            finish_operation()
            break

        else:
            print(f"Your command > {select}")
            print("command undefined")


if __name__ == "__main__":
    main()
