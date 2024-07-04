print("-="*12)
print("-=-=-Boas Vindas-=-=-=")
print("-="*12)

userName = input("Enter you name? ")
email = input("Enter you email ")
password = input(" you password")

print(f"Boas vindas {userName}")

# f= open("Name.txt","a")
print("[ 1 ] - login")
print("[ 2 ] - password")

operating = int(input("enter"))

if operating ==1:
    login = input("Enter you login ")
    passwordLogin = input("password")
    if login == userName and passwordLogin == password:
        print(userName)
        print("Continue")

    elif passwordLogin != password:
        print("Password not correct")
        passwordLogin = input("password")
        if passwordLogin == password:
            print("Continue")
            login = input("Enter you login ")
            if login == userName:
                print("Continue")

    elif login != userName:
        print("Login not correct")
        login = input("login")
        if passwordLogin == password:
            print("Continue")
            login = input("Enter you login ")
            if login == userName:
                print(userName)
                print("Continue")

elif operating == 2:
    passwordLogin = input("password")
    if passwordLogin == password:
        print("Continue")
        login = input("Enter you login ")
        if login == userName:
            print(userName)
            print("Continue")
