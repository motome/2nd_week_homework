from db_config import Customer_list

# インスタンスを生成しないでcreate
def create_Customer_list():
    Customer_list.create(customer="Bob", age=15)
    Customer_list.create(customer="Tom", age=57)
    Customer_list.create(customer="Ken", age=73)

if __name__ == "__main__":
    create_Customer_list()