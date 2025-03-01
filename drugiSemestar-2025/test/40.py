# 40

# numerickaTabla = ((1, 2, 3),
#                   (4, 5, 6),
#                   (7, 8, 9),
#                   ("*", 0, "#")
# )

numerickaTabla = ((1, 2, 3), (4, 5, 6), (7, 8, 9), ("*", 0, "#"))

for red in numerickaTabla:
    for broj in red:
        print(broj, end=" ")
    print()
