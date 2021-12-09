def Change(user_amount:float, price:float):  
    Cash = {}
    The_list = [100, 50, 20, 10, 5, 2, 1, 0.5 ,0.2 ,0.1 , 0.05, 0.02, 0.01]
    Refound = user_amount - price
    change = round(float(Refound),3)

    if price > user_amount:
        print (f"Customer have to pay {price - user_amount}$ more")

    else:
        print (f"Balance due: {change} $")
        for item in The_list:
            calculate = (change//item)
            Cash[item] = calculate
            change = round((change%item),2)

        result = {key:value for key,value in Cash.items() if value > 0}
        print("Denomination --> Quantity")
        for key,value in result.items():
            final_result = (str(key)+'$ --> '+str(value)).center(30, " ")
            print(final_result)
        
## change(input amout received from the customer, input price)
Change(2000,139.99)

