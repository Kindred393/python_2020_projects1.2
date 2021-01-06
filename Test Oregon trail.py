def shop (money, food, ammo, clothes, parts, ox):
    bill = 0
    inventory = []
    items = ["Oxen", "Ammunition", "Wagon parts", "Check Out"]
    spent_on_items = [0.00, 0.00, 0.00, 0.00, 0.00, bill]
    print(" Before leaving Independance you should buy items")
    print(str.format("You have {} in cash to make the trip",money))
    print("remember you can buy supplies along the way")
    input("Press Enter to Continue")

    while True:
        spent_on_items[len(spent_on_items)-1] = bill
        print("Welcome to the General Store")
        print("Here is a list of things you can buy")
        for i in range (len(items)):
            print(str.format("{}.        {:20}     ${:.2f}",i+1,items[i],spent_on_items[i]))
        print(str.format("Total Bill so far:       ${:.2f}",bill))
        print(str.format("Total Funds available:       ${:.2f}",money-bill))
        choice = getNumber("What Item would you like to buy?")# make sure this is a call to your number function
        if choice == 1:
            Print("""
            There are 2 oxen in a toke;
            I recomend at least 3 yokes.
            I charge $40 a toke""")
            print(str.format("Total Bill so far:          ${:.2f",bill)
            answer = int(input("How many yoke do you want"))
            cost = amswer*40
            ox = answer*2
            bill += cost
            spent_on_items{0} = cost

        if choice == 5:
                  print("""
            It is a good idea to have a few
            Spare parts for your wagon on hand
            you never know what can happen on
            the trail and a broken down
            wagon can be a death sentance""")
            pars_bill = 0.00
            parts = ["Wagon Wheel", "Wagon axle", "Wagon Tongue"]
                  parts_cost =[10.00,20.00,50.00,parts_bill]
            while True:
                parts_cost[len(parts_cost)-1] = parts_bill
            print("Here is a list of things you can buy")
            for i in range(len(parts)):
                print(str.format("Total Bill so far:      ${:.2f}",bill))
            print(str.format("Total funds available   ${:.2f}",money))
            item = int(input("What Item would you like to buy"))
            if item == 1:
                answer = int(input("How many wagon Wheels do you want?"))
                for i in range(answer):
                    inventory.append("Wagon Wheel")
                parts_bill += parts_cost[0]*answer
            elif item == 2:
                answer = int(input("How many wagon Axles do you want?"))
                for i in range(answer):
                    inventory.append("Wagon Axle")
                parts_bill += parts_cost[1]*answer
            elif item == 3:
                answer = int(input("How many wagon Tongues do you want?"))
                for i in range(answer):
                    inventory.append("Wagon Tongue")
                parts_bill += parts_cost[2]*answer
            elif item == 4:
                bill += parts_bill
                spent_on_items[4] = parts_bill
                break
                
        
money = 1000
food = 0
ammo = 0
clothes = 0
parts = []
ox = 0
shop(money, food, ammo, clothes, parts, ox)
