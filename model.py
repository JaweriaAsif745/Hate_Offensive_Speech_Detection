from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)

# Loading model and vectorizer
with open('Hate_speech_detector_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('Hate_speech_detector_model_vectorizer.pkl', 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)


@app.route('/', methods=['GET']) 
def index():
    return render_template("index.html")

@app.route("/analyze", methods=['POST'])
def analyze_text():
    try:
        # get input from request
        data = request.get_json()
        text = data.get('text', '')
    
        # validate input
        if not text.strip():
            return jsonify({'error':"No text provided"}), 400
    
        # transform text using vectorizer
        transformed_text = vectorizer.transform([text])

        # predict using model
        prediction = model.predict(transformed_text)[0]

        # Map prediction to labels
        label_map = {0: 'Hate', 1:'Offensive', 2:'Neutral'}
        result = {"label": label_map[prediction]}

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
if __name__ == '__main__':
    app.run(debug=True)
