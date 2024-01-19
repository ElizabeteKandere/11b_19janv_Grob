# Izveidot Python programmu, kas nolasītu un izdrukātu trešās teksta faila rindas saturu. 

# nolasa datus no faila

import json

def lasit_treso_rindu(tresais3.json):

    with open('tresais3.json', 'r', encoding='utf-8') as tresie:
    
       rindu_rindas = tresie.readlines()

    
# drukā
    if len(rindu_rindas) >= 3: 

         print(rindu_rindas[2])
