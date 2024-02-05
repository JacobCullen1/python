# print("Task 1 student list")

# students = ["Ali", "Vali", "Kozim", "Sobir", "Jobir"]
# for student in students:
#     print(f"Dear {student}, you have to bring your passport for registration")
#     print("Jacob Cullen")

# print(f'Kod {len(students)} marta takrorlandi')


# print("Task 2 Sonlarning ro'yhati va kubi")
# print("10dan 100gacha bo'lgan toq sonlarning kubi")
# numbers = list(range(11,100,2))
# for n in numbers:
#     print(f"{n} sonining kubi {n**3} ga teng")


# print("Task 3 | Adjectives")
# adjectives = []
# print("Name 5 favorite adjectives")
# for n in range(5):
#     adjectives.append(input(f"{n+1} - adjective > "))
# print(adjectives)


 # print("Task 4 | people I met today")
# people = []
# print("How many people did you meet today?")
# quantity = str(input())
# for n in range(int(quantity)):
#     people.append(input(f"{n+1} name of a person >"))
# print(people)

print("Task 1 and task 4 together")

students = []
print("How many students are you writing letter to?")
quantity = str(input("Quantity of students > "))
for n in range(int(quantity)):
    students.append(input(f"{n+1}. Please, write student's name > "))

for student in students:
    print(f"# Dear {student} \n We are happy to tell you that you are enrolled as a student to our University")
    print("Admission team")
    
print(f"Message  has been sent successfully to {len(students)} students!")
print(students)