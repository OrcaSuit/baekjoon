#10+20-30+40-50+60-70+80-90+100-110+120

inputString = input()
splitByMinus = inputString.split('-')
result = sum(map(int, splitByMinus[0].split('+')))

for subString in splitByMinus[1:]:

    sumOfSubstring = sum(map(int, subString.split('+')))

    result -= sumOfSubstring

print(result)

