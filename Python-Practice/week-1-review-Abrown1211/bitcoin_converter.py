# Please write your bitcoin_converter program in this file.
#!/usr/bin/python
 
from datetime import datetime

i = datetime.now()
print ("As of", i.strftime('%m/%d/%Y %H:%M %p'), "bitcoin is currently trading at $5805 per bitcoin")
UserCoinAmt = float(input("Enter the bitcoin amount: "))
USDbtcConversion = 5805 * UserCoinAmt
    
print("That is worth", USDbtcConversion, "us dollars.")

