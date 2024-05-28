Below is a list of all relevant scripts used for creating the thesis above.
- `PublicOtherNoise` - The noise data I used in this thesis.
- `16KHz.py` and `mono.py` - Used for resampling the noises to 16KHz and mono channel.
- `mix_noisespeech_difflen_SNR.py` - Used for mixing speech files with noise, when noise and speech files have different lengths. Multiple different SNRs are set.
- `repeat.py` - Used for checking and removing the same speech recording to avoid repeating mix with noise file.
- `extracttxt.py` - Used for getting the speech transcriptions.
- `create_metadata.py` - Used for creating a metadata file with transcriptions in the correctly readable format for transformers, in order to make the dataset complete.
- `metacsv.py`- Used for unifying the format of the metadata.csv.
- `finetune.py` - Used for fine-tuning wav2vec 2.0 on any dataset in the right format.
- `eval.py` - Used for evaluating ASR model performance: calculating the WER and CER.
