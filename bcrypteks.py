import hashlib
import json

def encrypt(data):
    encrypted_data = hashlib.sha512(data.encode('utf-8'))
    return encrypted_data.hexdigest()

while True:
    try:
        brukere = json.loads('brukere.json')
    except json.decoder.JSONDecodeError:
        brukere = {}

    x = input('reg / log / list: ')

    if x == 'reg':
        navn = input('Brukernavn: ').lower()
        if brukere.get(navn):
            print('Bruker eksisterer allerede.')
            continue
        passord = input('Passord: ')
        kryptert_pw = encrypt(passord)

        brukere[navn] = {'passord': kryptert_pw}
        with open('brukere.json', 'w+') as f:
            f.write(json.dumps(brukere))

    if x == 'log':
        navn = input('Brukernavn: ').lower()
        passord = input('Passord: ')
        kryptert_pw = encrypt(passord)

        if brukere.get(navn) and brukere[navn]['passord'] == kryptert_pw:
            print('Passord og brukernavn matchet')
        else:
            print('Feil brukernavn eller passord')

    if x == 'list':
        print(brukere)
