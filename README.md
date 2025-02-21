# Flask Application with /htop Endpoint in GitHub Codespace

## 📌 Project Overview
This repository contains a Flask application deployed in a **GitHub Codespace**, featuring an `/htop` endpoint that displays system details.

## 🚀 Features
- Displays **Name** (Aryan Chhetri)
- Displays **System Username**
- Shows **Current Server Time in IST**
- Returns **Top Command Output** (System usage details)
- Runs on **Port 5000** with **Public Visibility**

## Screenshot
![Image](https://github.com/user-attachments/assets/33cd0b8b-0a60-4955-a541-3331369f1809)

## 🛠️ Setup & Deployment
### **1. Create and Start a Codespace**
1. Go to [GitHub Codespaces](https://github.com/codespaces) and create a new codespace.
2. Set **timeout to 240 minutes** (maximum) in **Codespace Settings**.

### **2. Clone This Repository**
```bash
git clone https://github.com/chhetri-aryan/flask-htop-codespace.git
cd flask-htop-codespace
```

### **3. Install Dependencies**
```bash
pip install flask
```

### **4. Run the Flask Application**
```bash
python app.py
```

### **5. Expose Port 5000 Publicly**
- Open the **Ports tab** in the Codespace.
- Make sure **Port 5000** is **public** (Click the 🌍 globe icon).

### **6. Access the Endpoint**
Go to the following URL in your browser:
```
https://probable-tribble-wxp4p7r69vwf95v9-5000.app.github.dev/htop
```

## 📜 API Endpoint
### **GET /htop**
Returns JSON with the following data:
```json
{
    "Name": "Aryan Chhetri",
    "Username": "system_username",
    "Server Time (IST)": "YYYY-MM-DD HH:MM:SS",
    "Top Output": "<top command output>"
}
```

## 📝 Notes
- The **Codespace must remain running** for the endpoint to be accessible.
- Test in an **incognito tab** before submitting.

## 🔗 Links
- **GitHub Repository**: [https://github.com/chhetri-aryan/flask-htop-codespace](https://github.com/chhetri-aryan/flask-htop-codespace)
- **Live Endpoint**: [https://probable-tribble-wxp4p7r69vwf95v9-5000.app.github.dev/htop](https://probable-tribble-wxp4p7r69vwf95v9-5000.app.github.dev/htop)

## ✅ Status: **Working & Tested!** 🎯
