name = input("Name:")
height =  float(input("Height:"))
weight = float(input("Weight:"))
bmi = weight/height*height

if bmi>0:
    if bmi<18.5:
      print(f"{name} you are underweight")
    elif bmi>=18.5 and bmi<25:
      print(f"{name} you are normal")
    elif bmi>=25 and bmi>30:
     print(f"{name} you are overweight")
else:
    print(f"{name} enter correct details")


