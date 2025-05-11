from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import requests
import os
from dotenv import load_dotenv
import time

load_dotenv()
app = Flask(__name__)
CORS(app)

HF_TOKEN = os.getenv("HF_TOKEN")
HEADERS = {"Authorization": f"Bearer {HF_TOKEN}"}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze_pest():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    try:
        image_data = file.read()
        pest_result = detect_pest(image_data)

        if "error" in pest_result:
            return jsonify({"error": pest_result["error"]}), 500

        pest_label = pest_result.get('label', 'Unknown Pest')
        score = pest_result.get('score', 0)

        recommendations = get_ai_recommendations(pest_label)

        return jsonify({
            "pest": pest_label,
            "confidence": f"{score * 100:.1f}%",
            "recommendations": recommendations
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

def detect_pest(image_data):
    API_URL = "https://api-inference.huggingface.co/models/google/vit-base-patch16-224"

    for _ in range(3):
        response = requests.post(API_URL, headers=HEADERS, data=image_data)
        if response.status_code == 200:
            data = response.json()
            if data and isinstance(data, list) and len(data) > 0:
                return data[0]
        time.sleep(5)
    
    return {"error": "Pest detection failed"}

def get_ai_recommendations(pest):
    API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"

    prompt = f"""
Task: As a senior entomologist, give recommendations to manage a {pest} infestation.

- Use eco-friendly methods first
- Recommend specific pesticides (if any)
- Mention safety precautions

Structure:
Organic Control | Chemical Treatments | Prevention | Safety
"""

    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 300,
            "temperature": 0.7
        }
    }

    response = requests.post(API_URL, headers=HEADERS, json=payload)

    if response.status_code == 200:
        try:
            result = response.json()
            full_text = result[0]['generated_text']
            clean_text = full_text.split("Structure:")[-1].strip()
            return clean_text.replace("\n", "<br>")
        except:
            return "Could not parse AI recommendations."
    else:
        return "AI recommendation generation failed."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
