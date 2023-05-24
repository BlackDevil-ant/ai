import json
from flask import Flask, request, jsonify
import random
import random
import json
import cv2
from system.learning_model import load_data, build_model, predict
from system.find_matching_gpu import find_matching_gpu
import spacy
from textblob import TextBlob


nlp = spacy.load('en_core_web_sm')

app = Flask(__name__)

# Load data and build the model
data = load_data()
model = build_model()

# Load data from JSON file
def load_data():
    with open('./db/data.json', 'r') as file:
        data = json.load(file)
    return data

data = load_data()

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

# Fungsi untuk menghasilkan populasi awal
def generate_population(population_size, chromosome_length):
    population = []
    for _ in range(population_size):
        chromosome = [random.randint(0, 1) for _ in range(chromosome_length)]
        population.append(chromosome)
    return population

# Fungsi untuk menghitung fitness individu
def calculate_fitness(chromosome):
    fitness = sum(chromosome)
    return fitness

# Fungsi untuk memilih orang tua berdasarkan turnamen
def tournament_selection(population, k):
    tournament = random.sample(population, k)
    tournament.sort(key=lambda chromosome: calculate_fitness(chromosome), reverse=True)
    return tournament[0]

# Fungsi untuk melakukan crossover pada pasangan orang tua
def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

# Fungsi untuk melakukan mutasi pada individu
def mutation(chromosome, mutation_rate):
    for i in range(len(chromosome)):
        if random.random() < mutation_rate:
            chromosome[i] = 1 - chromosome[i]
    return chromosome

# Fungsi utama algoritma genetika
def genetic_algorithm(population_size, chromosome_length, tournament_size, crossover_rate, mutation_rate, generations):
    population = generate_population(population_size, chromosome_length)

    for _ in range(generations):
        new_population = []
        while len(new_population) < population_size:
            parent1 = tournament_selection(population, tournament_size)
            parent2 = tournament_selection(population, tournament_size)

            if random.random() < crossover_rate:
                offspring1, offspring2 = crossover(parent1, parent2)
                offspring1 = mutation(offspring1, mutation_rate)
                offspring2 = mutation(offspring2, mutation_rate)
                new_population.append(offspring1)
                new_population.append(offspring2)
            else:
                new_population.append(parent1)
                new_population.append(parent2)

        population = new_population

    best_chromosome = max(population, key=lambda chromosome: calculate_fitness(chromosome))
    best_fitness = calculate_fitness(best_chromosome)

    return best_chromosome, best_fitness

# Route for handling the chat requests
# Fungsi untuk mengirim permintaan ke server
def send_message(message):
    url = 'http://localhost:5000/chat'
    payload = {'message': message}
    response = requests.post(url, json=payload)
    return response.json()['response']

# Fungsi untuk memproses citra
def process_image(image):
    # Proses pengolahan citra menggunakan OpenCV
    # Ganti dengan algoritma yang cocok untuk tujuan Anda
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
    edges = cv2.Canny(blurred_image, 50, 150)

    # Kirim hasil citra ke server
    response = send_message('image_processed')
    print('Server Response:', response)

    # Tampilkan citra dan hasil pengolahan
    cv2.imshow('Original Image', image)
    cv2.imshow('Processed Image', edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Route for handling the chat requests
@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_input = request.json['message']
        if user_input.lower() == 'genetic_algorithm':
            best_chromosome, best_fitness = genetic_algorithm(population_size, chromosome_length, tournament_size, crossover_rate, mutation_rate, generations)
            response = f"Best Chromosome: {best_chromosome}\nBest Fitness: {best_fitness}"
        elif user_input.lower() == 'process_image':
            # Baca citra dari file
            image = cv2.imread('image.jpg')

            # Proses citra
            process_image(image)
            response = 'Image processing completed.'
        elif user_input.lower() == 'deep_learning':
            # Load data and build the model
            data = load_data()
            model = build_model()

            # Preprocess input data
            processed_data = preprocess_data(user_input)

            # Make predictions using the model
            predictions = predict(model, processed_data)

            # Process predictions and generate response
            response = process_predictions(predictions)
            
        elif user_input.lower() == 'find_gpu':
            # Parameter pencarian GPU
            search_brand = 'Nvidia'
            min_memory_size = 8

            # Mencari GPU yang sesuai
            matching_gpus = find_matching_gpu(gpus, search_brand, min_memory_size)

            # Membentuk respons
            response = "Matching GPUs:\n"
            if matching_gpus:
                for gpu in matching_gpus:
                    response += str(gpu) + "\n"
            else:
                response += "No matching GPUs found."

        else:
            response = get_bot_response(user_input)
            
        return jsonify({'response': response})
    except Exception as e:
        print("Error:", str(e))
        return jsonify({'response': 'Terjadi kesalahan saat memproses permintaan.'}), 500



# Function to get bot response
def get_bot_response(user_input):
    for intent in data['intents']:
        for pattern in intent['patterns']:
            if isinstance(user_input, str) and isinstance(pattern, str) and user_input.lower() == pattern.lower():
                # Perform action if defined
                if 'action' in intent:
                    action = intent['action']
                    if action['type'] == 'search':
                        search_engine = action['search_engine']
                        query = action['query']
                        perform_search(search_engine, query)
                return intent['responses']
    return ["Maaf tuan, saya tidak mengerti pertanyaan Anda."]

# Function to perform search
def perform_search(search_engine, query):
    if search_engine == 'google':
        # Code to perform Google search
        print(f"Melakukan pencarian di Google dengan kata kunci: {query}")
        # Place your code here to perform search using Google
    elif search_engine == 'other':
        # Code to perform search using other search engine
        print(f"Melakukan pencarian menggunakan search engine lain dengan kata kunci: {query}")
        # Place your code here to perform search using other search engine

if __name__ == '__main__':
    # Algoritma genetika - Parameter
    population_size = 10
    chromosome_length = 8
    tournament_size = 5
    crossover_rate = 0.8
    mutation_rate = 0.1
    generations = 100

    app.run()
