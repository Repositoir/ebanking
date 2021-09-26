path = int(input('''Choose a service:

1.Simple/Compound Interest Calculator
2.Create a new account
3.Currency converter (USD/INR)
4.Cryptocurrency info
5.Cryptocurrency conversion
6.Mutual Funds

'''))

print ("******************************")

if path == 1:
       
        p = float(input("Enter principal amount: "))

        t = float(input("Enter time (in years)"))

        r = 5/100

        si = p*r*t/100

        print ("******************************")

        print ("Your simple interest principal after ",t,"years will be = ",si+p)

        ci = p*(1+r)**t

        print ("Your compound interest principal after ",t,"years will be = ",ci)

elif path == 2:
    name = str(input("Enter your name: "))
    address = str(input("Enter your address: "))
    age = int(input("Enter your age: "))

    if age <= 18:
        print("Your application will be rejected due to your age.")
    else:
        print ('''The below details are of your new bank account:
Name = ''',name,'''\nAddress = ''',address,'''\nAge = ''',age)

elif path == 3:
    currency = int(input('''Choose the conversion:
1. USD to INR
2. INR to USD'''))
    if currency == 1:
        usd = float(input("Enter amount in USD = "))
        print ("Your value in INR is = ", (usd*74.56)//1)
    else:
        inr = float(input("Enter amount in INR = "))
        print ("Your value in USD is = ", inr*0.02)

elif path == 4:
    print ("******************************")
    buy_info = int(input('''Select your operation on bitcoin:
1. Check bitcoin's latest price
2. Check ether's latest price
3. Check dogecoin's latest price'''))
    if buy_info == 1:
        print ("******************************")    
        print ("Bitcoin's last price was 40000 USD")

    elif buy_info == 2:
        print("Ethereum last price was 2646 USD")

    elif buy_info == 3:
        print("Dogecoin last price was 0.21 USD")

elif path == 5:
        path_crypt = int(input('''Which conversion would you like to do
1.USD ---> BTC
2.BTC ---> USD
3.INR ---> BTC
4.BTC ---> INR
'''))
        if path_crypt == 1:
                usd_btc = float(input("Enter amount in USD here: "))
                print (usd_btc," USD is ", usd_btc*0.000025, " BTC")
        elif path_crypt == 2:
                btc_usd = float(input("Enter amount in BTC here: "))
                print (btc_usd," BTC is ", btc_usd*40000, " USD")
        elif path_crypt == 3:
                inr_btc = float(input("Enter amount in INR here: "))
                print (inr_btc," INR is ", inr_btc*0.0000004," BTC")
        elif path_crypt == 4:
                btc_inr = float(input("Enter amount in BTC here: "))
                print (btc_inr," BTC is ", btc_inr*3000000, " INR")

elif path == 6:
    funds = int(input('''Choose which mutual funds you would like to invest in:
1. TATA MOTORS
2. HDFC FIN LTD
3. INFOSYS'''))
    if funds == 1:
        print ("Your order for buying TATA MOTORS has been submitted")
    elif funds == 2:
         print ("Your order for buying HDFC FIN LTD has been submitted")
    elif funds == 3:
         print ("Your order for buying INFOSYS has been submitted")
else:
    print("Please select an integer value and try again")
        
    
