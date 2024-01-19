# Izveidot Python programmu, kas nolasītu un izdrukātu visu teksta faila saturu (txt formātā). 

# nolasa datus no faila

import json

with open('pirmais1.json', 'r', encoding='utf-8') as pirmie:
    nolasa_datus=json.load(pirmie)


# drukā

print(nolasa_datus)
