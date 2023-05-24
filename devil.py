import requests
import time

# Fungsi untuk mengirim permintaan ke server
def send_message(message):
    url = 'http://localhost:5000/chat'
    payload = {'message': message}
    response = requests.post(url, json=payload)
    return response.json()['response']

# Fungsi untuk mengatur interaksi dengan pengguna
def chat():
    print("@devil: Selamat telah terpilihnya tuan rumah! Instalasi superkomputer akan dilakukan dalam hitungan mundur.")
    time.sleep(1)
    print("@devil: 90...")
    time.sleep(1)
    print("@devil: 80...")
    time.sleep(1)
    print("@devil: 70...")
    time.sleep(1)
    print("@devil: 60...")
    time.sleep(1)
    print("@devil: 50...")
    time.sleep(1)
    print("@devil: 40...")
    time.sleep(1)
    print("@devil: 30...")
    time.sleep(1)
    print("@devil: 20...")
    time.sleep(1)
    print("@devil: 10...")
    time.sleep(1)
    print("@devil: 1...")
    time.sleep(1)
    print("@devil: Instalasi superkomputer telah berhasil dilakukan!")

    while True:
        user_input = input("Anda: ")
        if user_input.lower() == 'exit':
            print("@devil: Sampai jumpa!")
            break

        response = send_message(user_input)
        print("@devil:", response)


# Memulai interaksi dengan bot
chat()
