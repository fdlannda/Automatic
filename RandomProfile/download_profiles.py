import os
import requests
from PIL import Image
from io import BytesIO
import time

# Membuat direktori untuk menyimpan foto jika belum ada
save_dir = "random_profiles"
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# Direktori untuk menyimpan data mentah yang tidak valid
invalid_dir = "invalid_profiles"
if not os.path.exists(invalid_dir):
    os.makedirs(invalid_dir)

# Jumlah foto yang ingin diunduh
num_photos = 10

# Mengunduh dan menyimpan foto
for i in range(num_photos):
    try:
        response = requests.get("https://thispersondoesnotexist.com", timeout=20)
        if response.status_code == 200:
            try:
                # Memverifikasi apakah file yang diunduh adalah gambar yang valid
                img = Image.open(BytesIO(response.content))
                img.save(os.path.join(save_dir, f"profile_{i+1}.jpg"))
                print(f"Foto {i+1} berhasil diunduh dan valid")
            except IOError:
                # Jika tidak valid, simpan data mentah untuk debugging
                with open(os.path.join(invalid_dir, f"invalid_{i+1}.jpg"), "wb") as f:
                    f.write(response.content)
                print(f"File yang diunduh untuk foto {i+1} bukan gambar yang valid. Disimpan di {invalid_dir}")
        else:
            print(f"Gagal mengunduh foto {i+1} - Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Terjadi kesalahan saat mengunduh foto {i+1}: {e}")
    # Tambahkan jeda untuk menghindari terlalu banyak permintaan dalam waktu singkat
    time.sleep(1)

print("Selesai mengunduh 100 foto profil acak.")
