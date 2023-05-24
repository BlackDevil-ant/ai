import cv2
import numpy as np
import requests

# Fungsi untuk mengirim permintaan ke server
def send_message(message):
    url = 'http://localhost:5000/chat'
    payload = {'message': message}
    response = requests.post(url, json=payload)
    return response.json()['response']

# Fungsi untuk memproses citra
def process_image(image):
    # Proses pengolahan citra menggunakan OpenCV
    # Ganti dengan algoritma yang cocok untuk tujuan Anda
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
    edges = cv2.Canny(blurred_image, 50, 150)

    # Kirim hasil citra ke server
    response = send_message('image_processed')
    print('Server Response:', response)

    # Tampilkan citra dan hasil pengolahan
    cv2.imshow('Original Image', image)
    cv2.imshow('Processed Image', edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Fungsi utama
def main():
    # Baca citra dari file
    image = cv2.imread('image.jpg')

    # Proses citra
    process_image(image)

if __name__ == '__main__':
    main()
