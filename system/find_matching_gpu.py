import random

class GPU:
    def __init__(self, gpu_id, brand, memory_size):
        self.gpu_id = gpu_id
        self.brand = brand
        self.memory_size = memory_size

    def __str__(self):
        return f"GPU ID: {self.gpu_id}, Brand: {self.brand}, Memory Size: {self.memory_size} GB"

def generate_gpus(num_gpus):
    brands = ['Nvidia', 'AMD', 'Intel']
    gpus = []
    for i in range(1, num_gpus + 1):
        gpu_id = i
        brand = random.choice(brands)
        memory_size = random.randint(4, 16)
        gpu = GPU(gpu_id, brand, memory_size)
        gpus.append(gpu)
    return gpus

def find_matching_gpu(gpus, search_brand, min_memory_size):
    matching_gpus = []
    for gpu in gpus:
        if gpu.brand == search_brand and gpu.memory_size >= min_memory_size:
            matching_gpus.append(gpu)
    return matching_gpus

# Generate GPUs
gpus = generate_gpus(10)

# Find matching GPUs
search_brand = 'Nvidia'
min_memory_size = 8
matching_gpus = find_matching_gpu(gpus, search_brand, min_memory_size)

# Print matching GPUs
for gpu in matching_gpus:
    print(gpu)
