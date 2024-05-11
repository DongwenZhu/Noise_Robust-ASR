import glob
import pandas as pd
from datasets import load_dataset, Audio
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
import torch
from jiwer import wer, cer

datasetpath_list = ["final_no_noise/"]
modelpath_list = ["MODEL_libricarnoise_other/checkpoint-10000"]

for dataset_path in datasetpath_list:
    dataset = load_dataset("audiofolder", data_dir=dataset_path)
    for model_path in modelpath_list:
        model = Wav2Vec2ForCTC.from_pretrained(model_path).to("cuda")
        processor = Wav2Vec2Processor.from_pretrained(model_path)

        def map_to_pred(batch):
            input_values = processor(batch["audio"][0]["array"], return_tensors="pt", padding="longest", sampling_rate=16000).input_values
            logits = model(input_values.to("cuda")).logits
            predicted_ids = torch.argmax(logits, dim=-1)
            batch["predicted_text"] = processor.batch_decode(predicted_ids)
            return batch

        result = dataset.map(map_to_pred, batched=True, batch_size=1, remove_columns=["audio"])

        rows = [{
            "Transcription": trans.strip(),
            "Predicted Text": text.strip()
        } for trans, text in zip(result["test"]["transcription"], result["test"]["predicted_text"]) if trans.strip() and text.strip()]

        if rows:
            df = pd.DataFrame(rows)

            transcription_list = df["Transcription"].tolist()
            predicted_text_list = df["Predicted Text"].tolist()

            wer_score = wer(predicted_text_list, transcription_list)
            cer_score = cer(predicted_text_list, transcription_list)
            print(f"WER: {wer_score}, CER: {cer_score} on dataset {dataset_path} using model {model_path}")
            
            # 构建CSV文件的保存路径
            csv_path = dataset_path.rstrip("/") + "/" + f"transcription_results_{model_path.replace('/', '_')}.csv"
            df.to_csv(csv_path, index=False)
            print(f"Results saved to {csv_path}")
        else:
            print(f"No valid data to calculate WER/CER or save to CSV on dataset {dataset_path} using model {model_path}.")


print("WER:", wer_score)
print("CER:", cer_score)
