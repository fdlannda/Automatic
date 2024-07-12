from PIL import Image, ImageEnhance, ImageFilter
import os

# Direktori gambar yang sudah diunduh
input_dir = "random_profiles"
output_dir = "modified_profiles"

# Membuat direktori output jika belum ada
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Fungsi untuk memodifikasi gambar
def modify_image(image_path, output_path):
    try:
        img = Image.open(image_path)

        # Contoh modifikasi: kontras, ketajaman, dan filter kartun
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(1.5)

        enhancer = ImageEnhance.Sharpness(img)
        img = enhancer.enhance(2.0)

        img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)

        # Simpan gambar yang dimodifikasi
        img.save(output_path)
        print(f"Gambar {output_path} berhasil dimodifikasi")
    except IOError as e:
        print(f"Gagal memodifikasi gambar {image_path}: {e}")

# Memodifikasi semua gambar di direktori input
for filename in os.listdir(input_dir):
    input_path = os.path.join(input_dir, filename)
    output_path = os.path.join(output_dir, filename)
    modify_image(input_path, output_path)

print("Selesai memodifikasi semua gambar.")
