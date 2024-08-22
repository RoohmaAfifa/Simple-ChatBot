import streamlit as st
import google.generativeai as genai

# Configure the API key
GOOGLE_API_KEY = "YOUR API KEY"
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize the Generative Model
model = genai.GenerativeModel('gemini-1.5-flash')
# Function to get response from the model
def get_chatbot_response(user_input):
    response = model.generate_content(user_input)
    return response.text

# Streamlit interface
st.set_page_config(page_title="✨Simple ChatBot✨", layout="centered")


# Custom CSS for beautification
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f0f2f6;
        font-family: 'Arial', sans-serif;
    }
    .chat-title {
        text-align: center;
        font-size: 36px;
        color: #4CAF50;
        margin-top: -50px;
    }
    .chat-subtitle {
        text-align: center;
        font-size: 18px;
        color: #555;
        margin-bottom: 20px;
    }
    .chat-box {
        background-color: #fff;
        padding: 10px 20px;
        border-radius: 10px;
        box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    .chat-input-box {
        margin-top: 20px;
    }
    .user-message {
        color: #333;
        font-weight: bold;
        margin-bottom: 5px;
    }
    .bot-message {
        color: #007bff;
        margin-bottom: 20px;
    }
    .stTextInput>div>div>input {
        border-radius: 10px;
        padding: 10px;
        border: 1px solid #ccc;
    }
    .stButton>button {
        border-radius: 10px;
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
        padding: 10px 20px;
        border: none;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title and subtitle
st.markdown("<h1 class='chat-title'>✨Simple ChatBot✨</h1>", unsafe_allow_html=True)
st.markdown("<p class='chat-subtitle'>Powered by Google Generative AI</p>", unsafe_allow_html=True)


if "history" not in st.session_state:
    st.session_state["history"] = []

# Display chat history
for user_message, bot_message in st.session_state.history:
    st.markdown(f"""
    <div style="
        background-color: #d1d3e0;
        border-radius: 15px;
        padding: 10px 15px;
        margin: 5px 0;
        max-width: 70%;
        text-align: left;
        display: inline-block;
    ">
        <p style="margin: 0; font-size: 16px; line-height: 1.5;"><b>You:</b> {user_message} 😊</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div style="
        background-color: #e1ffc7;
        border-radius: 15px;
        padding: 10px 15px;
        margin: 5px 0;
        max-width: 70%;
        text-align: left;
        display: inline-block;
    ">
        <p style="margin: 0; font-size: 16px; line-height: 1.5;"><b>Bot:</b> {bot_message} 🤖</p>
    </div>
    """, unsafe_allow_html=True)

with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("", max_chars=2000)
    submit_button = st.form_submit_button("Send")

    if submit_button:
        if user_input:
            response = get_chatbot_response(user_input)
            st.session_state.history.append((user_input, response))
            # Display the latest response immediately
            st.markdown(
                f"<div class='chat-box'>"
                f"<p class='user-message'>**You:** {user_input}</p>"
                f"<p class='bot-message'>**Bot:** {response}</p>"
                f"</div>", 
                unsafe_allow_html=True
            )
        else:
            st.warning("Please Enter A Prompt")