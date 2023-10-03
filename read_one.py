from db_config import Customer_list


def find_customer(id):
    cld = Customer_list.get_by_id(id)
    print(cld.id, cld.customer, cld.age, cld.pub_date)

if __name__ == "__main__":
    id = 1
    find_customer(id)