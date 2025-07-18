# Real-Time Servo Motor Angle Monitoring System

-->Project Overview

This project demonstrates a complete pipeline that reads the real-time **angle of a servo motor** using Arduino, sends this data to Google Firestore, and displays it dynamically using a Streamlit web app.


-->System Components

1. Arduino Uno + Servo Motor
   - File: `sketch_jul16a.ino`  
   - Function: Reads the current angle of a servo motor and sends it via serial communication.

2. Python Serial to Firestore 
   - File: `2firestore.py`  
   - Function: Continuously reads angle data from Arduino’s serial monitor and pushes it to a Firestore collection.

3. Streamlit App 
   - File: `app.py`  
   - Function: Reads data from Firestore and updates the UI in real-time, displaying the current servo angle.

📂 File Structure

.
├── sketch_jul16a.ino       # Arduino code to control and read the servo motor angle
├── 2firestore.py           # Python script to push serial data to Firestore
├── app.py                  # Streamlit UI app to visualize real-time angle data
└── serviceAccountKey.json  # Firebase Admin SDK credentials (keep this secure)


-->Setup Instructions

1. Arduino

- Connect the servo motor to your Arduino to pin 9.
- Load and run `sketch_jul16a.ino` using the Arduino IDE.
- Ensure the correct COM port is selected.

2. Python (Serial to Firestore)

- Install dependencies:
  ``
  pip install pyserial firebase-admin
  ```
- Make sure `serviceAccountKey.json` is present and correctly linked to your Firebase project.
- Run the script:
  ```
  python 2firestore.py
  ```

3. Streamlit App

- Install dependencies:
  ```
  pip install streamlit firebase-admin
  ```
- Launch the app:
  ```
  streamlit run app.py
  ```
