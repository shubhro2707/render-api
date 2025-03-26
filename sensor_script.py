import requests
import json

URL = "https://render-api-1-8fyn.onrender.com/upload"  # Corrected URL
FILENAME = "sensor_data.json"

def save_sensor_data():
    sensor_data = {"temperature": 22.5, "humidity": 60}
    
    with open(FILENAME, "w") as file:
        json.dump(sensor_data, file)

    print("✅ Data saved to sensor_data.json")

def send_to_server():
    with open(FILENAME, "rb") as file:
        files = {"file": file}
        response = requests.post(URL, files=files)
        print(response.status_code, response.text)  # Print response for debugging

if __name__ == "__main__":
    save_sensor_data()
    send_to_server()
