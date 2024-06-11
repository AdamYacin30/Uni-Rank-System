def getInformation(selectCountry, RankingFileName, CapitalsFileName):
    try:
        RankingFileName = open('TopUni.csv', 'r')
        counter = -1
        univcount = RankingFileName.readline()
        with open('output.txt', 'w'):
            while univcount !='':
                univcount = RankingFileName.readline()
                counter += 1

            f = open('output.txt', 'w')

            f.write("Total number of universities => " + str(counter))
            # f.write(func1list)
    finally:
        f.close()











#getInformation('usa', 'TopUni.csv', 'capitals.csv')
