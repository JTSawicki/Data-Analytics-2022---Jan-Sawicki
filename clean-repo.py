# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 09:37:48 2022

@author: jasio
"""

import os
import sys

# Funkcja znajduje podfoldery
def FindFolders(path):
    folders = []
    

# Lista rozszerzeń do usunięcia
extensions = ['.exe', '.zip']
# Nazwa pliku skryptu
script_name = 'clean-repo.py'
# tworzenie listy plików do usunięcia
files_to_delete = []

# Powiadomienie o lokalizacji skryptu
print("Assuming script file name is: '" + script_name + "'")

# Powiadomienie o lokalizacji skryptu i kontrola jej poprawnosci
print(os.path.realpath(__file__))
masterpath = os.path.realpath(__file__)[:-( len(script_name) + 1)]
print('Is this your script location: ' + masterpath)
choice = input('(y/n)> ')

# Sprawdzenie odpowiedzi użytkownika
if choice != 'y':
    print('Urzytkownik stwierdził niepoprawnosć scieżki')
    input("Press Enter to continue...")
    exit(0)

# Szukanie plików do usunięcia
for i in os.walk(masterpath):
    print(i)

folders = os.walk('.')
#for i in folders:
#    print(i)