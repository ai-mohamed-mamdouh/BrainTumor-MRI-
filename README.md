# Brain Tumor MRI Classification 


## 🧠 Overview

The **Brain Tumor MRI Classification** project is an AI-powered system designed to assist patients and doctors in **quick and accurate diagnosis** of brain tumor MRI scans. The model is capable of classifying MRI images into different tumor categories and provides:

* Tumor name
* Confidence score
* Description of the disease
* Medical impact of the tumor

## 📂 Dataset

The dataset was obtained from **Kaggle**.

* **Training images:** 5712 (4 classes)
* **Testing images:** 1311 (4 classes)
* Images were organized by storing paths and labels in a **DataFrame**, then loaded using **ImageDataGenerator**.


## 🧠 Model Architecture

The model uses **Transfer Learning**:

* **VGG16** as a feature extractor
* Custom **DNN** classifier layers on top


**Technologies Used:**

* Python
* TensorFlow, Keras

## 📈 Evaluation Metrics

The model was evaluated using:

* Accuracy
* F1-score
* Classification Report
* Confusion Matrix
* ROC Curve & AUC



## ⚙️ Features

✔ Upload MRI image through a Flask web interface
✔ Model returns:

* Tumor type
* Confidence percentage
* Description of tumor
* Medical implications
  ✔ Built using **Flask**

## 🛠️ Tech Stack

* **Python**
* **TensorFlow 2.18.0**
* **Keras**
* **NumPy 1.26.4**
* **Pillow 10.3.0**
* **Flask 3.0.3**

## 📦 Installation & Running the Project

Follow these steps to run the application:

```bash
# 1️⃣ Create virtual environment
python -m venv .venv

# 2️⃣ Activate the environment
# Windows
".venv\Scripts\activate"
# Linux / MacOS
source .venv/bin/activate

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Run the Flask app
python app.py
```

After running the app, a local website will open. Upload an MRI image and the model will display the results.

## 📁 Project Structure

```
BrainTumorMRIProject/
│── app.py
│── model_Ai_dir/
│── requirements.txt
│── templates/
│── imagesForTest/
│── uploads/
└── README.md
└── .venv
```



## ✨ Author

**Mohamed Mamdouh** – Project creator.
<br>**Student at the Faculty of** Artificial Intelligence, Menoufia University, **Machine Intelligence** Department

## Connect with me on

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?logo=linkedin)](https://www.linkedin.com/in/ai-mohamed-mamdouh-74043b331/)

---

