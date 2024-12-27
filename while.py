password = "8904"

attempts = 0

y = 3

while attempts < y:
    user_password = input("Enter your password: ")
    if user_password == password:
        print("Login successful!")
        break
    else:
        attempts += 1
        if attempts < y:
            print("logged in....")
        else:
            print("Too many incorrect attempts. You are blocked.")

if attempts >= y:
   
    print("Access blocked due to too many incorrect attempts.")


  



   
 
