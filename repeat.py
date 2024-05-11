#在文件夹中，有文件61-70970-0033_leopard16kHz_15dB.wav和61-70970-0033_volvo16kHz_20dB.wav，删掉_leopard16kHz_15dB.wav之后前面都一样，随机选择其中一个删掉#

import os
import random
import re

def get_base_filename(filename):
    return re.sub(r'_.+', '', filename)

# Replace with your actual directory path
dir_path = '/Users/evazhu/Downloads/thesis_noiserobustASR/dataset/LibriSpeech/dev-clean'

# Dictionary to hold the base filenames and the files that match them
base_files = {}

# Populate the dictionary
for filename in os.listdir(dir_path):
    base_filename = get_base_filename(filename)
    if base_filename not in base_files:
        base_files[base_filename] = []
    base_files[base_filename].append(filename)

# Go through the base filenames and randomly delete one if there are duplicates
for base, files in base_files.items():
    if len(files) > 1:
        file_to_delete = random.choice(files)
        os.remove(os.path.join(dir_path, file_to_delete))
        print(f"Deleted file: {file_to_delete}")
