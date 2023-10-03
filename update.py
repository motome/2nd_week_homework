from db_config import Customer_list


def display_all_customer():
    for cld in Customer_list.select():
        print(cld.id, cld.customer, cld.age, cld.pub_date)


def update_customer(id):
    cld = Customer_list.get_by_id(id)
    cld.customer = "Tom Ford"
    cld.save()

if __name__ == "__main__":
    display_all_customer()

    id = 3
    update_customer(id)

    display_all_customer