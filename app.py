number = (2,2,4,6,3,4,6,1)
uniques = []
for number in number:
    if number not in uniques:
        uniques.append(number)
print(uniques)