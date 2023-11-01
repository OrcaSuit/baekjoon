inputString = input()
splitByMinus = inputString.split('-')
result = sum(map(int, splitByMinus[0].split('+')))

for subString in splitByMinus[1:]:

    sumOfSubstring = sum(map(int, subString.split('+')))

    result -= sumOfSubstring

print(result)

