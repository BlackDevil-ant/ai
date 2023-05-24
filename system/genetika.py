import random

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
