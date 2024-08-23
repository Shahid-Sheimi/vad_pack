# my_vad/vad.py

import torch

def apply_vad(audio_tensor, vad_threshold=0.4):
    model, utils = torch.hub.load(
        repo_or_dir="snakers4/silero-vad", model="silero_vad", onnx=False
    )
    (get_speech_timestamps, _, _, _, _) = utils
    speech_timestamps = get_speech_timestamps(audio_tensor, model, sampling_rate=16000, threshold=vad_threshold)
    return len(speech_timestamps) > 0
