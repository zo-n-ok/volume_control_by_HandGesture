🖐️ Hand Gesture Controlled Volume and Servo Motor
This project uses a Python script with OpenCV and MediaPipe to track hand gestures and control system volume. It also integrates Arduino to move a servo motor based on detected gestures.
✨ Features

🖐️ Hand gesture detection using Python (OpenCV + MediaPipe)
🔊 Volume control by pinching thumb and index finger
🔧 Arduino Uno controls a servo motor based on hand gesture detection

🔧 Requirements
🐍 Python Environment

Python 3.7 or later
OpenCV 📸
MediaPipe 🤚
NumPy 🔢
PySerial 🔌

Install requirements using:
pip install opencv-python mediapipe numpy pyserial

🛠️ Arduino Setup

🛠️ Arduino Uno
🔄 Servo motor
🔌 USB cable
💡 Arduino IDE

🛠️ Setup
🖥️ Python Script Setup


Clone the repository:
git clone https://github.com/zo-n-ok/volume_control_by_HandGesture.git
cd HandGestureVolumeServo



Run the Python script:
python hand_tracker.py



🔧 Arduino Setup

Open Arduino IDE and upload the Arduino script (e.g., servo_control.ino).
Select the correct board and port in Tools > Board and Tools > Port.
Upload the code to the Arduino Uno.

🎯 Usage

🔊 Volume Up: Pinch thumb and index finger apart.
🔉 Volume Down: Bring thumb and index finger close.
🔄 Servo Control: The Arduino script reads signals from the Python script to rotate the servo motor based on gesture detection.

🛠️ Troubleshooting

✅ Ensure the correct COM port is selected in both Python and Arduino.
🎥 If the camera doesn't start, check your webcam permissions.
🔄 If the servo doesn’t move, verify Arduino connections and script upload.

📄 License
This project is open-source under the MIT License.
Happy coding! 🚀
