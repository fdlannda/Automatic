from diffusers import StableDiffusionPipeline
import torch

# Load Stable Diffusion model
model_id = "CompVis/stable-diffusion-v1-4"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda")  # Ganti dengan "cpu" jika tidak ada GPU

# Generate image with a prompt
prompt = "a cyberpunk cityscape, vibrant colors"
image = pipe(prompt).images[0]

# Save the image
image.save("cyberpunk_image.png")
image.show()
