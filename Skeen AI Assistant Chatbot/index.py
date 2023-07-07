from flask import Flask, render_template, request
import openai
from openai.error import ServiceUnavailableError

app = Flask(__name__)
openai.api_key = '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'  # Replace with your OpenAI API key

conversation = [
    {"role": "system", "content": "I'm a skincare chatbot. Please ask me skin-related questions. I don't know anything else. I don't answer to anything other than skin-related questions. My answers are precise, small and concise."},
]

@app.route('/')
def index():
    return render_template('chat.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_query = request.form['user_query'] + ", be precise, small and concise."
    response = generate_response(user_query)
    return {'response': response}

def generate_response(user_query):
    global conversation
    conversation.append({"role": "user", "content": user_query})

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=conversation
        )
        reply = response.choices[0].message['content']
        conversation.append({"role": "system", "content": reply})
        return reply.strip()
    except ServiceUnavailableError:
        return "Sorry, the chatbot is temporarily unavailable. Please try again later."

if __name__ == '__main__':
    app.run()
