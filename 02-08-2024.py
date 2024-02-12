#Task 1

print("Salom ismingizni kiriting")
name = input(">>> ")
if name == name.lower():
    print("Salom", name.title())
else:
    print(f"Salom {name},")

books = []
print("Keling yoqtirgan kitoblaringiz ro'yhatini tuzamiz"\
      "\nEslatma! Chiqish uchun stop so'zini kiriting")
  
book = "Kitob nomini kiriting >>> "
flag = True
while flag:
    bname = input(book)
    if bname == 'stop':
        flag = False
        print(books)
    else:
        books.append(input(book))
    




















