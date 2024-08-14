from datetime import datetime

legal_age_count = 0
young = 0
for i in range(1, 11):
    yearUser = int(input('Enter year: '))
#     datetimeNow = datetime.now()
#     if datetimeNow.year - yearUser >= 18:
#         legal_age_count += 1
#     else:
#         young += 1
# print(legal_age_count)
# print(young)

if i == 0:
    legal_age_count =yearUser
    young = yearUser
else:
    if yearUser > legal_age_count:
        legal_age_count= yearUser
    if yearUser < young:
        young= yearUser

print(legal_age_count)
print(young)