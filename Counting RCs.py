def Join(touple):
    """
    takes a touple and returns str concatenating all elements within the touple
    :param sixgrams: A touple to be concatenated
    :return: string
    """
    result = ""
    for i in touple:
        result +=(str(i))
    return result

def checkDate(beforeSlash = "931020"):
    """
    takes a before slash argument of RC and checks for number pf possibilities

    :param beforeSlash: combination constructed with year, month, day.
    :return: a count of possible combinations, int
    """
    import itertools
    possibilities = []

    if type(beforeSlash) != str:
        beforeSlash = str(beforeSlash)

    assert (len(beforeSlash)==6), "Incorrent length of the input argument"


    for combination in itertools.product([str(i) for i in xrange(0,10)], repeat=3):
        comb = (' '.join(i) for i in combination)
        RC = str(beforeSlash)
        RC += Join(comb)
        remainder = int(RC)%11
        if remainder == 10:
            remainder = 0
        RC += str(remainder)

        if RC not in possibilities:
            possibilities.append(RC)
    print beforeSlash + ": " + str(len(possibilities)) + " possibilities."
    return len(possibilities)

def checkYear(year= 1993):
    """
    :param year: a year to be checked format either 1993 or 93, int or str
    :return: dictionary translating date combinations to number of possibilities
    """

    daysDict = {"01":"31","02":"28","03":"31","04":"30","05":"31","06":"30","07":"31","08":"31","09":"30","10":"31","11":"30","11":"31","12":"30"}
    possibilitiesDict = {}
    if type(year) != str:
        year = str(year)

    if len(year) == 4:
        year = year[2:]

    for month in daysDict.keys():

        for day in range(int(daysDict[month])+1)[1:]:
            if day < 10:
                formatedDay = "0" + str(day)
            else:
                formatedDay = str(day)
            beforeSlash = str(year) + month + formatedDay
            possibilitiesDict[beforeSlash] =checkDate(beforeSlash)

    return possibilitiesDict

def plotYear(year = 1993):
    """
    :param year:
    :return:
    """
    dayPossibilities = checkYear(year)

    import pylab

    pylab.figure()
    pylab.ylim(0,1200)
    pylab.xlim(1,366)
    pylab.title("Posiibilities for male rodna cisla in year " + str(year))
    pylab.plot(dayPossibilities.values())
