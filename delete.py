from db_config import Customer_list


def delete_customer(id):
    cld = Customer_list.get_by_id(id)
    cld.delete_instance()

if __name__ == "__main__":
    id = 4
    delete_customer(id)