import spacy
from textblob import TextBlob
from flask import Flask, request, jsonify

nlp = spacy.load('en_core_web_sm')
app = Flask(__name__)

# Function to perform cognitive computing tasks
def perform_cognitive_computing(user_input):
    doc = nlp(user_input)

    # Extract named entities
    named_entities = [ent.text for ent in doc.ents]
    
    # Perform sentiment analysis
    sentiment = TextBlob(user_input).sentiment.polarity

    # Perform topic extraction
    topics = [token.text for token in doc if token.pos_ == 'NOUN']

    return named_entities, sentiment, topics

# Route for handling the chat requests
@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_input = request.json['message']
        if user_input.lower() == 'cognitive_computing':
            named_entities, sentiment, topics = perform_cognitive_computing(user_input)
            response = f"Named Entities: {named_entities}\nSentiment: {sentiment}\nTopics: {topics}"
        else:
            response = get_bot_response(user_input)
        return jsonify({'response': response})
    except Exception as e:
        print("Error:", str(e))
        return jsonify({'response': 'Terjadi kesalahan saat memproses permintaan.'}), 500

if __name__ == '__main__':
    app.run()
