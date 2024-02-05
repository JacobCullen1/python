#Task 1
#Foydalanuvchidan juft son kiritishni so'rang. Agar foydalanuvchi juft son kiritsa "Rahmat!", 
#agar toq son kiritsa "Bu son juft emas" degan xabarni chiqaring.

# son = int(input("Juft son kiriting \n>>>"))
# if not son%2:
#     print("Rahmat")
# else:
#     print("Bu juft son emas!")

#Task 2
# Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini quyidagicha chiqaring:
# Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul
# Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm
# Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm

# print("Muzeyga hush kelibsiz!")
# yosh = int(input("Yoshingiz nechida? \n>>>"))
# if yosh<4 or yosh>60:
#     print("Sizga kirish bepul!")
# elif yosh<18:
#     print("Kirish narxi 10,000")
# elif yosh>18:
#     print('Kirish narxi 20,000')

#Task 3
# Foydalanuvchidan ikita son kiritishni so'rang, 
# sonlarni solishtiring va ularning teng yoki katta/kichikligi haqida xabarni chiqaring

# print("Sonlar ustida amallar bajarish")
# a = int(input("a uchun qiymat kiriting > "))
# b = int(input("b uchun qiymat kiriting > "))
# if a==b:
#     print('sonlar teng')
# elif a<b:
#     print('b a dan katta')
# else:
#     print("a b dan katta")


#Task 4
# mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting. 
# Yangi, savat degan bo'sh ro'yxat yarating va foydalanuvchidan savatga 
# kamida 5 ta mahsulot kiritishni so'rang. Savatdagi elementlarni, 
# mahsulotlar ro'yxati bilan solishtiring va qaysi biri ro'yxatda bo'lsa "Mahsulot do'konimizda bor" 
# aks holda, "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.

print("Do'konimizga xush kelibsiz, bugun nima xarid qilasiz?")
mahsulotlar = ['non', 'olma', 'sabzi', 'pomidor', 'shaftoli', 'karam', 'nok', 'mandarin', 'banan', 'tarvuz']
savat = []
for n in range(5):
    savat.append(input(f'Savatga {n+1}-mahsulotni kiriting > '))

for mahsulot in savat:
    if mahsulot in mahsulotlar:
        print(f"{mahsulot} do'konimizda bor")
    else:
        print(f"kechirasiz, {mahsulot} bizning do'konimizda yo'q")
        
        
# print("Do'konimizga xush kelibsiz")
# mahsulotlar = ['non', 'olma', 'sabzi', 'pomidor', 'shaftoli', 'karam', 'nok', 'mandarin', 'banan', 'tarvuz']
# savat = []
# for mahsulot in 













