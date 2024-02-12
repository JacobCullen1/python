#favorite movies
# friends = []
# for m in range(3):
#     friends.append(input(f"{m+1} - Ismingizni kiriting >>>").title())
# print(friends)
# print("3 ta sevimli kinoyingiz nomini kiriting >>>")
# kinolar = []
# for n in range(3):
#     kinolar.append(input(f"{n+1} - kino nomini kiriting >>>"))  
# print(kinolar)






# Davlatlar degan lug'at yarating, lug'at ichida bir nechta davlatlar haqida 
# ma'lumotlarni lug'at ko'rinishida saqlang. Har bir davlat haqida ma'lumotni konsolga chiqaring.

davlatlar = {
    "o'zbekiston":{'poytaxt':'toshkent',
                   'maydon':438000,
                   'axoli':35,
                   'taom':['manti', 'osh', 'mastava']},
    "turkiya":{'poytaxt':'anqara',
               'maydon':500978,
               'axoli':75,
               'taom':['qaxva', 'baklava', 'kofte']},
    "qozog\'iston":{'poytaxt':'ostana',
                   'maydon':279000,
                   'axoli':15,
                   'taom':['beshbarmoq', 'osh', 'shubat']},
    "qirg'iziston":{'poytaxt':'dushanbe',
                    'maydon':84000,
                    'axoli':12,
                    'taom':['beshbarmoq', 'qimiz', 'gulchaltay']},
    "amerika":{'poytaxt':'vashington',
           'maydon':950000,
           'axoli':150,
           'taom':['burger', 'pitsa', 'apple pie']}
    }
davlat = input('Davlat nomini kiriting >').lower()
if davlat in davlatlar:
    info = davlatlar[davlat]
    print(f"\n>>> {davlat.title()} \n"
          f"Poytaxti: {info['poytaxt'].title()} \n"
          f"Maydoni: {info['maydon']} kv/km \n"
          f"Axoli soni: {info['axoli']} mln \n"
          f"Mashxur taomlari:")
    for taom in info['taom']:
        print(taom.title(), end=", ")
else:
    print("Kechirasiz, bu davlat xaqida bizda ma'lumot yo'q")


# for davlat, info in davlatlar.items():
     # print(f"\n>>> {davlat.title()} \n"
    #       f"Poytaxti: {info['poytaxt'].title()} \n"
    #       f"Maydoni: {info['maydon']} kv/km \n"
    #       f"Axoli soni: {info['axoli']} mln \n"
    #       f"Mashxur taomlari:")
    # for taom in info['taom']:
    #     print(taom.title(), end=",")
    
    
    
    
    
    
    






















