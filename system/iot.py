import paho.mqtt.client as mqtt
import requests
from coapthon.client.helperclient import HelperClient
import websocket

# MQTT
def on_connect(client, userdata, flags, rc):
    print("Terhubung ke broker MQTT")
    client.subscribe("iot_topic")

def on_message(client, userdata, msg):
    print("Menerima pesan: " + msg.payload.decode())

mqtt_client = mqtt.Client()
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message
mqtt_client.connect("mqtt.broker.com", 1883, 60)
mqtt_client.loop_start()

# REST API
def send_rest_request():
    url = "https://api.example.com/endpoint"
    payload = {"sensor_value": 10}
    response = requests.post(url, json=payload)
    print("Respons dari REST API:", response.text)

send_rest_request()

# CoAP
def send_coap_request():
    client = HelperClient(server=("http://localhost:5000/chat", 5683))
    response = client.post("endpoint", "Hello CoAP")
    print("Respons dari CoAP:", response.payload)

send_coap_request()

# WebSockets
def on_message(ws, message):
    print("Menerima pesan dari WebSocket:", message)

websocket.enableTrace(True)
ws = websocket.WebSocketApp("ws://example.com/endpoint",
                            on_message=on_message)
ws.run_forever()
