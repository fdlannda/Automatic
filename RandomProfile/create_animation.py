import cv2
import os
import glob

# Direktori gambar yang dimodifikasi
input_dir = "modified_profiles"
output_file = "animation.avi"

# Memuat gambar
images = [cv2.imread(file) for file in glob.glob(f"{input_dir}/*.jpg")]

# Mendefinisikan codec dan membuat objek VideoWriter
fourcc = cv2.VideoWriter_fourcc(*'XVID')
height, width, layers = images[0].shape
video = cv2.VideoWriter(output_file, fourcc, 1.0, (width, height))

# Menulis gambar ke dalam video
for image in images:
    video.write(image)

video.release()
cv2.destroyAllWindows()
print(f"Animasi berhasil disimpan sebagai {output_file}")
