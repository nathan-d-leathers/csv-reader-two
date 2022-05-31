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
