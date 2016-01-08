def checkForDays():
    pass

def RCDistribution(year = 1996, plot = False, measureTime = False):
    """
    Takes a year and checks for possible rodna cisla within each day of the year
    :param year: A year to check for possibilities
    :param plot: If True, a lot will be generated and displayed
    :param measureTime: Prints time for execution if True
    :param testGender: boolean, if true a check will be performed for RCs assigned to females. Their RC is obtained by adding 50 to the month component
    :return: dictionary translating days of a year a to number of possibilities for RC in the year. A touple of two dictionaries if testGender
    """
    #importing methods

    import itertools, pylab, time

    afterSlash = [] # to be generated by iterlools  later

    #sanity checking on format of the year, converting to str otherwise
    if len(str(year)) == 4:
        year = str(year)[-2:]
    else:
        if type(year) != str:
            year = str(year)

    #dict to store possible combinations of rodne cislo within a year
    dayPossibilities = {}


    #generates all possible 3 digit numbers to test with the before slash component (length of 6561)
    afterSlash = []
    for i in itertools.product([str(i) for i in xrange(0,10)], repeat=4): 
        afterSlash.append(''.join(i))          # add that shit to the list

     
    
    if measureTime:
        start = time.clock()

    #dictionary with number of days per month
    daysDict = {"01":"31","02":"28","03":"31","04":"30","05":"31","06":"30","07":"31","08":"31","09":"30","10":"31","11":"30","11":"31","12":"30"}


    for month in daysDict.keys():
        for day in range(int(daysDict[month])+1)[1:]:
            if len(str(day)) == 1:
                dayChanged = "0"+str(day)
            else:
                dayChanged = day
            possibilities = 0
            beforeSlash = str(year) + str(month) + str(dayChanged)
            print "Before slash = " + beforeSlash
            for combination in afterSlash:
                print "After slash: " + combination
                rc = beforeSlash + combination
                print rc
                if int(rc[:9])%11==int(rc[9]):
                    possibilities += 1
            dayPossibilities[beforeSlash] = possibilities


    if measureTime:
        print str((time.clock() - start))

    if plot:
        pylab.figure()
        pylab.ylim(0,1200)
        pylab.xlim(0,366)
        pylab.plot(dayPossibilities.values())

        pylab.show()

    return dayPossibilities
