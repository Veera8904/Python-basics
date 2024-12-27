#2 friend are going out to eat, in total they have money, they enter a restaurent and get a menu in theform of a list (just the prices) called menu * we have to output the combination of 2 items that make the friends use up all the money

x = 180 

menu = [10,20,40,80,100,140,200]

def combination(x, menu):
    for i in range(len(menu)):
        for j in range(i + 1, len(menu)):
            if menu[i] + menu[j] == x:
                return (menu[i], menu[j])
    return None

x = 180
menu = [10, 20, 40, 80, 100, 140, 200]

result = combination(x, menu)

if result:
    print(f"The two items that add up to {x} are: {result}")
else:
    print(f"No combination of two items adds up to {x}")
