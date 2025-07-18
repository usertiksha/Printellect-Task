import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
import time

# Initialize Firebase once
@st.cache_resource
def init_firebase():
    cred = credentials.Certificate("C:\\Users\\Dell\\SERVO\\serviceAccountKey.json")
    firebase_admin.initialize_app(cred)
    return firestore.client()

db = init_firebase()

st.title("🔁 Real-Time Servo Angle Monitor")

# Display area
angle_display = st.empty()

# Continuously fetch and display updated angle
doc_ref = db.collection('servo_data').document('current_angle')

# Fetch and display data, auto-refreshing every 2 seconds
while True:
    doc = doc_ref.get()
    if doc.exists:
        angle = doc.to_dict().get('angle', 'N/A')
        angle_display.markdown(f"### 🧭 Current Angle: **{angle}°**")
    else:
        angle_display.markdown("### ❌ No angle data found.")

    time.sleep(2)
    
