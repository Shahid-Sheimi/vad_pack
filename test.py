import torch
from my_vad import apply_vad

# Example usage
audio_tensor = torch.randn(16000)  # Replace with actual audio tensor
has_speech = apply_vad(audio_tensor)
print(f"Speech detected: {has_speech}")
