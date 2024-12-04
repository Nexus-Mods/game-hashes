import json
import os
import shutil

# Load game name to ID mapping
with open('json/ids.json', 'rb') as f:
    game_mappings = json.load(f)

# Iterate over the directories inside 'json' folder
base_path = 'json'
for game_name in os.listdir(base_path):
    full_path = os.path.join(base_path, game_name)
    if os.path.isdir(full_path) and game_name in game_mappings:
        game_id = str(game_mappings[game_name])
        new_full_path = os.path.join(base_path, game_id)
        shutil.move(full_path, new_full_path)