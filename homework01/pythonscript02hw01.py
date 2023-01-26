import names

randonames = []
i = 0

while i < 5:
    nameid = names.get_first_name()
    if (len(nameid) == 8):
        randonames.append(nameid)
        print(randonames[i])
        i += 1
