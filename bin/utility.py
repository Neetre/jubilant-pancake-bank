'''
Random stuff
'''

def generate_clientcode(name, surname, email):
    mail = email.split("@")[0].lower()
    name = name.lower()
    surname = surname.lower()

    client_code = name[0:3] + mail[0:3] + surname[-3:]
    return client_code
