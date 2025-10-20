# 🧠 Smart Edge-to-Cloud Motion Detection Framework

## 📘 Overview
The **Smart Edge-to-Cloud Motion Detection Framework** is an IoT-based intelligent surveillance system that combines **edge computing** and **cloud analytics** to achieve real-time motion detection, reduced bandwidth usage, and enhanced privacy.  
This hybrid model leverages **Raspberry Pi**, **NodeMCU**, and **PIR sensors** at the edge for quick local processing and integrates with a **Flask-based cloud dashboard** for centralized monitoring and data analytics.

---

## 🚀 Key Features
- ⚡ **Hybrid Architecture:** Combines edge and cloud computing for optimal performance.  
- 🎯 **Real-Time Motion Detection:** Achieves sub-300 ms latency using edge processing.  
- 🌐 **Bandwidth Optimization:** Transmits only relevant motion events (up to 70 % reduction).  
- 🔒 **Privacy Protection:** Sensitive video data processed locally at the edge.  
- 🤖 **High Accuracy:** 95 % detection accuracy with < 5 % false alarms.  
- 📊 **Flask Dashboard:** Real-time monitoring and analytics.  
- 🔧 **Modular Design:** Scalable and cost-efficient for IoT and industrial use.

---

## 🧩 System Architecture
**Edge Layer:**
- PIR Sensors detect motion (heat-based changes).  
- NodeMCU handles motion signal processing and data transfer.  
- Raspberry Pi processes visual data using Pi Camera and TensorFlow Lite.  

**Cloud Layer:**
- Flask server hosted locally or on Anaconda Cloud.  
- Real-time dashboard for visualization and control.  
- Centralized data analytics and storage.  

**Communication Protocols:**
- **MQTT** – Event notification and command distribution.  
- **HTTP/HTTPS** – Secure high-bandwidth data transfer.

---

## 🛠️ Hardware Requirements
- Raspberry Pi 3 Model B / 4  
- Pi Camera Module V2  
- NodeMCU (ESP8266 / ESP32)  
- PIR Motion Sensors × 2  
- Connecting Cables (M-M, F-F, M-F)  
- 5 V Power Supply  

---

## 💻 Software Requirements
| Component | Description |
|------------|-------------|
| **OS** | Raspberry Pi OS (32-bit recommended) |
| **IDE** | Arduino IDE (for NodeMCU), Python (for Pi) |
| **Cloud** | Anaconda Cloud / Local Flask Server |
| **Languages** | Python, C/C++ |
| **Libraries** | Flask, OpenCV, TensorFlow Lite, NumPy, psutil, requests |

---

## 📦 Installation

### 1. Setup Raspberry Pi
```bash
sudo apt update && sudo apt upgrade
sudo apt install python3-pip
```

### 2. Install Dependencies
Create a `requirements.txt`:
```
flask
opencv-python
numpy
tensorflow
psutil
requests
```
Then install:
```bash
pip3 install -r requirements.txt
```

### 3. Run Flask Server
```bash
python3 app.py
```

### 4. Deploy NodeMCU Code
- Open Arduino IDE  
- Select correct **Board** and **Port** under *Tools → Board/Port*  
- Verify and upload the code  

---

## 🧠 Working Methodology
1. **Detection:** PIR sensors detect movement.  
2. **Trigger:** NodeMCU notifies Raspberry Pi.  
3. **AI Inference:** Pi Camera captures image/video and TensorFlow Lite filters true events.  
4. **Transmission:** Only verified data sent to the cloud dashboard.  
5. **Monitoring:** Flask dashboard displays live feed and logs events in real time.  

---

## 📊 Results
- ⏱️ Latency < 300 ms  
- 📉 Bandwidth usage reduced by ≈ 70 %  
- ✅ Detection accuracy ≈ 95 %  
- 🔒 Enhanced privacy through edge processing  

---

## 🔮 Future Enhancements
- AI-based **anomaly detection** and behavior analysis.  
- Integration with **multi-sensor fusion** and environmental data.  
- **Mobile app notifications** for motion events.  
- Advanced **encryption and access control** for IoT security.  

---

## 🧾 References
1. Stauffer & Grimson (1999) – Adaptive Background Models  
2. Zhang et al. (2017) – Cloud-Based Video Surveillance  
3. Chen et al. (2019) – CNN-Based Motion Detection  
4. Li et al. (2022) – EdgeSense Motion Detection  
5. Flask Docs – https://flask.palletsprojects.com  
6. TensorFlow Lite – https://www.tensorflow.org/lite  
7. MQTT Protocol – https://mqtt.org  

---

## 👨‍💻 Author
**Goshike Aaditya**  
*Project:* Smart Edge-to-Cloud Motion Detection Framework  
*Technologies:* IoT • Edge Computing • Cloud Integration • AI • Flask • TensorFlow Lite  

---

## ⚖️ License
This project is licensed under the **MIT License** — you’re free to use, modify, and distribute it with attribution.  

```
MIT License

Copyright (c) 2025 Shravya Vasa

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
