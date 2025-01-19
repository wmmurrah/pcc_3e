# oridinal_numbers.py

numeral_list = range(1,10)

positions = []
for numeral in numeral_list:
    if numeral == 1:
        positions.append(str(numeral)+"st")
    elif numeral == 2:
        positions.append(str(numeral)+"nd")
    elif numeral == 3:
        positions.append(str(numeral)+"rd")
    else:
        positions.append(str(numeral)+"th")
for position in positions:
    print(position)
