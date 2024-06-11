
output = {}
odd, even, three = set(), set(), set()

for nums in range(1, 20):
    if nums % 2 == 1:
        odd.add(nums)

    if nums % 2 == 0:
        even.add(nums)

    if nums % 3 == 0 and nums != 0:
        three.add(nums)

output['even'] = even
output['odd'] = odd
output['three'] = three

for element in output:
    print(element, ':', output[element])


print()

sentence = "I had such a horrible day it was awful so bad sign it could not have been worse but actually thoough it was such a terrible horrible bad day"
makeItHappy = {'horrible':"amazing",'bad':'good','awful':'awesome','worse':'better','terrible':'great'}
spsentence = sentence.split()

for word in range(0,len(spsentence)):
    if spsentence[word] in makeItHappy:
        spsentence[word] = makeItHappy[spsentence[word]]

newString = ""
for word in spsentence:
    newString = newString + word + " "
print(newString)


f = open('rawdata.txt', 'r')
incomeDict = {}
countryDict = {}
countryList = []
incomeList = []
initialList = []

for line in f:
    line = line.upper().strip('\n').split(':')
    initialList.append(line[1][0])
    countryList.append(line[1])
    incomeList.append(line[2])

for i in range(0, len(countryList)):
    incomeDict[countryList[i]] = incomeList[i]
    if initialList[i] in countryDict:
        countryDict[initialList[i]].add(countryList[i])
    else:
        countryDict[initialList[i]] = {countryList[i]}

done = False
while not done:
    text = input('enter an initial or a country name:')
    text = text.upper()
    if text == 'QUIT':
        done = True
    elif text in countryDict:
        print(countryDict[text])
    elif text in incomeDict:
        print(incomeDict[text])
    else:
        print('does not exist')





