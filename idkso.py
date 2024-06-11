# Python Program prepared by Adam Yassine

# Global function for all functions in this program
import csv

filedict = {}
filelist = []

def readCSV(file):

    # create an empty dictionary and an empty list

    # create a try and except to determine ...
    try:
        sheet1 = open(file, 'r', encoding='utf-8')
        next(sheet1)

        for col in sheet1:
            col = col.strip('\n').split(',')
            if file == 'TopUni.csv':
                filedict = {'World Rank': row[0], 'Institution Name': row[1], 'Country': row[2].upper(), 'National Rank': row[3], 'Score': row[8]}
            elif file == 'capitals.csv':
                filedict = {'Country Name': row[0].upper(), 'Capital': row[1].upper(), 'Continent': row[5].upper()}
            filelist.append(filedict)
        sheet1.close()
        print(filelist)
        return filelist
    except FileNotFoundError as exception:
        return exception

    print(filelist)
# Function 1: Universities count

file = open('TopUni.csv', 'r')
count = -1
uniCount = len(filelist)




# _______________________________________________________________________________

# Function 2: Available Countries

"""sheet2 = open('TopUni.csv', 'r')
line2 = csv.DictReader(sheet2)
count2 = 0
countries = []

for i in line2:
    count2 += 1
    countries.append(i['Country'])

# convert all country names into upper case
countries_upper = [countries.upper() for countries in countries]

# Make a dictionary with only the keys inside
countries_dictionary = dict.fromkeys(countries_upper)

# Convert the dictionary into a list
countriesNew = (list(countries_dictionary.keys()))

new_list = [item.replace("'", '') for item in countriesNew]
new_list = ', '.join(str(x) for x in countriesNew)

func1list = ('Available Countries =>', new_list)
f = open("output.txt", "a")
f.write(str(func1list))
f.close()

f = open('output.txt', 'r')
f.write('\nAvailable Countries =>' + new_list)
f.close()"""


# ________________________________________________________________________

# Function 3: Available Continents


def continents(sheet3):
    continents = []
    del new_list[0]
    for elements in new_list:
        sheet3 = open('capitals.csv', 'r', encoding='utf8')
        for line in sheet3:
            line3 = line.split(',')
            if row[0].upper == elements:
                continents = (row[5].strip().upper())
                return continents
    print(continents)

count3 = 0
continents = []

sheet3 = open('TopUni.csv', 'r')
line2 = csv.DictReader(sheet2)

for i in line2:
    count3 += 1
    continents.append(i['Continent'])


continents_upper = [continents.upper() for continents in continents]

continents_dictionary = dict.fromkeys(continents_upper)

continentsNew = (list(continents_dictionary.keys()))


continentsList = ', '.join(str(x) for x in continentsNew)

print('Available Continents =>', continentsList)

# _____________________________________________________________________________

# Function 4: The university with top international rank

sheet3 = open('TopUni.csv', 'r')

print()
choice = input(str('Choose a Country: '))

done = False
while not done:
    choice = input(str('Choose a Country: '))
    if choice.upper() == countries_dictionary:
        done = True
    elif choice.upper() in countries_dictionary:
        print(countries_dictionary)
    else:
        print('Country not in list. Select a valid country')

reader = csv.reader(sheet3)

new_Country_dict = {}

with open('TopUni.csv', 'r') as data_file:
    data_file.__next__()
    for row in data_file:
        row = row.strip().split(',')
        new_Country_dict.setdefault(row[2].upper(), {})[int(row[0])] = row[1]
rank = min(new_Country_dict[choice.upper()].keys())
funct4Output = ('At International rank =>', rank, 'The University Name is =>', new_Country_dict[choice.upper()][rank])


# _____________________________________________________________________________

# Function 5: The university with top national rank




# Function 6: The average score

sheet5 = open('TopUni.csv')
reader3 = csv.reader(sheet5)
numCountries = 0.0
totalAverage = 0.0

for row in reader3:
    if row[2] == choice.upper() or choice.lower():
        totalAverage += float(row[8])
        numCountries += 1

averageScore = totalAverage/numCountries
print(averageScore)


# Function 7: The continent relative score



# Function 8: The capital city

line7 = open('Capitals.csv', 'r')
reader3 = csv.reader(line7)

for row in reader3:
    if row[0] == choice.upper():
        print('the Capital is =>', row[1].upper())

# Function 9: The universities that hold the capital name



