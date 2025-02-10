#Stuff
Hour = 40
OT_Rate = 1.5

#Inputs
Hours = float(input("Enter hours worked"))
Hour_Rate= float(input("Enter pay rate per hour"))

#Calculations (Over Time)
if Hours > Hour:
    Pay = Hour * Hour_Rate
    OT_Hours = Hours - Hour
    OT_Pay = OT_Hours * (Hour_Rate * OT_Rate)
    gross_OT = Pay + OT_Pay

#Calculations Normal Time
else:
    gross = Hours * Hour_Rate

if Hours < Hour:
    print("Gross: ", gross)
else:
    print("Gross Over time: ", gross_OT)