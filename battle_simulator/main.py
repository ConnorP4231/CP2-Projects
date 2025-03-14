# Connor Pavicic, battle_simulator
import csv
from create_character import create_character
from display_csv import display_csv


create_character()

for line in display_csv():
    print(line)