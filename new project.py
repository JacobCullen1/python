# foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing. 
# Foydalanuvchidan yangi login tanlashni so'rang va foydalanuvchi kiritgan 
# loginni foydalanuvchilar degan ro'yxatning tarkibi bilan solishtiring. 
# Agar ro'yxatda bunday login mavjud bo'lsa, "Login band, yangi login tanlang!" 
# aks holda "Xush kelibsiz, foydalanuvchi!" xabarini chiqaring.

    
users = ['admin', 'jacob', 'james', 'john', 'julie']

while True:
    login = input("Login tanlang >>> ")

    if login in users:
        print("Login allaqachon band, yangi login tanlang!")
    else:
        print(f"Xush kelibsiz, {login}")
        break  