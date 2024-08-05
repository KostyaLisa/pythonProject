from datetime import datetime

legal_age_count = 0
young = 0
for i in range(1, 8):
    yearUser = int(input('Enter year: '))
    datetimeNow = datetime.now()
    if datetimeNow.year - yearUser >= 18:
        legal_age_count += 1
    else:
        young += 1
print(legal_age_count)
print(young)
