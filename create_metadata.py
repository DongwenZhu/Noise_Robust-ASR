# This script contains a metadata.csv containing audio file names with corresponding transcriptions, for LibriSpeech files.
# Output format: file_name,transcription
# EXAMPLE output line: data/first_audio_file.mp3,znowu się duch z ciałem zrośnie w młodocianej

# REQUIREMENTS:
# dir containing:
#    train/     containing audio files containing LibriSpeech file code in filename (from dev-clean)
#    test/      containing audio files containing LibriSpeech file code in filename (from test-clean)

# remember to cd dataset or will get error FileNotFoundError: [Errno 2] No such file or directory

import glob
import re

audiofolderpath = "/Users/evazhu/Downloads/thesis_noiserobustASR/dataset/LibriSpeech"

mixed_noisyspeech_list = glob.glob(fr"{audiofolderpath}/**/*.wav", recursive="True") 
print(mixed_noisyspeech_list[:5])

pattern_speakerID = r'(\d+)-\d+-\d+'
pattern_chapterID = r'-(\d+)-'
pattern_utteranceID = r'\d+-\d+-(\d+)'
pattern_filename = r'(\d+-\d+)-'
pattern_testtrain = r'\/([a-z]+)\/'

with open(f'{audiofolderpath}/metadata.csv', 'w') as metadata_file:
    metadata_file.write("file_name,transcription\n")
    for item in mixed_noisyspeech_list:
        speakerID = re.findall(pattern_speakerID, item)[0]
        chapterID = re.findall(pattern_chapterID, item)[0]
        filename = re.findall(pattern_filename, item)[0]

         # Determine the directory to use for the transcription file
        if len(re.findall(r'[a-z]+-clean', item)) != 0:
            testtrain = re.findall(r'[a-z]+-clean', item)[0].replace('clean', 'txt')
        elif re.findall(pattern_testtrain, item)[0] == 'train':
            testtrain = 'dev-txt'
        elif re.findall(pattern_testtrain, item)[0] == 'test':
            testtrain = 'test-txt'
        filepath = item.removeprefix(f'{audiofolderpath}/')

        utteranceID = re.findall(pattern_utteranceID, item)[0]
        uttIDX = utteranceID.lstrip("0")
        if uttIDX == '':
            uttIDX = '0'
        uttIDX = int(uttIDX)

        with open(f"LibriSpeech/{testtrain}/{filename}.trans.txt", 'r') as transcription_file:
            transcription_file_list = transcription_file.readlines()
            
            code_utterance = transcription_file_list[uttIDX]

            transcription = re.findall(r'\d+-\d+-\d+\s(.*)', transcription_file_list[uttIDX])[0]

          
            metadata_file.write(f"{filepath},{transcription}\n")
