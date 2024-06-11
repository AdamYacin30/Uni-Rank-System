
def readCSV(file):
    fileDict = {}
    fileList = []
    try:  # making sure file opens with no erros
        file1 = open(file, "r", encoding="utf-8")
        next(file1)  # skipping over first line of data in csv

        for line in file1:
            line = line.strip("\n").split(",")  # str
            if file == "TopUni.csv":
                fileDict = {"World Rank": line[0], "Institution Name": line[1], "Country": line[2].upper(),
                            "National Rank": line[3], "Score": line[8]}
            elif file == "capitals.csv":
                fileDict = {"Country Name": line[0].upper(), "Capital": line[1].upper(), "Continent": line[5].upper()}
            fileList.append(fileDict)
        file1.close()
        return fileList
    except FileNotFoundError as exception:
        return exception


def UniCount(list):
    uniTotal = len(list)
    func1 = f"Total number of universities => {uniTotal}"
    WriteToFile(func1)
    return


def AvailableCountriesCount(list):
    Countrylist = []

    for i in list:
        if i["Country"] in Countrylist:
            pass
        else:
            Countrylist.append(i["Country"])

    formattedstring = ", ".join(Countrylist)
    text = f"Available countries => {formattedstring}"
    WriteToFile(text)
    return


def AvailableContinents(capslist):
    continentslist = []
    for i in capslist:

        if i["Continent"] in continentslist:
            pass
        else:
            continentslist.append(i["Continent"])
            formattedstring = ", ".join(continentslist)
    text = f"Available continents => {formattedstring}"
    WriteToFile(text)
    return


def TopRankInternational(list, country):
    toprankinternational = []
    for i in list:
        if i["Country"] == country:
            toprankinternational.append((i["Institution Name"], i["World Rank"]))

    func5= f"At international rank => {toprankinternational[0][1]} the university name is => {toprankinternational[0][0]}"
    WriteToFile(func5)
    return


def TopRanknational(list, country):
    """
    Find top ranking national university. Data input = country name and uni list
    """

    # topranknational = []

    # for i in list:
    #     if i["Country"].upper() == country.upper():
    #         topranknational.append(i["Institution Name"]) #made it append 2 seperate items  instead of one tuple with 2 items
    #         topranknational.append(i["National Rank"])
    #
    # text = f"At national rank => {topranknational[1]} the university name is => {topranknational[0]}"
    # topranknational = []
    # for i in list:
    #     if i["Country"] == country:
    #         topranknational.append((i["Institution Name"], i["National Rank"]))

    topranknational = []
    for i in range(len(list)):
        if list[i]["Country"] == country and list[i]["National Rank"] == "1":
            topranknational.append((list[i]["Institution Name"].upper(), list[i]["National Rank"]))
        # else:
        #     pass

    text = f"At national rank => {topranknational[0][1]} the university name is => {topranknational[0][0]}"
    WriteToFile(text)
    return


def CountryAverageScore(country, list):
    """
    Find average score of universites in selected country
    """
    countryscores = []
    totalscore = 0
    for i in list:
        if i["Country"].upper() == country.upper():
            # listpercountry.append((list[i]["Country"], list[i]["Institution Name"], list[i]["National Rank"],list[i]["World Rank"] ))
            countryscores.append(float(i["Score"]))
            # for k in range (len(countryscore):
            totalscore += float(i["Score"])
        else:
            pass
    global avgnationalscore
    avgnationalscore = totalscore / len(countryscores)
    text = f"The average score => {avgnationalscore:0.2f}"
    WriteToFile(text)
    return


def ContinentRelativeScore(country, capslist, unilist):
    """
    Find average score of universites in selected country
    """
    # avgScore = CountryAverageScore(country,list)
    # find all the countries in the same continent
    for line in capslist:
        if line["Country Name"] == country:
            continent = line["Continent"]

    # Get all the unis in the continent using country list from above and get the highest score
    CountriesInContinent = []
    for i in capslist:
        if i["Continent"] == continent:
            CountriesInContinent.append(i["Country Name"])

    # Find the highest university ranking out of all these countries
    highestscore = 0
    for country in CountriesInContinent:
        for j in unilist:
            if j["Country"] == country and float(j["Score"]) > highestscore:
                highestscore = float(j["Score"])

    # Do the calcualtion
    relativeScore = (float(avgnationalscore) / highestscore) * 100
    func = f"The relative score to the top university in {continent} is => ({avgnationalscore}/{highestscore}) x 100% = {relativeScore:0.2f}%"
    WriteToFile(text)
    return


def CapitalCity(country, capslist):

    global capital
    for i in capslist:
        if i["Country Name"] == country:
            capital = i["Capital"]
    text = f"The capital is => {capital}"
    WriteToFile(text)
    return


def UnisWithCapitalName(unilist):

    # Using capital name go through Institution names in unidata and if capital is in institution name append it empty capunilist

    capunilist = []
    number = 0
    for i in unilist:
        if capital.upper() in i["Institution Name"].upper():
            number = number + 1
            capunilist.append("#" + f"{str(number)}" + " " + i["Institution Name"])
    # if capunilist == []:
    #    pass
    # else:
    formattedtext = "\n ".join(capitalunivlist)
    # formattedtext = *capunilist, sep = "\n"
    print("The universities that contain the capital name =>\n", (formattedtext))
    #WriteToFile(text)
    return


def WriteToFile(text):

    with open("output.txt", "a") as f:
        f.write(f"{text} \n")


def getInformation(country, TopUni, capitals):
    country = country.upper()
    unidata = readCSV(TopUni)
    capsdata = readCSV(capitals)
    # test 1
    UniCount(unidata)
    # test 2
    AvailableCountriesCount(unidata)
    # #test 3
    AvailableContinents(capsdata)
    # #test 4
    TopRankInternational(unidata, country)
    # #test 5
    TopRanknational(unidata, country)
    # #test 6
    CountryAverageScore(country, unidata)
    # #test 7
    ContinentRelativeScore(country, capsdata, unidata)
    # #test 8
    CapitalCity(country, capsdata)
    # #test 9
    UnisWithCapitalName(unidata)


getInformation("usa", "TopUni.csv", "capitals.csv")

# if __name__ == "__main__":
#     unidata = readCSV('TopUni.csv')
#     capsdata = readCSV('capitals.csv')
#     country = "USA"
#     getInformation(country, unidata,capsdata )
univRanking.py
