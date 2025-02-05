import torch
import torchvision.transforms as transforms
from PIL import Image
import cv2
import numpy as np

transformations = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),  
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

image_path = "sample_images/l9_54S_00001.png"
image = Image.open(image_path).convert("RGB")

#image = transforms.functional.pil_to_tensor(image)
tensor = transformations(image)


print(tensor.shape)  # Print shape of the tensor

# Print first 10 elements of the first row for each channel
for i in range(3):
    print(f"Channel {i}:", tensor[i, 0, :20])  

# Print 3x3 region of Channel 0
print("Channel 0:")
for i in range(5):
    for j in range(5):
        print(tensor[0, i, j].item(), end=" ")
    print()