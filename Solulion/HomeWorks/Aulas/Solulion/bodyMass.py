height = float(input("Enter your height: "))
weight = int(input("Enter your body weight: "))

BMI = weight / (height*height)
print("Calculating...")

print(f"Your BMI is {BMI:.2f}.")

if BMI < 18.5:
    print ("You are underweight.")

elif BMI >= 18.5 and BMI <= 24.9:
    print ("You are at your ideal weight.")

elif BMI >=25.0 and BMI < 29.9:
    print ("You are overweight.")

elif BMI >=30.0 and BMI <=34.9:
    print ("You have grade 1 obesity.")

elif BMI >= 35.0 and BMI <=39.9:
    print ("You have grade 2 obesity.")

elif BMI >=40:
    print ("You are morbidly obese.")