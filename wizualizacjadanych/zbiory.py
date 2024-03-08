panstwa = {"Polska", "Stany Zjednoczone", "Niemcy", "Francja", "Włochy"}
print(panstwa)

panstwa.add("Polska")
print(panstwa)

print("Polska" in panstwa)

panstwa.remove("Francja")
print(panstwa)

panstwa1 = {"Polska", "Stany Zjednoczone", "Niemcy", "Francja", "Włochy"}
panstwa2 = {"Polska", "Wielka Brytania", "Portugalia", "Kanada", "Włochy"}
panstwa3 = {"Polska", "Włochy"}
print(panstwa1 | panstwa2)
print(panstwa1 & panstwa2)
print(panstwa1 - panstwa2)
print(panstwa3.issubset(panstwa1))
