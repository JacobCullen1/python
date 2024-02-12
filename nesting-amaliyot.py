#Task 1
# Adabiyot (ilm-fan, san'at, internet) olamidagi 4 ta mashxur shaxlar haqidagi 
# ma'lumotlarni lug'at ko'rinishida saqlang. Lug'atlarni bitta ro'yxatga joylang, 
# va har bir shaxs haqidagi ma'lumotni konsolga chiqaring.

buxoriy = {'ism':'Abu Abdulloh Muhammad ibn Ismoil',
            'tyil':810,
            'vyil':870,
            'tjoy':'Buxoro',
            'asarlar':['algebra tilsimlari', 'xadislar']
            }

qodiriy = {'ism':'Abdulla Qodiriy',
            'tyil':1894,
            'vyil':1938,
            'tjoy':'Toshkent',
            'asarlar':["sherlar to'plami", "maqolalar"]
            }

vohidov = {'ism':'Erkin Vohidov',
            'tyil':1936,
            'vyil':2016,
            'tjoy':"Farg'ona",
            'asarlar':["baxor", "gulshan", "qish"]
            }

navoiy = {'ism':'Alisher Navoiy',
            'tyil':1441,
            'vyil':1501,
            'tjoy':"Xirot",
            'asarlar':["hamsa", "chaman", "baxtli tun"]
            }

shaxslar = [buxoriy, qodiriy, vohidov, navoiy]


for shaxs in shaxslar:
    ism = shaxs['ism']
    asarlar = shaxs['asarlar']
    print(f"\nIsmi - {shaxs['ism']}, "
          f"Tug'ilgan yili - {shaxs['tyil']}, "
          f"Vafot etgan yili - {shaxs['vyil']}, "
          f"Tug'ilgan joyi - {shaxs['tjoy']},"
          f"\n{ism} ning mashxur asarlari: ")
    for asar in asarlar:
              print(asar.title())
