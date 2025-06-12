# 🤖 Real-Time Face Blur with OpenCV DNN

This project detects human faces in real-time using OpenCV's Deep Neural Network (DNN) module and applies a Gaussian blur to those regions. It's useful for protecting privacy in images or webcam video streams.

---

## 📌 Features

- ✅ Real-time face detection using a pre-trained DNN model
- ✅ Gaussian blur applied only to detected face areas
- ✅ Supports both images and webcam streams
- ✅ Lightweight and easy to integrate

---

## 🎥 Demo

Here's a real-time demonstration of the face blur in action:

![Face Blur Demo](demo.gif)

---
## 🖼️ Example Output on Static Image

Here’s the result of applying the face blur function on a sample image:

![Output Static Image](output_static_image.png)

---
## 🧠 How It Works

1. The image is passed through a pre-trained DNN face detector.
2. A binary mask is created for detected face areas.
3. Gaussian blur is applied only to the masked (face) regions.
4. The blurred regions are merged with the original background.

---

## 🛠 Requirements

- Python 3.x
- `opencv-python`
- `numpy`
