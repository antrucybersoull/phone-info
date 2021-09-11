import phonenumbers
from phonenumbers import carrier,geocoder,timezone
import os
import time
import sys

def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(10. / 100)
slowprint("[!] Starting : ")
time.sleep(5)
os.system('clear')

slowprint("        Made by A N ⃢T RU_ᴄʏᷧʙᷠᴇͭʀͬ_sͧᴏᴜʟ       ")
os.system('figlet Antru')


phoneNo =input("Enter mobile number with country code : ")
phoneNo =phonenumbers.parse(phoneNo)

print(timezone.time_zones_for_number(phoneNo))

print(carrier.name_for_number(phoneNo, "en"))

print(geocoder.description_for_number(phoneNo, "en"))

print("Valid phone number : ",phonenumbers.is_valid_number(phoneNo))

print("Checking possibility of number : ",phonenumbers.is_possible_number(phoneNo))
