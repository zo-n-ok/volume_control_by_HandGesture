🎛️ Hand Gesture Volume Control ✋
📌 Description
This project uses computer vision and hand tracking to control your system's volume based on hand gestures. It employs OpenCV, MediaPipe, and the ctypes library for interacting with system volume controls.
The program tracks your hand through the webcam, detecting the distance between your thumb and index fingertip. Based on this distance:

🤏 Close thumb and index finger: Decrease volume
✋ Spread thumb and index finger apart: Increase volume

🌟 Features

🖐️ Real-time hand tracking using MediaPipe.
🔊 Dynamic volume control with hand gestures.
📺 Visual feedback showing volume percentage.
⏳ Safety cooldown to prevent rapid unintended volume changes.

🛠️ Requirements

🐍 Python 3.8 or later
📷 OpenCV (cv2)
🖥️ MediaPipe
🔧 NumPy
🪟 Windows OS (for ctypes volume control)

🔧 Installation


Clone the repository:
git clone https://github.com/zo-n-ok/volume_control_by_HandGesture.git
cd hand-gesture-volume-control



Install required packages:
pip install opencv-python mediapipe numpy



🚀 Usage

Run the script:
python hand_volume_control.py


Ensure your webcam is connected and accessible.
Perform gestures:

🤏 Thumb and index finger close together: Volume down
✋ Thumb and index finger far apart: Volume up


Press 'q' to quit the program.

🔍 Troubleshooting

❗ If the camera doesn’t start, ensure no other applications are using the webcam.
💡 If hand detection fails, ensure good lighting and place your hand clearly in view.
🛠️ The volume control may only work on Windows due to ctypes.windll.user32 usage.

🔮 Future Improvements

🖐️ Add multi-hand support.
💻 Implement cross-platform volume control.
🎯 Fine-tune gesture recognition for smoother control.

📝 License
This project is open-source and available under the MIT License.

🎧 Happy volume controlling! ✋
