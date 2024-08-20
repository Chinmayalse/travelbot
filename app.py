from flask import Flask, render_template, request, jsonify
from groq import Groq

app = Flask(__name__)

# Initialize the Groq client
client = Groq(api_key='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')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['message']
    
    # Get response from Groq API
    response = get_chat_completion(user_input)
    
    return jsonify({'response': response})

def get_chat_completion(user_input):
    messages = [
        {"role": "system", "content": "Hi welcome to Thirdray. How may I help you today\nPress 1 for Sight seeing in Paris\npress 2 for Paris Olympic 2024 events"},
        {"role": "user", "content": user_input}
    ]
    
    try:
        # Call Groq API to generate the chatbot response
        completion = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=messages,
            max_tokens=500,
            temperature=0.7
        )
        
        # Collect the response
        response_text = completion.choices[0].message['content']
        return response_text

    except Exception as e:
        print(f"Error: {e}")
        return "Sorry, I'm having trouble connecting to the Groq API. Please try again later."

if __name__ == '__main__':
    app.run(debug=True)
