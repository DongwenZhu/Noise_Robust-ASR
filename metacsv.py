import pandas as pd

# Load the CSV file to examine its contents
file_path = '/Users/evazhu/Downloads/thesis_noiserobustASR/dataset/LibriSpeech/metadata.csv'
data = pd.read_csv(file_path)

# Replace "dev-clean" with "train" and "test-clean" with "test" in the file_name column
# Add regex=True to clarify that these are not regular expressions, and to handle future warnings
data['file_name'] = data['file_name'].str.replace('dev-clean', 'train', regex=False)
data['file_name'] = data['file_name'].str.replace('test-clean', 'test', regex=False)

# Display the first few rows of the dataframe to understand its structure and save the file
data.head(), data.columns

# Optionally save the modified dataframe back to a file
output_path = '/Users/evazhu/Downloads/thesis_noiserobustASR/dataset/LibriSpeech/1metadata.csv'
data.to_csv(output_path, index=False)
