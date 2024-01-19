# Izveidot Python programmu, kas ļauj lietotājam ievadīt savu vārdu terminālī. Ievadīto vārdu pēc tam ierakstīt teksta failā (piemēram, "lietotajs.txt").

def ievadit_faila(Elizabete, piektais5.py):

    with open(piektais5.py, 'a') as vardi:
         vardi.write(Elizabete + '\n')
    print(f"Lietotāja vārds '{Elizabete}' ir ierakstīts failā '{piektais5.py}'.")

    lietotaja_vards = input("Elizabete")
    faila_nosaukums = 'piektais5.py'