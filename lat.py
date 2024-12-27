import streamlit as st
import os
import textwrap
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Custom styling and page configuration
st.set_page_config(
    page_title="LOTUS MIND: Wellness Companion",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Enhanced custom CSS for mental wellness theme
st.markdown("""
    <style>
    /* Global Styling */
    body {
        background: linear-gradient(135deg, #f6f9fc 0%, #e9f0f7 100%);
        font-family: 'Nunito', 'Arial', sans-serif;
    }

    /* Header Styling with Gentle Animation */
    .main-header {
        color: #2c3e50;
        font-family: 'Quicksand', sans-serif;
        text-align: center;
        padding: 30px;
        background: linear-gradient(to right, #a1c4fd 0%, #c2e9fb 100%);
        border-radius: 15px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        animation: headerPulse 3s infinite alternate;
        position: relative;
        overflow: hidden;
    }

    @keyframes headerPulse {
        0% { transform: scale(1); }
        100% { transform: scale(1.02); }
    }

    .main-header::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(255,255,255,0.2) 0%, transparent 70%);
        animation: shine 5s infinite linear;
    }

    @keyframes shine {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }

    /* Input Styling with Soft Glow */
    .stTextInput > div > div > input {
        border: 2px solid #6a9efd;
        border-radius: 15px;
        padding: 15px;
        font-size: 16px;
        background-color: rgba(255,255,255,0.7);
        box-shadow: 0 4px 6px rgba(106, 158, 253, 0.1);
        transition: all 0.3s ease;
    }

    .stTextInput > div > div > input:focus {
        border-color: #4a90e2;
        box-shadow: 0 0 15px rgba(74, 144, 226, 0.3);
    }

    /* Button Styling with Soft Hover Effects */
    .stButton > button {
        background: linear-gradient(to right, #56ccf2, #2f80ed);
        color: white;
        border-radius: 15px;
        padding: 12px 25px;
        font-weight: bold;
        border: none;
        transition: all 0.4s ease;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    .stButton > button:hover {
        background: linear-gradient(to right, #2f80ed, #56ccf2);
        transform: translateY(-3px);
        box-shadow: 0 7px 14px rgba(50, 50, 93, 0.1), 0 3px 6px rgba(0, 0, 0, 0.08);
    }

    /* Response Box Styling - Removed default Streamlit white bar */
    .response-box {
        background: linear-gradient(135deg, #ffffff 0%, #f1f5f9 100%);
        border-radius: 15px;
        padding: 25px;
        margin-top: 20px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.05);
        border-left: 5px solid #4a90e2;
        animation: fadeIn 0.5s ease;
    }

    /* Remove white bar in response section */
    .stMarkdown {
        margin: 0 !important;
        padding: 0 !important;
    }

    .stMarkdown > div {
        margin: 0 !important;
        padding: 0 !important;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* Sidebar Styling */
    .css-1aumxhk {
        background: linear-gradient(135deg, #f5f7fa 0%, #e9ecef 100%);
        border-radius: 15px;
        padding: 20px;
    }

    /* Engagement Indicators */
    .engagement-indicator {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: 20px;
    }

    .engagement-dot {
        width: 10px;
        height: 10px;
        background-color: #4a90e2;
        border-radius: 50%;
        margin: 0 5px;
        animation: pulse 1.5s infinite alternate;
    }

    @keyframes pulse {
        0% { transform: scale(0.7); opacity: 0.6; }
        100% { transform: scale(1); opacity: 1; }
    }
    </style>
    """, unsafe_allow_html=True)

def get_gemini_response(question):
    """
    Generate response using Gemini Pro model with mental wellness context
    
    Args:
        question (str): User's input question
    
    Returns:
        str: Generated response from Gemini
    """
    try:
        model = genai.GenerativeModel('gemini-pro')
        wellness_context = f"Respond to the following question with empathy, understanding, and a focus on mental wellness: {question}"
        response = model.generate_content(wellness_context)
        return response.text
    except Exception as e:
        return f"🌸 I sense something isn't quite right. Let's take a deep breath: {str(e)}"

def main():
    # Header with enhanced styling and mindfulness theme
    st.markdown(
        '<h1 class="main-header">🌸 LOTUS MIND: Your Wellness Companion 🧠</h1>', 
        unsafe_allow_html=True
    )
    
    # Sidebar with more compassionate information
    st.sidebar.title("About LOTUS MIND")
    st.sidebar.info(
        "LOTUS MIND is a compassionate AI companion designed to support your "
        "mental wellness journey. Our goal is to listen, understand, and "
        "provide gentle, supportive guidance tailored to your unique needs."
    )
    
    # Wellness quote section
    st.sidebar.markdown("### 💭 Daily Wellness Reflection")
    wellness_quotes = [
        "Breathe. Let go. Remember that this very moment is the only one you know you have for sure.",
        "Your mind is a garden. Your thoughts are the seeds. You can grow flowers or you can grow weeds.",
        "Be gentle with yourself. You're doing the best you can."
    ]
    import random
    st.sidebar.markdown(f"*{random.choice(wellness_quotes)}*")
    
    # Input area with mindful placeholder
    input_question = st.text_input(
        "What's on your mind today?", 
        key="input", 
        placeholder="Share your thoughts, concerns, or questions..."
    )
    
    # Submit button
    if st.button("Seek Compassionate Insight 🌿"):
        if input_question.strip():
            # Mindful loading spinner
            with st.spinner('Cultivating a thoughtful response...'):
                response = get_gemini_response(input_question)
            
            # Display response with gentle styling
            st.markdown('<div class="response-box">', unsafe_allow_html=True)
            st.markdown("### 💡 Insights for Your Wellness")
            st.write(response)
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Engagement indicator
            st.markdown(
                '<div class="engagement-indicator">' +
                '<div class="engagement-dot"></div>' * 3 +
                '</div>', 
                unsafe_allow_html=True
            )
        else:
            st.warning("Your thoughts matter. Please share something with me.")

if __name__ == "__main__":
    main()