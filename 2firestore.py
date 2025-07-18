import serial
import time
import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase
cred = credentials.Certificate("C:\\Users\\Dell\\SERVO\\serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# Initialize Serial Port
ser = serial.Serial('COM7', 9600, timeout=1)
time.sleep(2)  # Give time for serial connection to stabilize

try:
    while True:
        if ser.in_waiting > 0:
            angle_data = ser.readline().decode().strip()
            if angle_data.isdigit():
                angle_value = int(angle_data)
                
                # Upload to Firestore
                doc_ref = db.collection('servo_data').document('current_angle')
                doc_ref.set({'angle': angle_value})
                
                print(f"Uploaded angle: {angle_value}")
        time.sleep(2)

except KeyboardInterrupt:
    print("Stopped by user.")
    ser.close()
