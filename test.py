import torch
from my_vad.vad import apply_vad

# Example usage
audio_tensor = torch.randn(16000)  # Replace with your audio tensor
result = apply_vad(audio_tensor)
print(f"Speech detected: {result}")
