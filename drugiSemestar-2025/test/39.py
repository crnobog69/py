# 39

voce = ["јабука", "кокос", "поморанџа", "шљива"]
povrce = ["купус", "целер", "парадајз"]
mesa = ["кокошка", "риба", "свиња"]

# namirnice = [
#     ["јабука", "кокос", "поморанџа", "шљива"],
#     ["купус", "целер", "парадајз"],
#     ["кокошка", "риба", "свиња"],
# ]

namirnice = [voce, povrce, mesa]

# voce[0] = "ананас"

print(namirnice[0])  # voce
print(namirnice[1])  # povrce
print(namirnice[2])  # mesa

print()

print(namirnice[0][0])  # `јабука`

print()

for namirnica in namirnice:
    print(namirnica)
    print()

for kolekcija in namirnice:
    for hrana in kolekcija:
        print(hrana, end=" ")
    print()
