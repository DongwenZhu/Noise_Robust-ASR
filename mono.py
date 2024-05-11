from pydub import AudioSegment
import os

# 设置音频文件所在的文件夹路径
audio_folder_path = '/Users/evazhu/Downloads/thesis_noiserobustASR/dataset/other_noise'

# 遍历文件夹中的所有文件
for filename in os.listdir(audio_folder_path):
    if filename.endswith(".wav"):
        file_path = os.path.join(audio_folder_path, filename)
        try:
            # 加载音频文件
            audio = AudioSegment.from_wav(file_path)
            # 转换为单声道
            mono_audio = audio.set_channels(1)
            # 保存转换后的音频文件
            mono_audio.export(file_path, format="wav")
            print(f"Converted {filename} to mono.")
        except Exception as e:
            print(f"Could not process file {filename}: {str(e)}")
