import matplotlib.pyplot as plt

# Example data (replace this with your actual data)
square_grid_sizes = [10, 15, 20, 25, 30, 35]
square_times = [0.05859541893005371, 0.2104499340057373, 0.6029419898986816, 1.0049123764038086, 1.805891752243042, 2.9373788833618164]
hexagonal_grid_sizes = [10, 15, 20, 25, 30, 35]
hexagonal_times = [0.04236555099487305, 0.10612058639526367, 0.20646142959594727, 0.30500125885009766, 0.6009635925292969, 0.5728495121002197]

# Plotting
plt.plot(square_grid_sizes, square_times, label='Square Grid', marker='o')
plt.plot(hexagonal_grid_sizes, hexagonal_times, label='Hexagonal Grid', marker='s')
plt.xlabel('Grid Size')
plt.ylabel('Time Taken (seconds)')
plt.title('Comparison of Genetic Algorithm')
plt.legend()
plt.grid(True)
plt.show()
