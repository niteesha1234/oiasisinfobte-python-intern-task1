while True:
    
    print("BMI calculator")
    
    try:
        weight=int(input("enter your weight in kg"))
    
    except ValueError:
        print("Please!! Enter  correct weight")
        continue
    
    try:
        height=int(input("enter your height in cm"))
    
    except ValueError:
        print("PLEASE!!Enter correct height")
        continue
    
    bmi=weight/(height/100)**2
    print(f"your BMI is : {bmi: .2f}")
    
    if bmi>0 and bmi<18.5:
        print("you are UnerdWeight")
    
    elif bmi>=18.5 and bmi<24.9:
        print("you are Normal")
    
    elif bmi>=25.0 and bmi<=29.9:
        print("you are OverWeight")
    
    elif bmi>=30.0:
        print("you are Obese")
    
    else:
        print("enter the correct details")
    
    x=input("do you want to calculate one more BMI?Type(yes/no):").lower()
    if x!="yes" and x!="y":
        print("bye")
        break
    