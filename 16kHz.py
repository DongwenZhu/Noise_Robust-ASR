from pydub import AudioSegment
import os

def convert_audio_to_16khz(source_folder, target_folder):
    # 确保目标文件夹存在
    os.makedirs(target_folder, exist_ok=True)

    # 遍历源文件夹中的所有文件
    for filename in os.listdir(source_folder):
        # 支持的文件扩展名
        valid_extensions = (".mp3", ".wav", ".ogg", ".flac", ".m4a")
        if filename.endswith(valid_extensions):
            # 构建完整的文件路径
            filepath = os.path.join(source_folder, filename)
            # 读取音频文件
            audio = AudioSegment.from_file(filepath)
            # 将音频文件的采样率转换为16kHz
            audio = audio.set_frame_rate(16000)
            # 修改文件扩展名为 .wav
            new_filename = os.path.splitext(filename)[0] + ".wav"
            # 构建目标文件路径
            new_filepath = os.path.join(target_folder, new_filename)
            # 导出转换后的音频文件
            audio.export(new_filepath, format="wav")
            
# 使用示例
source_folder = '/Users/evazhu/Downloads/thesis_noiserobustASR/othernoise'  # 将此路径替换为你的音频文件所在的源文件夹路径
target_folder = '/Users/evazhu/Downloads/thesis_noiserobustASR/other_noise'  # 将此路径替换为你想要保存转换后文件的目标文件夹路径
convert_audio_to_16khz(source_folder, target_folder)