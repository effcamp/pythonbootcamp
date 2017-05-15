

tmp = [1, "Ace", "Ace"]
ace = 0
if "Ace" in tmp:
    for card in tmp:
        if card == "Ace":
            inp = int(input("1 or 11: "))
            if inp == 1:
                ace += inp
            elif inp == 11:
                ace += inp
            else:
                pass

print(ace)
