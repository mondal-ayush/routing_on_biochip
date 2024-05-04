import GeneticSqGrid
import time, json

with open('testcases/test_cases_1.json', 'r') as f:
    test_cases = json.load(f)

# Initialize lists to store grid sizes and corresponding times
square_grid_sizes = []
square_times = []

# Iterate over each test case
for i, test_case in enumerate(test_cases, start=1):
    print(f"Running test case {i}...")

    # Unpack test case parameters
    n = test_case['n']
    m = test_case['m']
    obstacles = test_case['obstacles']
    start = test_case['start']
    end = test_case['end']
    pop_size = test_case['pop_size']
    generations = test_case['generations']

    # Store grid size
    grid_size = max(n, m)
    square_grid_sizes.append(grid_size)

    print(f'Grid : {n} X {m}')

    # Measure time taken to run genetic algorithm
    start_time = time.time()
    GeneticSqGrid.run_genetic_algorithm(n, m, obstacles, start, end, pop_size, generations)
    end_time = time.time()

    # Calculate and store time taken
    time_taken = end_time - start_time
    square_times.append(time_taken)

    print("Test case completed.\n")

# Write the lists to a text file
with open('dumps/results.txt', 'w') as f:
    f.write("square_grid_sizes = " + str(square_grid_sizes) + "\n")
    f.write("square_times = " + str(square_times) + "\n")
