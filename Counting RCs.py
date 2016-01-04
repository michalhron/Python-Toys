def RCDistribution(year = 1996, plot = False, testGender = False, measureTime = False):
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

    #initialize dictionary for storing the values for female versions
    if testGender:
        dayPossibilitiesWoman = {}

    #generates all possible 4 digit numbers to test with the before slash component (length of 6561)
    for i in itertools.product([str(i) for i in xrange(1,10)], repeat=4):
        afterSlash.append(''.join(i))


    if measureTime:
        start = time.clock()

    #dictionary with number of days per month
    daysDict = {"1":"31","2":"28","3":"31","4":"30","5":"31","6":"30","7":"31","8":"31","9":"30","10":"31","11":"30","11":"31","12":"30"}


    for month in daysDict.keys():
        for day in range(int(daysDict[month])):
            possibilities = 0
            beforeSlash = str(year) + str(int(month)+50) + str(day)
            for combination in afterSlash:
                rc = beforeSlash + combination
                if int(rc) % 11 == 0:
                    possibilities += 1
            dayPossibilities[beforeSlash] = possibilities

    if testGender:
        for month in daysDict.keys():
        #print "month: " + month
            for day in range(int(daysDict[month])):
                #print "Day: " + str(day)
                possibilities = 0
                beforeSlash = str(year) + str(int(month)+50) + str(day)
                for combination in afterSlash:
                    rc = beforeSlash + combination
                    if int(rc) % 11 == 0:
                        possibilities += 1
                dayPossibilitiesWoman[beforeSlash] = possibilities

    if measureTime:
        print str((time.clock() - start))

    if plot:
        pylab.figure()
        pylab.ylim(0,1200)
        pylab.plot(dayPossibilities.values())
        if testGender:
            pylab.plot(dayPossibilitiesWoman.values())

        pylab.show()

    if testGender:
        return (dayPossibilities, dayPossibilitiesWoman)
    return dayPossibilities

