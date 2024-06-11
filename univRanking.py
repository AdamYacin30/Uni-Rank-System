# Python Program for Universities Rankings prepared by Adam Yassine

# define function to Read both CSV files and create a list with dictionaries inside
def ReadCSVFile(file):
    dictionaryFile = {}
    listFile = []

    # create a try and except function to ensure file opens with no errors
    try:
        sheet1 = open(file, 'r', encoding='utf-8')
        # 'next' is used to skip over the first line of the csv file since there is unused info
        next(sheet1)
        for row in sheet1:

            row = row.strip('\n').split(',')
            # if file is called from 'TopUni.csv' create a dictionary with all 'USED' components in csv file
            if file == 'TopUni.csv':
                dictionaryFile = {'World Rank': row[0], 'Institution Name': row[1], 'Country': row[2].upper(), 'National Rank': row[3], 'Score': row[8]}
            # if file is called from 'Capitals.csv' create a dictionary with all 'USED' components in csv file
            elif file == 'capitals.csv':
                dictionaryFile = {'Country Name': row[0].upper(), 'Capital': row[1].upper(), 'Continent': row[5].upper()}
            # put the dictionary in a list
            listFile.append(dictionaryFile)
        sheet1.close()
        return listFile
    except FileNotFoundError as exception:
        return exception


# Function 1: Universities count
def UnivCount(listFile):
    # variable to give the length/amount of universities there are in the 'TopUni.csv file
    univTotal = len(listFile)

    # create a variable that prints out necessary output statement in order to be used in another function
    func = f'Total number of universities => {univTotal}'
    WriteToFile(func)
    return


# Function 2: Available Countries
def AvailableCountries(listFile):
    countries = []

# for loop to go through the list and find the country name in the dictionary with the key 'country'
    for row in listFile:
        if row['Country'] in countries:
            continue
        else:
            countries.append(row['Country'])

    # ', ' used to seperate the countries more neatly
    countriesNew = ', '.join(countries)
    func = f'Available countries => {countriesNew}'
    WriteToFile(func)
    return


# Function 3: Available Continents
def AvailableContinents(capitalsList):
    # create an empty list to hold all the continents
    continents = []
    for row in capitalsList:

        if row['Continent'] in continents:
            continue
        else:
            # if continent key is in the list add every item that has the key 'continent' with in the dictionary
            continents.append(row['Continent'])
            continentsNew = ', '.join(continents)
    Func = f'Available continents => {continentsNew}'
    WriteToFile(Func)
    return


# Function 4: The university with top international rank
def TopIntRank(list, countries):
    # create a new list that holds the university name and the world rank
    topInterRank = []

    for row in list:
        if row['Country'] in countries:
        # for loop and if statement used for every line that has 'country as the key, append the university name and its rank in the list
            topInterRank.append((row['Institution Name'], row['World Rank']))

    func = f'At international rank => {topInterRank[0][1]} the university name is => {topInterRank[0][0]}'
    WriteToFile(func)
    return


# Function 5: The university with top national rank
def TopNationalRank(list, country):
    topNationRank = []

# for loop to find country with the national rank consisting of '1'
    for row in range(len(list)):
        if list[row]['Country'] == country and list[row]['National Rank'] == '1':
            topNationRank.append((list[row]['Institution Name'].upper(), list[row]['National Rank']))


    func = f'At national rank => {topNationRank[0][1]} the university name is => {topNationRank[0][0]}'
    WriteToFile(func)
    return


# Function 6: The average score
def AverageScore(country, listFile):
    # create a list to hold all the scores in every university and create a variable with 0
    allCountryScores = []
    totalScore = 0

    for row in listFile:
        if row['Country'].upper() == country.upper():
            # if country name is in the csv list, add the university score into the allCountryScore list
            allCountryScores.append(float(row['Score']))
            totalScore += float(row['Score'])
        else:
            pass
    global averageNatScore
    averageNatScore = totalScore / len(allCountryScores)
    func = f'The average score => {averageNatScore}%'
    WriteToFile(func)
    return


# Function 7: The continent relative score
def RelativeScore(country, capitalList, list):
    # create a for loop to find all the countries that are in the same continent
    for line in capitalList:
        if line['Country Name'] == country:
            continent = line['Continent']

    # create a list all to hold all the university names in the continent
    CountriesInContinent = []
    for row in capitalList:
        if row['Continent'] == continent:
            CountriesInContinent.append(row['Country Name'])

    # create a nested loop to find the greatest ranked university out of all the countries
    greatestScore = 0
    for country in CountriesInContinent:
        for col in list:
            if col['Country'] == country and float(col['Score']) > greatestScore:
                greatestScore = float(col['Score'])

    # compute calculation for relative score by dividing the average national score by the greatest score and multiply it by 100
    relativeScore = (float(averageNatScore) / greatestScore) * 100
    func = f'The relative score to the top university in {continent} is => ({averageNatScore}/{greatestScore}) x 100% = {relativeScore:0.2f}%'
    WriteToFile(func)
    return


# Function 8: The capital city
def CapitalCity(country, capitalList):

    # create a global variable for the variable 'capital'
    global capital
    for row in capitalList:
        # if statement created to output the capital city that corresponds to the country
        if row['Country Name'] == country:
            capital = row['Capital']
    func = f'The capital is => {capital}'
    WriteToFile(func)
    return


# Function 9: The universities that hold the capital name
def CapitalNames(listFile):
    # Using the capital city names to check which university in the list corresponds
    capitalUnivList = []
    counter = 0
    for row in listFile:
        if capital.upper() in row['Institution Name'].upper():
            counter += 1
            capitalUnivList.append('#' + f'{str(counter)}' + ' ' + row['Institution Name'])

    capitalUnivList = '\n '.join(capitalUnivList)
    func = f'The universities that contain the capital name =>\n {capitalUnivList}'
    WriteToFile(func)
    return


# Function created to open and write to text file output.txt
def WriteToFile(func):
    with open('output.txt', 'a') as f:
        f.write(f'{func} \n')


# create a define function to get all the information from all the functions above in steps 1-9
def getInformation(country, TopUni, capitals):
    country = country.upper()
    listFile = ReadCSVFile(TopUni)
    capitalList = ReadCSVFile(capitals)

# function 1
    UnivCount(listFile)
# function 2
    AvailableCountries(listFile)
# function 3
    AvailableContinents(capitalList)
# function 4
    TopIntRank(listFile, country)
# function 5
    TopNationalRank(listFile, country)
# function 6
    AverageScore(country, listFile)
# function 7
    RelativeScore(country, capitalList, listFile)
# function 8
    CapitalCity(country, capitalList)
# function 9
    CapitalNames(listFile)

