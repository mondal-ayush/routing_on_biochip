import numpy as np
import random

# Define the directions
directions = ['left', 'right', 'top', 'bottom']

def create_individual(n, m):
    # Create a random sequence of moves
    return [random.choice(directions) for _ in range(n * m)]

def evaluate(individual, grid, start, end, n, m):
    # Start from the start point
    x, y = start
    fitness = 0

    # Keep track of the visited cells
    visited = set()

    # Make each move in the individual's sequence
    for move in individual:
        if move == 'left' and y > 0 and grid[x][y-1] == 0 and (x, y-1) not in visited:
            y -= 1
        elif move == 'right' and y < m-1 and grid[x][y+1] == 0 and (x, y+1) not in visited:
            y += 1
        elif move == 'top' and x > 0 and grid[x-1][y] == 0 and (x-1, y) not in visited:
            x -= 1
        elif move == 'bottom' and x < n-1 and grid[x+1][y] == 0 and (x+1, y) not in visited:
            x += 1

        # Add the current cell to the visited cells
        visited.add((x, y))

        # Calculate the Manhattan distance from the end point
        fitness += abs(x - end[0]) + abs(y - end[1])

        # If the end point is reached, break the loop
        if (x, y) == end:
            break

    return fitness

def select_parents(population, fitness_values):
    # Select individuals with lower fitness values for crossover
    return [population[i] for i in np.argsort(fitness_values)[:len(population)//2]]

def crossover_and_mutation(parents):
    # Create a new population by combining and modifying the moves of the parents
    new_population = []

    while len(new_population) < len(parents):
        # Select two parents
        parent1, parent2 = random.sample(parents, 2)

        # Perform single-point crossover
        crossover_point = random.randint(0, len(parent1))
        offspring = parent1[:crossover_point] + parent2[crossover_point:]

        # Perform mutation
        mutation_point = random.randint(0, len(offspring)-1)
        offspring[mutation_point] = random.choice(directions)

        new_population.append(offspring)

    return new_population

def print_path(individual, grid, start, end, n, m):
    # Start from the start point
    x, y = start

    # Keep track of the visited cells
    visited = set()

    # Make each move in the individual's sequence
    for move in individual:
        if move == 'left' and y > 0 and grid[x][y-1] == 0 and (x, y-1) not in visited:
            y -= 1
        elif move == 'right' and y < m-1 and grid[x][y+1] == 0 and (x, y+1) not in visited:
            y += 1
        elif move == 'top' and x > 0 and grid[x-1][y] == 0 and (x-1, y) not in visited:
            x -= 1
        elif move == 'bottom' and x < n-1 and grid[x+1][y] == 0 and (x+1, y) not in visited:
            x += 1

        # Add the current cell to the visited cells
        visited.add((x, y))

        # Print the move and hence current position
        # If an invalid move(obstacles or visited cell) if made the position remains same
        fitness = evaluate(individual, grid, (x, y), end, n, m)
        print(f"Move: {move}, Position: ({x}, {y})")

        # If the end point is reached, break the loop
        if (x, y) == end:
            break

# Driver code
def run_genetic_algorithm(n, m, obstacles, start, end, pop_size, generations):
    # Initialize the grid with 0's
    grid = np.zeros((n, m))

    # Define some obstacles in the grid by setting their value to 1
    for obstacle in obstacles:
        grid[obstacle] = 1

    # Define the initial population
    population = [create_individual(n, m) for _ in range(pop_size)]

    for generation in range(generations):
        # Evaluate the fitness of each individual in the population
        fitness_values = [evaluate(individual, grid, start, end, n, m) for individual in population]

        # Print the current generation
        # print(f"Generation: {generation + 1}")

        # Select the parents for crossover
        parents = select_parents(population, fitness_values)

        # Check if there are at least two parents before attempting crossover
        if len(parents) < 2:
            break

        # Perform crossover and mutation to create a new population
        population = crossover_and_mutation(parents)

        # Evaluate the fitness of the new population
        fitness_values = [evaluate(individual, grid, start, end, n, m) for individual in population]

        # If the end point is reached by any individual, break the loop
        if any(fitness == 0 for fitness in fitness_values):
            break

    # Find the best individual from the final population
    best_individual = population[np.argmin(fitness_values)]

    # Print the path taken by the best individual
    print_path(best_individual, grid, start, end, n, m)