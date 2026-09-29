from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)

# Configure Gemini API
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate-home', methods=['POST'])
def generate_home():
    try:
        data = request.get_json() or {}
        budget = data.get('budget', '')
        requirements = data.get('requirements', '')

        prompt = f"Create a home interior plan with budget: {budget} and requirements: {requirements}"
        response = model.generate_content(prompt)

        return jsonify({'recommendations': response.text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
