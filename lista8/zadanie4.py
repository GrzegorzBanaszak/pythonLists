serniczkowyspam = {}


def add_new_adres(email, name):
    if name not in serniczkowyspam:
        serniczkowyspam[name] = email
    else:
        print("Osoba jest już zarejstrowania do mailingu")

#


def get_mails():
    return serniczkowyspam


add_new_adres("jakKowalski@gmail.com", "Jan Kowajski")

print(serniczkowyspam)
