# Miggy Reyes
# Texas Tech University
# CS 1411 - 502

#
# Problem 1
#

def retFund(salary, save, growthRate, years):
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - growthRate: the annual percent increase in your investment account (an
      integer between 0 and 100).
    - years: the number of years to work.
    - return: a list whose values are the size of your retirement account at
      the end of each year.
    """
    retirementFund = []                         # Will store a list of floats
    prevYearFund = salary * save * 0.01
    retirementFund.append(float(prevYearFund))  # Adds initial size of account

    while years > 1:    # Will break loop when all the given years have passed
                        # and skips the first year since that has already been
                        # calculated
        prevYearFund = prevYearFund * (1 + 0.01 * growthRate) + salary * save * 0.01
        retirementFund.append(float(prevYearFund))
        years -= 1      # Will make sure that the right amount of years are calculated

    return retirementFund

def testRetFund():
    salary     = 10000
    save       = 10
    growthRate = 15
    years      = 5
    savingsRecord = retFund(salary, save, growthRate, years)
    print (savingsRecord)
    # Output should have values close to:
    # [1000.0, 2150.0, 3472.5, 4993.375, 6742.3812499999995]

    salary = 30000
    save = 60
    growthRate = 5
    years = 4
    savingsRecord = retFund(salary, save, growthRate, years)
    print(savingsRecord)
    # Output should have values close to:
    # [18000.0, 36900.0, 56745.0, 77582.25]

    salary = 80000
    save = 7
    growthRate = 20
    years = 3
    savingsRecord = retFund(salary, save, growthRate, years)
    print(savingsRecord)
    # Output should have values close to:
    # [5600.0, 12320.0, 20384.0]

#
# Problem 2
#

def retVariable(salary, save, growthRates):
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - growthRate: a list of the annual percent increases in your investment
      account (integers between 0 and 100).
    - return: a list of your retirement account value at the end of each year.
    """

    returnVar = []

    for index, value in enumerate(growthRates):
        savings = salary / save

        if index == 0:
            tempF = retFund(salary, save, value, len(growthRates))[index]
            returnVar.append(tempF)

        else:
            tempF = tempF * (1 + 0.01 * growthRates[index]) + savings
            returnVar.append(tempF)


    return returnVar

def testRetVariable():
    salary      = 10000
    save        = 10
    growthRates = [3, 4, 5, 0, 3]
    savingsRecord = retVariable(salary, save, growthRates)
    print (savingsRecord)
    # Output should have values close to:
    # [1000.0, 2040.0, 3142.0, 4142.0, 5266.2600000000002]

    # TODO: Add more test cases here.

    salary      = 15000
    save        = 8
    growthRates = [3, 9, 5, 3, 3]
    savingsRecord = retVariable(salary, save, growthRates)
    print (savingsRecord)
    # Output should have values close to:
    # [1200.0, 3183.0, 5217.15, 7248.6645, 9341.124435]
    # TODO: Add more test cases here.

    salary      = 10000
    save        = 1
    growthRates = [6, 4, 22, 0, 3]
    savingsRecord = retVariable(salary, save, growthRates)
    print (savingsRecord)
    # Output should have values close to:
    # [100.0, 10104.0, 22326.879999999997, 32326.879999999997, 43296.6864]

    # TODO: Add more test cases here.

    salary      = 17500
    save        = 5
    growthRates = [6, 4, 5, 0, 3]
    savingsRecord = retVariable(salary, save, growthRates)
    print (savingsRecord)
    # Output should have values close to:
    # [875.0, 4410.0, 8130.5, 11630.5, 15479.415]
    # TODO: Add more test cases here.

#
# Problem 3
#

def postRetirement(savings, growthRates, expenses):
    """
    - savings: the initial amount of money in your savings account.
    - growthRate: a list of the annual percent increases in your investment
      account (an integer between 0 and 100).
    - expenses: the amount of money you plan to spend each year during
      retirement.
    - return: a list of your retirement account value at the end of each year.
    """
    postRetirementList = []

    for index, value in enumerate(growthRates):
        if index == 0:
            savings = savings * (1 + 0.01 * growthRates[index]) - expenses
        else:
            savings = postRetirementList[index - 1] * (1 + 0.01 * growthRates[index]) - expenses

        postRetirementList.append(savings)

    return postRetirementList


def testPostRetirement():
    savings     = 100000
    growthRates = [10, 5, 0, 5, 1]
    expenses    = 30000
    savingsRecord = postRetirement(savings, growthRates, expenses)
    print (savingsRecord)
    # Output should have values close to:
    # [80000.000000000015, 54000.000000000015, 24000.000000000015,
    # -4799.9999999999854, -34847.999999999985]

    savings = 125000
    growthRates = [10, 5, 0, 5, 1]
    expenses = 38000
    savingsRecord = postRetirement(savings, growthRates, expenses)
    print (savingsRecord)
    # Output should have values close to:
    # [99500.0, 66475.0, 28475.0, -8101.25, -46182.2625]

    savings = 165000
    growthRates = [10, 5, 0, 5, 1]
    expenses = 15000
    savingsRecord = postRetirement(savings, growthRates, expenses)
    print (savingsRecord)
    # Output should have values close to:
    # [166500.00000000003, 159825.00000000003, 144825.00000000003, 137066.25000000003, 123436.91250000003]

    savings = 170000
    growthRates = [10, 5, 0, 5, 1]
    expenses = 25000
    savingsRecord = postRetirement(savings, growthRates, expenses)
    print (savingsRecord)
    # Output should have values close to:
    # [162000.00000000003, 145100.00000000003, 120100.00000000003, 101105.00000000003, 77116.05000000003]


if __name__ == "__main__":
    # retFund(80000, 2, 5, 20)
    # testRetFund()
    # testRetVariable()
    # testPostRetirement()
    pass
