dataWords = input("Enter a word or data : ")

enterUser = ''.join(dataWords.split()).lower()

enterUser=enterUser[:,:,-1]

if enterUser(dataWords):
    print("good")
else:
    print("bad")
