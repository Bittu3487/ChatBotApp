from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)
CORS(app)

# Set your Gemini API Key here
API_KEY =  os.getenv("SECRET_KEY")
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        message = data.get('message')

        if not message:
            return jsonify({'error': 'No message received'}), 400

        # Start a new conversation (adjust method based on actual library usage)
        conversation = model.start_chat()  # Hypothetical method to start a chat session

        # Send the message to the AI
        ai_response = conversation.send_message(content=message)  # Adjust as per actual method

        # Assuming the response has a 'text' attribute with the AI's reply
        response_text = ai_response.text if ai_response and hasattr(ai_response, 'text') else "Sorry, I didn't understand that."

        return jsonify({'response': response_text})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
