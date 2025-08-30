# 📩 Email & SMS Spam Detection  

An end-to-end **Spam Detection System** using **Natural Language Processing (NLP)** and **Machine Learning**.  
This project predicts whether a message is 🚨 **Spam** or ✅ **Ham (Not Spam)**.  

---

## 📥 Dataset  
We use the **SMS Spam Collection Dataset** from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/sms+spam+collection).  

Steps:  
1. Download the dataset and rename it to **`spam.csv`**  
2. Place it in the project root directory  

---

## 🧹 Data Cleaning Steps  

Before training the model, the raw dataset was cleaned using the following steps:  

<details>
<summary>🗑️ Dropping Unnecessary Columns</summary>

- The dataset contains some extra/unnamed columns (like `Unnamed: 2`, `Unnamed: 3`, etc.)  
- We removed all irrelevant columns and kept only:  
  - `v1` → Label (spam/ham)  
  - `v2` → Message  
</details>

<details>
<summary>🧽 Removing Duplicates</summary>

- Duplicate messages were removed to avoid **data leakage** and **bias**.  
</details>

<details>
<summary>✍️ Renaming Columns</summary>

- Renamed:  
  - `v1` → **target**  
  - `v2` → **text**  
</details>

<details>
<summary>🔢 Encoding Labels</summary>

- Converted categorical labels into numbers:  
  - `ham` → **0**  
  - `spam` → **1**  
</details>

---

## ⚙️ Text Preprocessing  

Each message is processed with the following steps:  

- 🔡 Convert to lowercase  
- ✂️ Tokenization  
- 🚫 Remove stopwords & punctuation  
- 🌱 Stemming using **PorterStemmer**  
- 🔢 Convert to numerical features using **TF-IDF Vectorizer**  

---

## 🧠 Model Training  

- 📊 Algorithm → **Multinomial Naive Bayes**  
- 🏗️ Features → TF-IDF (max_features=3000)  
- 🧪 Train/Test Split → 80/20  
- 🎯 Accuracy → ~97% on test data  

The trained model and vectorizer are saved as:  
- `model.pkl`  
- `vectorizer.pkl`  

---

## 🌐 Web Application  

The **Streamlit App** provides an interactive interface:  

- ⌨️ Enter a message  
- 🚀 Get instant prediction (Spam ✅ / Ham 🚨)  
- 📊 Shows prediction probability  
- 🔍 Displays transformed text (optional, for learning/debugging)  

---

## 🛠️ Tech Stack  

- Python 3.x 🐍  
- Streamlit 🌐  
- Pandas & NumPy 📊  
- Scikit-learn 🤖  
- NLTK 📝  
- Pickle 📦  

---

## 📂 Project Structure  

 Email-Spam-Detection

┣ 📄 app.py # Streamlit web app

┣ 📄 train_model.py # Training script

┣ 📄 spam.csv # Dataset (local copy)

┣ 📄 model.pkl # Trained ML model

┣ 📄 vectorizer.pkl # TF-IDF vectorizer

┗ 📄 README.md # Documentation


---

## 🚀 Run Locally  

In Pycharm's treminal run this commands

```bash
# Install streamlit
pip install streamlit

# Run Streamlit App
streamlit run app.py
```

✨ Now you can type a message and instantly check whether it’s spam or ham! 🚨✅
