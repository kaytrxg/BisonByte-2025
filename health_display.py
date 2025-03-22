import streamlit as st
from openai import OpenAI  # Import the OpenAI library

# Replace with your actual OpenAI API key
openai_api_key = "LLM.py"  # IMPORTANT: Store this securely, don't hardcode in production

# Initialize the OpenAI client (moved outside the function)
client = OpenAI(api_key = openai_api_key)

if 'buttonState' not in st.session_state:
	st.session_state.buttonState = False

def generate_ai_response(text_input, ai_model="gpt-3.5-turbo"):
    """Generates an AI response using OpenAI's GPT-3.5-turbo or Gemini."""
    if not text_input:
        return "Please enter some text."
    try:
        if ai_model == "gpt-3.5-turbo":
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": text_input},
                ]
            )
            return response.choices[0].message.content
        elif ai_model == "gemini-pro":
            #  Placeholder:  Replace with actual Gemini API call when available
            return "Gemini Pro response placeholder:  " + text_input # Placeholder
            #  Important:  Add the actual Gemini API call here.  This is just a placeholder.
        else:
            return "Invalid AI model selected."
    except Exception as e:
        st.error(f"Error generating AI response: {e}")
        return "Sorry, I'm having trouble connecting to the AI."

def click_button():
    st.session_state.buttonState = True

def submit_request():
	if len(st.session_state.review) > 0:
		st.write("Thank you for your request!")
	else:
		st.write("Please enter more text")



def main():
    st.title("Text Input with AI Response")

    text_input = st.text_area("Enter your text:", height=100)
    ai_model = st.selectbox("Choose AI Model", ["Deep.AI", "Gemini"])  # Added model selection
    
    st.button('Get Response', on_click = click_button)
    if st.session_state.buttonState:
        counter = 0 
        #st.text_input("Enter review", key="review", on_change = submit_request)
        ai_response = generate_ai_response(text_input, ai_model)  # Pass the selected model
        st.subheader("AI Response:")
        st.write(ai_response)



if __name__ == "__main__":
    main()


