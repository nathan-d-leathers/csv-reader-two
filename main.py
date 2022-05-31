animal = input("insert an animal: ")
if animal[-1] != "s":
    animal = animal + "s"
try:
    with open(f"data/{animal}.csv") as animals:
        for x in animals.readlines()[1:]:
            line = x.strip().split(", ")
            print(f"{line[0].capitalize()} is a {line[1]} year old {line[2].title()} available for adoption.")


except Exception:
    print(f"{animal} are not available for adoption")

# adding notes to git

# Code Platoon Solution:
# import csv
# animal_type = input("cats or dogs?\n")

# try:

#     data = open(f'./data/{animal_type}.csv')
#     reader = csv.DictReader(data)

#     for row in reader:
#         print(f"{row['name']} is a {row['age']} year old {row['breed']}.")
# except:
#     print(f"Sorry, we don't have any {animal_type} here.")
