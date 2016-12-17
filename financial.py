#INPUT YEAR
#INPUT QUARTER i.E. 3Q16, 2Q16
#INPUT TIME PERIOD - i.E. YEAR, QUARTER or multiple quarters i.e. 9ME

#Revenues for the "TIME PERIOD - I.E. 9ME16" "rose or fell" to "INPUT 9ME Revenues HERE" which is a "% change" from 9ME15.
#This "fall or rise" in revenues was driven by "INPUT RATIONALE HERE".

def calc(Year, Quarter, TimePeriod, Revenues, PriorRevenues):
    pass

    PercentageChange = ((float(Revenues) - float(PriorRevenues))/float(PriorRevenues))
    REVENUES = "REVENUES: Revenues for " + str(Year) + "were " + str(Revenues) + "which represents a " + str(PercentageChange) + \
    " percent change from " +  str(int(Year) - 1) + "."
    Reason = None
    print("State reason for change in revenues.")

    if PercentageChange > 0:
        Reason = input(  'Revenues rose due to:   ')
    else:
        Reason = input('Revenues fell due to: ')

    print(REVENUES)

if __name__=="__main__":

  Year = input('Enter the year being analyzed: ')
  Quarter = input('Enter the quarter being analyzed: ')
  TimePeriod = input('Enter the time period being analyzed - I.E. 9ME16 / FYE15 / 3ME16')
  Revenues = input('Please enter revenues for the time period entered: ')
  PriorRevenues = input('Please enter revenues for the time period - 1 year --- I.E. if you are analyzing 9ME16 revenues, enter 9ME15 revenues')
  calc(Year, Quarter, TimePeriod, Revenues, PriorRevenues)
