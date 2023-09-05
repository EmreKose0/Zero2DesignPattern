customers = []


def CustomerCreate (name,surname,email,phone):
    new_Customer = {
        "Name":name,
        "Surname":surname,
        "Email":email,
        "Phone":phone,
        "Orders":[]
    }
    customer_id = len(customers) + 1
    new_Customer["id"] = customer_id
    customers.append(new_Customer)


def CreateOrder (customer_id,item,count,orderDate):
    for customer in customers:
        if customer["id"] == customer_id:
            new_Order = {
                "Item":item,
                "Count":count,
                "OrderDate":orderDate
            }
            customer["Orders"].append(new_Order) 
            break
        else:
            print(f"Müşteri ID bulunamadı: {customer_id}")

CustomerCreate("Emre", "Köse", "emrekose1995@gmail.com", "5524070651")
CreateOrder(1, "Ürün A", 2, "2023-09-05")


def ShowCustomers():
    for customer in customers:
        print(f"Müşteri ID: {customer['id']}")
        print(f"Adı: {customer['Name']}")
        print(f"Soyadı: {customer['Surname']}")
        print("Siparişler:")
        for order in customer["Orders"]:
            print(f"Ürün: {order['Item']}")
            print(f"Miktar: {order['Count']}")
            print(f"Sipariş Tarihi: {order['OrderDate']}")
        print()

ShowCustomers()
