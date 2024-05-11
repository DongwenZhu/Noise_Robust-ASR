import os

def rename_and_move_files(source_directory, target_directory):
    # 检查目标文件夹是否存在，如果不存在则创建
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)

    # 遍历源文件夹中的所有文件
    for filename in os.listdir(source_directory):
        if filename.endswith(".wav"):  # 确保只处理.wav文件
            new_name = filename.split('_')[0] + '.wav'  # 获取新文件名
            original_path = os.path.join(source_directory, filename)  # 原文件的完整路径
            new_path = os.path.join(target_directory, new_name)  # 新文件的完整路径
            os.rename(original_path, new_path)  # 移动并重命名文件
            print(f"Moved and renamed '{filename}' to '{new_path}'")

# 使用你的源文件夹和目标文件夹路径替换下面的路径
source_folder_path = '/Users/evazhu/Downloads/thesis_noiserobustASR/final_other_noise/test'
target_folder_path = '/Users/evazhu/Downloads/thesis_noiserobustASR/final_noise_other/test'
rename_and_move_files(source_folder_path, target_folder_path)
