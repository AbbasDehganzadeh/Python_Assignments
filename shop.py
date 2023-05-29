# from 'crud-shop.py' import add_product, del_product, edit_product
import csv


FILE = "./db.csv"
# HELP = "./help.txt"
MENU = {
    "A": "add",
    "B": "delete",
    "C": "edit",
    "D": "purchase",
    "E": "show products",
    "F": "search",
    "G": "exit",
    # "H": "help",
}


def add_product():
    teml = "Enter product {} Please? "
    product_id = int(products[-1]["id"]) + 1

    name = input(teml.format("name"))
    pid = search_products(name)
    price = input(teml.format("price"))
    amount = input(teml.format("amount"))

    if pid is not None:  # the product exists
        products[int(pid) - 1]["price"] = price  # mutating price
        n_amount = int(products[int(pid) - 1]["amount"]) + int(
            amount
        )  # increasing amount
        products[int(pid) - 1]["amount"] = n_amount
        return

    # append a product dictionary to the list of products
    products.append(
        dict(id=str(product_id).zfill(3)), name=name, price=price, amount=amount
    )


def del_product():
    k_world = input("Type a keyword please?")
    p_id = search_products(k_world)
    if p_id is not None:
        # Should keep the ID in safe
        products[int(p_id) - 1]["name"] = "name"
        products[int(p_id) - 1]["price"] = "price"
        products[int(p_id) - 1]["amount"] = "amount"


def edit_product():
    k_word = input("Type a keyword please?")
    product_id = search_products(k_word)
    if product_id is None:
        return
    p_id = int(product_id) - 1
    teml = "Enter product {} Please? ,({}) "
    p_name = input(teml.format("name", products[p_id]["name"]))
    p_price = input(teml.format("price", products[p_id]["price"]))
    p_amount = input(teml.format("amount", products[p_id]["amount"]))
    products[p_id]["name"] = p_name if p_name else products[p_id]["name"]
    products[p_id]["price"] = p_price if p_price else products[p_id]["price"]
    products[p_id]["amount"] = p_amount if p_amount else products[p_id]["amount"]


def show_products():
    print("Product list available")
    for product in products:
        print(
            "\t{};\t{},  {}, {}.".format(
                product.get("id", "None"),
                product.get("name", "No name"),
                product.get("price", "No price"),
                product.get("amount", "No amount"),
            )
        )


def search_products(expr: str):
    found = False
    for product in products:
        if (
            expr in product["id"]
            or expr in product["name"]
            or expr in product["price"]
            or expr in product["amount"]
        ):
            print(
                "Found product {} with ID {}, price {}, and amount {}".format(
                    product["name"],
                    product["id"],
                    product["price"],
                    product["amount"],
                )
            )
            found = True
            return product["id"]

    if not found:
        print("Product %s not found!" % expr)


def exit_save_all():
    with open(FILE, "w") as f:
        writer = csv.writer(f, delimiter=", ")
        writer.writerow(products[0].keys())

        for product in products:
            csv.DictWriter(f, product.values(), delimiter=", ")
            writer.writerow(product.values())
    exit(0)


def show_menu():
    print()
    template = "\t\t{}): {}.\n"
    message = "delivery program menu\n".capitalize()
    for k, v in MENU.items():
        message += template.format(k, v.capitalize())  # foreach item in menu

    ans = input(message).strip()
    return ans


def print_bill(bill_):
    if bill_ == []:
        return

    MAX_CHAR = max((len(product[1]) for product in bill_))

    print(
        f"--{'-'*MAX_CHAR}--" * 4,
    )
    for p in products[-1].keys():
        print(f"| {p.center(MAX_CHAR)} ", end="")
    print("|")
    print(f"__{'_'*MAX_CHAR}__" * 4, end="")
    for b in bill_:
        for i, v in enumerate(b):
            print(f"| {str(v).center(MAX_CHAR)} ", end="")

        print("|")

    print(f"__{'_'*MAX_CHAR}__" * 4)

    total = sum(int(b[2]) * b[3] for b in bill_)
    print("The total amount {}".format(total))


def punches_product():
    done = False
    customer_bill = list()

    while not done:
        k_word = input("Type a keyword to find the product. ")
        P_id = search_products(k_word)
        if P_id is None:
            break
        product_id = int(P_id) - 1

        amount = int(products[product_id]["amount"])
        c_amount = int(input("Total amount is %s\t you should'nt take more. " % amount))
        if c_amount > amount:
            print("Amount is not possible!")
            continue
        amount -= c_amount  # decreasing amount
        products[product_id]["amount"] = amount

        price = products[product_id]["price"]
        name = products[product_id]["name"]
        customer_bill.append((P_id, name, price, c_amount))

        done = bool(input("Done yet?\t|Please type anything!"))

    return customer_bill


def main():
    user_choice = show_menu()

    # execute command based on user input
    if user_choice.upper() not in MENU.keys():
        return
    if user_choice.upper() == "A":  # adding functionality
        add_product()
    elif user_choice.upper() == "B":  # removing functionality
        del_product()
    elif user_choice.upper() == "C":  # updating functionality
        edit_product()
    elif user_choice.upper() == "D":  # monetizing functionality
        cus_bill = punches_product()
        print_bill(cus_bill)
    elif user_choice.upper() == "E":  # retrieving functionality
        show_products()
    elif user_choice.upper() == "F":  # searching functionality
        k_word = input("Type a keyword please?")
        search_products(k_word)
    elif user_choice.upper() == "G":  # terminating functionality
        exit_save_all()
    else:
        pass
        # f = open(HELP)
        # print(f.read().split("\n"))
        # f.close()


# Welcome! This program executes here
print("Welcome to the delivery ordering programme")
products = []  # List of products needed to read from database
with open(FILE, "r") as f:
    # NOTE: This uses file database
    f.readline()  # skip header line
    lines = f.readlines()
    for line in lines:
        product = dict(id="000", name="name", price="price", amount="amount")
        property_ = line.split(", ")
        product["id"] = property_[0]
        product["name"] = property_[1]
        product["price"] = property_[2]
        product["amount"] = property_[3][:-1]
        products.append(product)

import pdb


pdb.set_trace()
while True:
    main()
