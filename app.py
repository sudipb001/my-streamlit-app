import streamlit as st

st.title("Test App")
st.header("App is updated now")
st.write("Hello, how are you?")

# Access secrets
api_key = st.secrets["api"]["weather_key"]
db_user = st.secrets["database"]["user"]
db_password = st.secrets["database"]["password"]

# Use in your app
st.write(f"Connected as: {db_user}")
# Never display the actual password or API key!
