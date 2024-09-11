def calculate_total_purchase():
        # A customer in a store is purchasing five items. 
    Item1 = input(str("Enter 1st Item: "))
    Item2 = input(str("Enter 2nd Item: "))
    Item3 = input(str("Enter 3rd Item: "))
    Item4 = input(str("Enter 4th Item: "))
    Item5 = input(str("Enter 5th Item: "))

    PItem1 = 2
    PItem2 = 6.20
    PItem3 = 10
    PItem4 = 0.99
    PItem5 = 1.46

    print(PItem1, Item1)
    print(PItem2, Item2)
    print(PItem3, Item3)
    print(PItem4, Item4)
    print(PItem5, Item5)

    Item_total = float(PItem1 + PItem2 + PItem3 + PItem4 + PItem5)
    print("Total: ", Item_total)

    Sales_tax = (Item_total * (7 / 100))
    print("Tax: ", Sales_tax)

    # Write a program that asks for each item, 
    # then displays the subtotal of the sale, 
    # the amount of sales tax, and the total.  
    # Assume the sales tax is 7 percent.

calculate_total_purchase()

calculate_total_purchase()
