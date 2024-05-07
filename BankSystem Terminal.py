from pwinput import pwinput
from os import system, name
import hashlib
import json

LoggedIn = False

print("Welcome to AndyBank. What do you want to do? Type -help for help")

def encrypt(data):
    encrypted_data = hashlib.sha512(data.encode('utf-8'))
    return encrypted_data.hexdigest()
try:
    with open('brukere.json', 'r') as file:
        brukere = json.load(file)
except json.decoder.JSONDecodeError:
    brukere = {}


while True:
    answer = input().lower()
    if answer == "-help":
        input(
            "---------------------------------\nCommands you can use:\n-   Clear\n-   Login\n-   Regrister\n-   Send Money\n-   Check Balance\n---------------------------------\n")

    elif answer == "clear".lower():
        print("In progress. Code doesnt work")


    elif answer == "regrister".lower():
        if not LoggedIn:
            while True:
                try:
                    with open('brukere.json', 'r') as file:
                        brukere = json.load(file)
                except json.decoder.JSONDecodeError:
                    brukere = {}

                navn = input('Brukernavn: ').lower()
                if brukere.get(navn):
                    print('Bruker eksisterer allerede.')
                    continue
                passord = input('Passord: ')
                kryptert_pw = encrypt(passord)

                brukere[navn] = {'passord': kryptert_pw, 'money': '2000'}
                with open('brukere.json', 'w+') as f:
                    json.dump(brukere, f, indent=4)
                    print("Brukernavn registrert")
                    break
        else:
            print("You are already logged in as " + navn + ".")





    elif answer == "login".lower():
        if not LoggedIn:
                navn = input('Brukernavn: ').lower()
                passord = input('Passord: ')
                kryptert_pw = encrypt(passord)

                if brukere.get(navn) and brukere[navn]['passord'] == kryptert_pw:
                    print("Velkommen tilbake " + navn)
                    LoggedIn = True
                else:
                    print('Feil brukernavn eller passord')
        else:
            print("You are not logged in.")









    elif answer == "check balance".lower():
        if LoggedIn:
            with open('brukere.json', 'r') as file:
                data = json.load(file)
                username = (navn)
                if username in data:
                    money = data[username]['money']
                    print(f"The money for user {username} is: {money}")
                else:
                    print(f"User '{username}' not found in the JSON data.")


    elif answer == "Send money".lower():
        if LoggedIn:
            with open('brukere.json', 'r') as file:
                data = json.load(file)
                username = (navn)
                money = data[username]['money']
                if username in data:
                    balance = data[username]['money']
                    print("You are logged in as: " + username)
                    if money >=0:
                        print("No money in account")
                    else:
                        print("Balance: " + money)
                    if brukere.get(navn) == kryptert_pw:
                        print("Velkommen tilbake " + navn)

                    SendToUser = input("Who do you want to send money to? ")
                    amount = input("Amount to send to " + SendToUser)

        else:
            print("You are not logged in.")