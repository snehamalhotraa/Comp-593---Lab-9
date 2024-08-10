"""
Authors: Mahenur Master, Nisharg Patel, Sneha Malhotra, Siddharth Patel

Description: 
  Graphical user interface that displays specific details about a 
  user-entered Pokémon fetched from the PokeAPI 

Usage:
  python poke_info_viewer.py
"""
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from poke_api import get_pokemon_info

# Create the main window
window = Tk()
window.title("Pokémon Information")
window.resizable(False, False)

# Create the frames
input_frame = ttk.Frame(window)
input_frame.grid(row=0, column=0, columnspan=2, pady=(20,10))

# Frame for displaying Pokémon info
info_frame = ttk.LabelFrame(window, text="Pokémon Details")
info_frame.grid(row=1, column=0, padx=(20,10), pady=(10,20), sticky=N)

# Frame for Pokémon stats
stats_frame = ttk.LabelFrame(window, text="Stats")
stats_frame.grid(row=1, column=1, padx=(10,20), pady=(10,20), sticky=N)

# Populate the input frame with widgets
name_label = ttk.Label(input_frame, text="Pokémon Name:")
name_label.grid(row=0, column=0, padx=(10,5), pady=10)

name_entry = ttk.Entry(input_frame)
name_entry.insert(0, "Diglett")
name_entry.grid(row=0, column=1)

def fetch_pokemon_data():
    pokemon_name = name_entry.get().strip()
    if not pokemon_name:
        return
    pokemon_data = get_pokemon_info(pokemon_name)
    if pokemon_data:
        height_label_value['text'] = f"{pokemon_data['height']} dm"
        weight_label_value['text'] = f"{pokemon_data['weight']} hg"
        types = [t['type']['name'].capitalize() for t in pokemon_data['types']]
        
        # Update stats
        type_label_value['text'] = ', '.join(types)
        hp_progress['value'] = pokemon_data['stats'][0]['base_stat']
        attack_progress['value'] = pokemon_data['stats'][1]['base_stat']
        defense_progress['value'] = pokemon_data['stats'][2]['base_stat']
        special_attack_progress['value'] = pokemon_data['stats'][3]['base_stat']
        special_defense_progress['value'] = pokemon_data['stats'][4]['base_stat']
        speed_progress['value'] = pokemon_data['stats'][5]['base_stat']
    else:
        messagebox.showerror('Error', f'Failed to retrieve data for {pokemon_name} from the PokeAPI.')

fetch_button = ttk.Button(input_frame, text='Fetch Details', command=fetch_pokemon_data)
fetch_button.grid(row=0, column=2, padx=10, pady=10)

# Populate the info frame with widgets
height_label = ttk.Label(info_frame, text="Height: ")
height_label.grid(row=0, column=0, padx=(10,5), pady=(10,5), sticky=E)
height_label_value = ttk.Label(info_frame, width=20)
height_label_value.grid(row=0, column=1, padx=(0,10), pady=(10,5), sticky=W)

weight_label = ttk.Label(info_frame, text='Weight:')
weight_label.grid(row=1, column=0, padx=(10,5), pady=(10,5), sticky=E)
weight_label_value = ttk.Label(info_frame, width=20)
weight_label_value.grid(row=1, column=1, padx=(0,10), pady=(10,5), sticky=W)

type_label = ttk.Label(info_frame, text='Type:')
type_label.grid(row=2, column=0, padx=(10,5), pady=(10,5), sticky=E)
type_label_value = ttk.Label(info_frame, width=20)
type_label_value.grid(row=2, column=1, padx=(0,10), pady=(10,5), sticky=W)

# Populate the stats frame with widgets
MAX_STAT_VALUE = 255.0
PROGRESS_BAR_LENGTH = 200

hp_label = ttk.Label(stats_frame, text="HP:")
hp_label.grid(row=0, column=0, padx=(10,5), pady=(10,5), sticky=E)
hp_progress = ttk.Progressbar(stats_frame, length=PROGRESS_BAR_LENGTH, maximum=MAX_STAT_VALUE)
hp_progress.grid(row=0, column=1, padx=(0,10), pady=(10,5))

attack_label = ttk.Label(stats_frame, text="Attack:")
attack_label.grid(row=1, column=0, padx=(10,5), pady=5, sticky=E)
attack_progress = ttk.Progressbar(stats_frame, length=PROGRESS_BAR_LENGTH, maximum=MAX_STAT_VALUE)
attack_progress.grid(row=1, column=1, padx=(0,10), pady=5)

defense_label = ttk.Label(stats_frame, text="Defense:")
defense_label.grid(row=2, column=0, padx=(10,5), pady=5, sticky=E)
defense_progress = ttk.Progressbar(stats_frame, length=PROGRESS_BAR_LENGTH, maximum=MAX_STAT_VALUE)
defense_progress.grid(row=2, column=1, padx=(0,10), pady=5)

special_attack_label = ttk.Label(stats_frame, text="Special Attack:")
special_attack_label.grid(row=3, column=0, padx=(10,5), pady=5, sticky=E)
special_attack_progress = ttk.Progressbar(stats_frame, length=PROGRESS_BAR_LENGTH, maximum=MAX_STAT_VALUE)
special_attack_progress.grid(row=3, column=1, padx=(0,10), pady=5)

special_defense_label = ttk.Label(stats_frame, text="Special Defense:")
special_defense_label.grid(row=4, column=0, padx=(10,5), pady=5, sticky=E)
special_defense_progress = ttk.Progressbar(stats_frame, length=PROGRESS_BAR_LENGTH, maximum=MAX_STAT_VALUE)
special_defense_progress.grid(row=4, column=1, padx=(0,10), pady=5)

speed_label = ttk.Label(stats_frame, text="Speed:")
speed_label.grid(row=5, column=0, padx=(10,5), pady=5, sticky=E)
speed_progress = ttk.Progressbar(stats_frame, length=PROGRESS_BAR_LENGTH, maximum=MAX_STAT_VALUE)
speed_progress.grid(row=5, column=1, padx=(0,10), pady=5)

window.mainloop()
