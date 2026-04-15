# ☕ Smart Coffee Recommender

A simple Machine Learning web app that recommends the best coffee based on the day and time using historical sales data.

---

## 🚀 Overview

This project uses a Random Forest model to analyze past coffee sales and suggest the most suitable coffee for a given time and day.

Instead of random suggestions, the model learns patterns like:
- Morning → Latte ☕
- Afternoon → Americano
- Night → Hot Chocolate

---

## 🧠 Features

- 📅 Select day of the week
- ⏰ Choose time of day (Morning / Afternoon / Night)
- 🤖 ML-based recommendations
- 🔝 Top 3 coffee suggestions with confidence scores
- 🌐 Interactive web app using Streamlit

---

## 🏗️ Project Structure

coffee-recommender/
│
├── app.py # Streamlit frontend
├── train.py # Model training script
├── model/
│ └── pipeline.pkl # Saved model + encoders
├── data/
│ └── coffee.csv # Dataset
└── README.md



---

## ⚙️ Tech Stack

- Python 🐍
- Scikit-learn 🤖
- Pandas 📊
- Streamlit 🌐
- Joblib 💾

---

## 🧪 How It Works

1. Dataset is preprocessed (date & time → features)
2. Features used:
   - Day of week
   - Time of day
3. Model trained using Random Forest
4. Model predicts probability of each coffee
5. Top 3 recommendations are shown

---

## ▶️ How to Run

### 1. Install dependencies

pip install pandas scikit-learn streamlit joblib


### 2. Train the model

python train.py


### 3. Run the app

streamlit run app.py



---

## 📊 Example Output


Input:
Day = Friday
Time = Afternoon

Output:

Latte — 45%
Americano — 30%
Cappuccino — 25%


---

## 🔥 Future Improvements

- 📈 Add sales analytics dashboard
- 🎯 Improve recommendations using more features
- 🌍 Deploy online for public access
- 🤖 Add chatbot interface

---

## 💡 Inspiration

Built as a real-world ML project to simulate how cafes can use data to improve customer experience and sales.

---

## 👨‍💻 Author

**Mohammed Zaid**  
Founder @ HatchUp

---

## ⭐ If you like this project

Give it a star ⭐ and share it!
