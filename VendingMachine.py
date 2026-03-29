import time


def display_items(machine_items):
    print(f'{"Code":<5} {"Item":<15} Price($)')
    for code, (name, price) in machine_items.items():
        print(f"{code:<5} {name.title():<15} ${price:.2f}")


def is_available_item(machine_items, code):
    return code in machine_items


def buy_item(machine_items):
    code = input("Enter the item code you want to buy (e.g., C1): ").upper()


    if is_available_item(machine_items, code):
        name, price = machine_items[code]
        payment = float(input(f"Total is ${price:.2f}. Enter payment: "))


        if payment >= price:
            dispense_item(name)
            print(f"Here is your {name.title()}. Change: ${payment - price:.2f}")
        else:
            print("Insufficient payment.")
    else:
        print("This item code is not available.")


def dispense_item(item):
    print(f"Dispensing {item.title()}...")
    time.sleep(2)
    print(f"{item.title()} delivered. Enjoy!")


def main():
    machine_items = {
        "C1": ("mikmik", 1.25),
        "C2": ("lumpia", 2.50),
        "C3": ("tattoo", 2.50),
        "J1": ("rollercoaster", 5.75),
        "J2": ("RC", 10.50),
        "J3": ("Sprite", 10.50),
        "F1": ("Willkins", 5.50)
    }


    while True:
        print("-" * 30)
        print("1. Show Items")
        print("2. Buy Item")
        print("3. Exit")
        choice = input("Choose an option (1/2/3): ")
        print("-" * 30)


        if choice == "1":
            display_items(machine_items)
        elif choice == "2":
            buy_item(machine_items)
        elif choice == "3":
            print("Thanks for using the vending machine.")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
