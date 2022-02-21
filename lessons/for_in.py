"""An example of for in syntax."""

names: list[str] = ["Dila", "Angel", "Kinza", "Ceren"]

i: int = 0  # while loop
while i < len(names):
    name: str = names[i]
    print(name)
    i += 1

for name in names:  # for...in loop
    print(name)