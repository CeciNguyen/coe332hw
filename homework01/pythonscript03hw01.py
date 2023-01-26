import names

def lengthofname():
    randonames = []
    i = 0

    while i < 5:
        nameid = names.get_full_name()
        length = len(nameid) - 1
        randonames.append(nameid)
        print(randonames[i], length)
        i += 1


lengthofname()
