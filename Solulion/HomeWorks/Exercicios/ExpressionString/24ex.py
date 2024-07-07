speed= int(input("Your speed "))

if speed < 80:
    print(f"Good {speed}")

elif speed > 80 or speed == 80:
   result = ((speed-80)*7)+100
   print(f"you have payment {result}")