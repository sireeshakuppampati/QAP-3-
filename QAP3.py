#Program to generate and calculate the invoice
#for Honest Harry Car Sales
#Date written : OCT 16 2023
#Author : SIREESHA KUPPAMPATI
import datetime
print()
print()

# Declaring constants
Tfee = 0.1
Ltax = 0.016
HST = 0.15
Fin_Rate = 39.99

# Defining  user input values
allowed_char = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-")
while True:
    

    while True:

        Cust_Firstname = input("Enter the customer first name (END to quit):    ").title()
        # Checking the firstname validation
        if Cust_Firstname == "":
                print("Customer Firstname must not be blank. Please re-enter:       ")

        elif set(Cust_Firstname).issubset(allowed_char) == False:
            print("Customer Firstname contains invalid characters. Please re-enter:     ")

        else:
            break

        #"END" to quit
    if Cust_Firstname.upper() == "END":
        break

            


    while True:
    
        Cust_Lastname = input("Enter the customer last name          :     ").title()
        # Checking the lastname validation
        if Cust_Lastname == "":
            print("Customer Lastname must not be blank. Please re-enter:    ") 
        elif set(Cust_Lastname).issubset(allowed_char) == False:
            print("Customer Lastname contains invalid characters. Please re-enter:    ")
        else:
            break
    print(Cust_Firstname)
    print(Cust_Lastname)

    StAddr = input("Enter the customer street address          : ").upper() 
    City = input("Enter the city                             :    ").upper()
    while True:

        Prov = input("Enter the  province (XX)                 :    ").upper()
        if Prov !="NL" and Prov !="NB" and Prov !="PE" and Prov !="NS":
            print("Province must be of NL,NS,NB or PE. Please re-enter:    ")
        else:
            break

    PostalCode = input("Enter the postal code                     :   ").upper() 

    while True:

        Ph_Num = input("Enter the customer phone number (9999999999):    ")
        if Ph_Num == "":
            print("Phone number cannot be blank. Please re-enter:   ")
        elif len(Ph_Num) != 10:
            print("Phone number must contain 10 digits. Please re-enter:  ")
        elif Ph_Num.isdigit() == False: 
            print("Phone number must contain numbers only. Please re-enter:  ")
        else:
         break
    Ph_Num1 = "(" + Ph_Num[0:3] + ")" + Ph_Num[3:6] + "-" + Ph_Num[6:]
    print(Ph_Num1)

    while True:

        Plate_Num = input("Enter the plate number (xxx000):  ").upper()
        if Plate_Num == "":
             print("Plate number cannot be blank. Please re-enter:  ")
        elif len(Plate_Num) != 6:
             print("Plate number must contain 6 characters. Please re-enter:  ")
        elif Plate_Num[0:3].isalpha() == False: 
                print("First 3 characters must be alphabetics only. Please re-enter:  ")
        elif Plate_Num[3:].isdigit() == False:
            print("Last 3 characters must be numbers")
        else:
            break

    print(Plate_Num)   

    Car_Make = input("Enter the car making company:  ").title()
    Car_Model = input("Enter the car model:  ").title()
    Made_In_Year = input("Enter the car made-in year: ")
    Sales_Person = input("Enter the sales person name:  ").title()

    # Calculation part
    while True:
        Selling_Price = 0
        try:
            Selling_Price = int(input("Enter selling price (Must be less than 50000):  "))
        except:
            print("Selling price must be lessthan 50000 - please re-enter: ")
        else:
            if Selling_Price > 50000 or Selling_Price == "":
                print("Thats not a valid number, please re-enter, lessthan 50000:")
            else:
                break
    while True:
            Trade_In_Amt = 0
            try:
                Trade_In_Amt = int(input("Enter the trade-in-amount (Must be less than the selling price):  "))
            except:
                print("Thats not a valid number, please re-enter: ")
            else:
                if Trade_In_Amt >= Selling_Price or Trade_In_Amt == "":
                    print("Trade in amount must be lessthan selling price.Please re-enter: ")
                else:
                    break

                


    print("selling price:" , Selling_Price)
    print("trede in amount:", Trade_In_Amt)

    Price_aft_Trade = Selling_Price - Trade_In_Amt
    print("price after trade: ", Price_aft_Trade)

    licensefee = 0
    if Selling_Price <= 5000.00:
        licensefee = 75.00
    else:
        licensefee = 165.00

    print("licence fee:", licensefee)    

    Trans_fee = 0
    if Selling_Price <=20000:
        Trans_fee = Tfee * Selling_Price 
    else:
        Lux_Tax = Ltax * Selling_Price
        Trans_fee = (0.01 * Selling_Price) + Lux_Tax

    print("transfer fee:", Trans_fee)

    Subtotal = Price_aft_Trade + licensefee + Trans_fee
    HST1 = HST * Subtotal
    Tot_Sales_Price = Subtotal + HST
    print("subtotal:", Subtotal)
    print("HST:", HST1)
    print("total sales price:", Tot_Sales_Price)

    Cust_Name = Cust_Firstname[0] + "." + Cust_Lastname

    FullCPP = City + "," + " " + Prov + " " + " " + PostalCode

    Car_Details = Made_In_Year[0:4] + " " + Car_Make[0:10] + " " + Car_Model[0:10]
    Receipt_id = Cust_Firstname[0] + Cust_Firstname[1] + "-"  + Plate_Num[3:6] + "-" + Ph_Num[6:10]
    CurrDate = datetime.datetime.now()
    CurrDateDsp = CurrDate.strftime("%B %d, %Y")
    Inv_Date = CurrDate.strftime("%d %b %y")
    FPaydate = CurrDate + datetime.timedelta(days= 30)
    First_pay_Date = FPaydate.strftime("%d %b %y")
        

    print()
    print()
    print(f"                    123456789012345678901234567890123456789012345678901234567890123456789012345678")
    print()
    print(f"                    Honest Harry Car Sales                           Invoice Date:{CurrDateDsp:>10s}")                   
    print(f"                    Used Car Sale and Receipt                         Receipt No:      {Receipt_id:>11s}")
    print()

    Selling_PriceDSP = "${:,.2f}".format (Selling_Price)
    print(f"                                                            Sale price:                 {Selling_PriceDSP:>9s}")

    Trade_In_AmtDSP = "${:,.2f}".format (Trade_In_Amt)
    print(f"                    Sold to                                 Trade Allowance:            {Trade_In_AmtDSP:>9s}")
    print(f"                                                            --------------------------------------- ")

    Price_aft_TradeDSP = "${:,.2f}".format (Price_aft_Trade)
    print(f"                          {Cust_Name:<29s}     Price after Trade:           {Price_aft_TradeDSP:>9s}")

    licensefeeDSP = "${:,.2f}".format (licensefee)
    print(f"                          {StAddr:<29s}     License Fee:                 {licensefeeDSP:>9s}")

    Trans_feeDSP = "${:,.2f}".format (Trans_fee)
    print(f"                          {FullCPP:<29s}     Transfer Fee:                {Trans_feeDSP:>9s}")
        
    print(f"                                                            ---------------------------------------- ")

    SubtotalDSP = "${:,.2f}".format (Subtotal)
    print(f"                    Car Details:                            Subtotal:                    {SubtotalDSP:>9s}")

    HSTDSP = "${:,.2f}".format (HST1)
    print(f"                                                            HST:                         {HSTDSP:>9s}")
    print(f"                          {Car_Details:<29s}     ----------------------------------------- ")

    Tot_Sales_PriceDSP = "${:,.2f}".format (Tot_Sales_Price)
    print(f"                                                            Total sales price:           {Tot_Sales_PriceDSP:>9s}")
    print()
    print()
    print(f"                    -------------------------------------------------------------------------------------")
    print()
    print()
        
        
    print(f"                                                           Financing         Total        Monthly")
    print(f"                                     # Years  # Payments      Fee           Price        Payment")
        
    print()
        
    for years in range(1,5):
        Payments = years * 12
        Fin_Fee = years * Fin_Rate
        Tot_Price = Tot_Sales_Price + Fin_Fee
        Mon_Pay = Tot_Price / (years * 12)

        PaymentsDSP = "${:,.2f}".format(Payments)
        Fin_FeeDSP = "${:,.2f}".format(Fin_Fee)
        Tot_PriceDSP = "${:,.2f}".format(Tot_Price)
        Mon_PayDSP = "${:,.2f}".format(Mon_Pay)
        
        print(f"                                     {years:>2d}       {PaymentsDSP:>2s}     {Fin_FeeDSP:>9s}       {Tot_PriceDSP:>9s}     {Mon_PayDSP:>9s}   ")
                
        

    print()
    print()
    print(f"                   -------------------------------------------------------------------------------------")
    print(f"                             Invoice date:         {Inv_Date:<9s}      First payment date:      {First_pay_Date:>9s}")
    print() 
                                
    print(f"                   -------------------------------------------------------------------------------------")
    print(f"                                           Best used cars at the best prices!")
    print()
    print()
print()
print()        
print("Thank you have a nice day")
print()
print()
                   