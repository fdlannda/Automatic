import os
import requests
from PIL import Image
from io import BytesIO
import torch
from transformers import VQGanTokenizer, VQGanModel
from torchvision import transforms

# Direktori untuk menyimpan gambar yang dihasilkan
save_dir = "generated_images"
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# Load VQ-VAE-2 model and tokenizer
model = VQGanModel.from_pretrained("CompVis/vqgan-f16-16384")
tokenizer = VQGanTokenizer.from_pretrained("CompVis/vqgan-f16-16384")

def download_image(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content)).convert("RGB")
    return img

def transform_image_vqvae(image, model, tokenizer):
    inputs = tokenizer(images=image, return_tensors="pt")
    outputs = model.generate(**inputs)
    generated_image = outputs.pixel_values[0]
    generated_image = (generated_image * 255).byte()
    generated_image = generated_image.permute(1, 2, 0).cpu().numpy()
    generated_image = Image.fromarray(generated_image)
    return generated_image

def generate_image_stylegan(seed):
    stylegan_model = torch.hub.load('facebookresearch/pytorch_GAN_zoo:hub', 'PGAN', model_name='celebAHQ-512', pretrained=True, useGPU=False)
    torch.manual_seed(seed)
    noise, _ = stylegan_model.buildNoiseData(1)
    with torch.no_grad():
        generated_images = stylegan_model.test(noise)
    img = transforms.ToPILImage()(generated_images[0].cpu())
    return img

# URL gambar acak
image_url = "https://thispersondoesnotexist.com/image"

# Unduh dan ubah 100 gambar
for i in range(100):
    try:
        img = download_image(image_url)
        # Transformasi menggunakan VQ-VAE-2
        transformed_image = transform_image_vqvae(img, model, tokenizer)
        transformed_image.save(os.path.join(save_dir, f"vqvae_{i+1}.jpg"))

        # Transformasi menggunakan StyleGAN
        generated_image = generate_image_stylegan(i)
        generated_image.save(os.path.join(save_dir, f"stylegan_{i+1}.jpg"))

        print(f"Gambar {i+1} berhasil diunduh dan diubah.")
    except Exception as e:
        print(f"Gagal mengunduh atau mengubah gambar {i+1}: {e}")

print("Selesai mengunduh dan mengubah 100 gambar.")
