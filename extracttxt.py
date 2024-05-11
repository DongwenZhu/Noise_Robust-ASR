import os
import shutil

def get_txt_files(source_directory, destination_directory):
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)
        
    for root, dirs, files in os.walk(source_directory):
        for file in files:
            if file.endswith(".txt"):
                txt_file_path = os.path.join(root, file)
                # Make sure the destination directory is different from the source directory
                if root != destination_directory:
                    shutil.copy(txt_file_path, destination_directory)

# Use the corrected source and destination paths
source_dir = 'dataset/LibriSpeech/test-clean_flac'
destination_dir = '/Users/evazhu/Downloads/thesis_noiserobustASR/dataset/LibriSpeech/test_txt' # Make sure this is a new or different directory

get_txt_files(source_dir, destination_dir)
