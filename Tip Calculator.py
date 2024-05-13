print("Welcome to the tip calculator")
Bill = float(input("How much was the bill:"))
Tip_Percent = int(input("What percent would you like to tip(10/12/15): "))

def COST(Bill,Tip):
    tip_amount = (Bill * Tip_Percent)/100
    return tip_amount
tip = COST(Bill,Tip_Percent)
print("Tip Amount: ",tip)