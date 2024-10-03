from flask import Flask, render_template, request, jsonify, session
from flask_cors import CORS
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)
app.secret_key = os.urandom(24)  # Set a secret key for session

# Set up OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    
    # Get or initialize conversation history
    conversation = session.get('conversation', [])
    conversation.append({"role": "user", "content": user_message})
    
    try:
        # Call OpenAI API with full conversation history
        completion = client.chat.completions.create(
            model="gpt-4-0125-preview",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                *conversation
            ]
        )
        
        bot_message = completion.choices[0].message.content
        conversation.append({"role": "assistant", "content": bot_message})
        
        # Store updated conversation in session
        session['conversation'] = conversation
        
        return jsonify({"message": bot_message})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/reset', methods=['POST'])
def reset_conversation():
    session.pop('conversation', None)
    return jsonify({"message": "Conversation reset successfully"})

if __name__ == '__main__':
    app.run(debug=True)