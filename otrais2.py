# Izveidot Python programmu, kas nolasītu un izdrukātu tikai otrās kolonnas datus no CSV faila.
# nolasa datus

import csv

def lasit_otro_kolonnu(otrais2.csv):
    with open(otrais2.csv, 'r') as lulu:

        lasitajs= csv.reader(lulu)

        for rindina in lasitajs:
            if len(rindina) >= 2:
                print(rindina[1])