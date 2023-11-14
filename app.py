from flask import Flask, request, jsonify
import openai
from prompt import get_summarization_prompt
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

# Set your OpenAI API key
openai.api_key = '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'


@app.route('/ping', methods=['GET'])
def ping():
    return "ping"


@app.route('/summarize', methods=['POST'])
def summarize():
    try:
        print("==>>>> 1")
        data = request.get_json()
        print("==>> 2")
        print(data)
        text_to_summarize = get_summarization_prompt(data["text"])

        print("==>>>> ")
        print(text_to_summarize)

        user_prompt = [{
            "role": "user",
            "content": text_to_summarize
        }]

        # Using GPT-3 for summarization
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-1106",
            messages=user_prompt,
            max_tokens=150,
            temperature=0.7,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )

        summary = response['choices'][0]["message"]["content"]

        print(summary)

        return jsonify({'summary': summary})

    except Exception as e:
        print(e)
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
