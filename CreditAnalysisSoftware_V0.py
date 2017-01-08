


# HOMEWORK, use TKINTER within Application
# Look into Djanjo web framework
#PEP 8 - Style Guidelines for Code


#FUNCTIONS HERE
def calc(yr,
         qr,
         tp,
         revs,
         revs_1,
         ):

    pc = ((float(revs) - float(revs_1)) / float(revs_1)) * 100
    revwrite = "REVENUES: Revenues for " + str(yr) + " were " + str(revs) + " which represents a " + str(pc)[0:4] + " percent change from " + str(int(yr) - 1) + "."
    print(revwrite)

if __name__=="__main__":

  #Time Inputs
  yr = input('Enter the year in which performance is being analyzed: ')
  qr = input('Enter the quarter being analyzed: ')
  tp = input('Enter the time period being analyzed. I.E., 9ME, 6ME, 3ME')

  #Revenue Inputs
  revs = input('Please enter revenues for the time period entered: ')
  revs_1 = input('Please enter revenues for the time period - 1 year --- I.E. if you are analyzing 9ME16 revenues, enter 9ME15 revenues')

  #EBITDA Inputs
  #Adjusted_EBITDA = input("Please enter Adjusted EBITDA")
  #Adjusted_EBITDA_1 = input("Please enter Adjusted EBITDA for the prior period being analyzed")

  #Cash Flow Inputs
  #CFO = input("Please enter Total Debt as specified at the end of " + Year )
  #CFO_1 = input("Please enter Total Debt as specified at the end of " + Year-1 )
  #Divs = input("Please enter Dividends as specified at the end of " + Year )
  #Divs_1 = input("Please enter Dividends as specified at the end of " + Year )
  #CapEx = input("Please enter CapEx as specified at the end of " + Year )
  #CapEx_1 = input("Please enter CapEx as specified at the end of " + Year )
  #WC = input("Please enter total working capital swings as specified at the end of " + Year )
  #WC_1 = input("Please enter total working capital swings as specified at the end of " + Year )
  #FCF = (CFO-Divs-Capex)
  #FCF_1 = (CFO_1 - Divs_1 - CapEx_1)

  #Leverage and LIQUIDITY Inputs
  #Total_Debt = input("Please enter Total Debt as specified at the end of " + )

  #Leverage = Total_Debt / Adjusted_EBITDA

  # Write-Up Strings
  # Adjusted_EBITDA = "Adjusted EBITDA: Adjusted EBITDA for " + TimePeriod + " " + str(Year) + " was "
  # CASH_FLOWS = "CASH FLOWS: Cash from operations for " + TimePeriod + " " + str(Year) + " was "
  # LEVERAGE_AND_LIQUIDITY = "LEVERAGE & LIQUIDITY: Leverage, as defined by Total Debt divided by Adjusted EBITDA, stood at "

  # Reason = None
  # print("State reason for change in revenues.")
  # if PercentageChange > 0:
  # Reason = input('Revenues rose due to:   ')
  # else:
  # Reason = input('Revenues fell due to: ')
  # print(REVENUES)

  calc(yr, qr, tp, revs, revs_1)

