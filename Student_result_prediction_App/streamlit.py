import streamlit as st
import joblib

st.set_page_config(page_title="Marks Prediction App", page_icon="📚", layout="centered")

# Purple Theme CSS
st.markdown("""
<style>

[data-testid="stAppViewContainer"]{
background: linear-gradient(135deg, #f3e7ff, #e0c3fc);
}

h1{
color:#5A189A;
text-align:center;
}

.stButton>button{
background-color:#7B2CBF;
color:white;
font-size:18px;
border-radius:10px;
padding:10px;
border:none;
}

.stButton>button:hover{
background-color:#5A189A;
color:white;
}

</style>
""", unsafe_allow_html=True)

# Load model
model = joblib.load("hours_pass_model.pkl")

st.title("📚 Student Result Prediction App")
st.write("Enter number of hours studied:")

hours = st.number_input("Hours Studied", min_value=0.0, step=0.5)

if st.button("Predict Result"):
    prediction = model.predict([[hours]])

    if prediction[0] == 1:
        st.success("✅ Student will PASS 🎉")
    else:
        st.error("❌ Student will FAIL 📉")