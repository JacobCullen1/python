# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 10:43:58 2024

@author: Jacob
Topic: while cycle with list and dictionary
"""

#Task 1 Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing. 
# Mahsulotlar nomini birma-bir qabul qilib, yangi ro'yxatga joylang

# buyurtmalar = []
# print("Buyurtmalar ro'yhatini tuzamiz!")
# n=1
# while True:
#     savol = f"{n}- mahsulot nomini kiriting >>> "
#     mahsulot = input(savol)
#     buyurtmalar.append(mahsulot)
#     javob = input("Yana mahsulot qo'shasizmi? ha / yo'q >>> ")
#     if javob == 'ha':
#         n+=1
#         continue
#     else:
#         break

# print("Mahsulotlar ro'yhati:")
# for mahsulot in buyurtmalar:
#     print(mahsulot.title())    

# Done
    

# Task 2
# e-bozor uchun mahsulotlar va ularning narhlari lug'atini shakllantiruvchi dastur yozing. 
# Foydalanuvchidan lug'atga bir nechta elementlar (mahsulot va uning narhi) kiritishni so'rang

# bozor = {}
# flag = True
# while flag:
#     mahsulot = input("Mahsulot nomini kiriting >>> ")
#     narh = input(f"{mahsulot}ning narhini kiriting >>> ")
#     bozor[mahsulot] = int(narh)
    
#     javob = input("Yana mahsulot qo'shasizmi? ha / yo'q >>> ")
#     if javob =="yo'q":
#         flag = False

# for mahsulot, narh in bozor.items():
#     print(f"{mahsulot.title()}ning narhi {narh} so'm")
    
# Done    

# Task 3
# Yuqoridagi ikki dasturni jamlaymiz. Foydalanuvchi buyurtmasi ro'yxatidagi har bir 
# mahsulotni e-bozordagi mahsulotlar bilan solishitiring (tayyor ro'yxat ishlatishingiz mumkin). 
# Agar mahsuot e-bozorda mavjud bo'lsa mahuslot narhini chiqaring, aks holda 
# "Bizda bu mahsulot yo'q" degan xabarni kor'sating.

# mahsulotlar = {'olma': 20000,
#                'shaftoli': 25000,
#                'tarvuz': 18000,
#                'uzum': 22000,
#                'qovun': 15000,
#                'sok': 7000}

# buyurtmalar = []
# while True:
#     buyurtma = input("Mahsulot nomini kiriting >>> ")
#     if buyurtma in mahsulotlar:
#         buyurtmalar.append(buyurtma)
#         narh = mahsulotlar[buyurtma]
#         print(f"{buyurtma.title()} - {narh} so'm")
#     else:
#         print(f"Bizda '{buyurtma}' yo'q")
        
#     javob = input("Yana mahsulot buyurtma qilasizmi? ha/yo'q > ")
#     if javob.lower() != 'ha':
#         break

# if buyurtmalar:
#     print("Sizning buyurtmalaringiz:")
#     sorted_buyurtmalar = sorted(buyurtmalar)
#     total_price = 0
#     for mahsulot in sorted_buyurtmalar:
#         narh = mahsulotlar[mahsulot]
#         print(f"{mahsulot.title()} - {narh} so'm")
#         total_price += narh
#     print(f"Umumiy narxi: {total_price} so'm")
# else:
#     print("Siz hali hech qanday mahsulot buyurtma qilmagansiz.") 












