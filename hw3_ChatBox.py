import random
import re

samples = {
    r'Γειά σου': ['Γειά σου!'],
    r'Καλησπέρα' : ['Καλησπέρα σας!'],
    r'Πώς είσαι;': ['Είμαι καλά, εσύ;'],
    r'Τι κάνεις;': ['Διαβάζω, εσύ;'],
    r'Πώς σε λένε;': ['Με λένε Άγγελο, εσένα;'],
    r'Πόσο χρονών είσαι;': ['Δεν μπορώ να σου πω την ηλικία μου.']
}

while True:
    met = False
    user_input = input("Ρώτησε με κάτι: ")
    for sample, responses in samples.items():
        match = re.match(sample, user_input)
        if match:
            print(random.choice(responses))
            found = True
            break
    if met == False:
        print('\nΜπορείς να ρωτήσεις κάτι άλλο;')
