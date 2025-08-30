import streamlit as st
import pickle
import string
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
from nltk.corpus import stopwords
nltk.download('stopwords')
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()


def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

with open('vectorizer.pkl', 'rb') as f:
    tf = pickle.load(f)

with open('model (1).pkl', 'rb') as m:
    model = pickle.load(m)

st.title('Spam Detection ')

input_msg = st.text_input("Enter the message")

if st.button('Predict'):
    # Steps to follow:
    # 1. Preprocess
    transformed_msg = transform_text(input_msg)

    # 2. Vectorize
    vector_input = tf.transform([transformed_msg])

    # 3. Predict
    result = model.predict(vector_input)[0]
    prob = model.predict_proba(vector_input)[0][result]

    # 4. Display
    if result == 1:
        st.header("🚨 Spam Mail")
    else:
        st.header("✅ Ham Mail")

    st.subheader(f"Confidence: {prob * 100:.2f}%")
