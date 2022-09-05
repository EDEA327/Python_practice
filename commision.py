seller_name = input("What's your name?: ")
sales = float(input("Please tell me how much you sold?: "))
comission = round(sales * 0.13,2)
print(f"OK {seller_name} this month you will receive {comission}$")