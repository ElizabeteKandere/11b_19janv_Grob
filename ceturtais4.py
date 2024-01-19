# Izveidot Python faila programmu, kur lietotajs ievada faila nosaukumu un formātu, un atkarībā no faila formāta, tiek nolasīts faila saturs. Nolasītā informācija ir jāizdrukā terminālī.

import json 

def lasit_faila_saturu(ceturtais4.json, txt):

     with open(ceturtais4.json, 'r') as dzonsons:
        saturs = dzonsons.read()

# drukā

        print(f"Faila saturs (txt):")
        print(saturs)

faila_nosaukums = input("ceturtais4.json")
faila_formats = input("txt")

