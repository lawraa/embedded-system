import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import lfilter

# FIR coefficients
fir_coeffs = np.array(
    [
        -0.0018225230,
        -0.0015879294,
        0.0000000000,
        +0.0036977508,
        +0.0080754303,
        +0.0085302217,
        -0.0000000000,
        -0.0173976984,
        -0.0341458607,
        -0.0333591565,
        +0.0000000000,
        +0.0676308395,
        +0.1522061835,
        +0.2229246956,
        +0.2504960933,
        +0.2229246956,
        +0.1522061835,
        +0.0676308395,
        +0.0000000000,
        -0.0333591565,
        -0.0341458607,
        -0.0173976984,
        -0.0000000000,
        +0.0085302217,
        +0.0080754303,
        +0.0036977508,
        +0.0000000000,
        -0.0015879294,
        -0.0018225230,
    ]
)

# Function to read data from a file
def read_data_from_file(file_path):
    with open(file_path, "r") as file:
        line = file.readline()
        data = [float(number) for number in line.split()]
    return data

# Function to plot the data
def plot_data(input_data, output_data, filtered_signal):
    fig, axs = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

    # Styles
    styles = {'input': {'color': 'royalblue', 'marker': 'o', 'label': 'Input Data'},
              'output': {'color': 'darkorange', 'marker': 'x', 'label': 'Output Data'},
              'filtered': {'color': 'forestgreen', 'marker': 's', 'label': 'Filtered Signal'}}

    # Plot input and output data in the first subplot
    axs[0].plot(input_data, **styles['input'])
    axs[0].plot(output_data, **styles['output'])
    axs[0].set_title("Input and Output Data - From Mbed")
    axs[0].set_ylabel("Value")
    axs[0].grid(True, linestyle='--', alpha=0.7)
    axs[0].legend(loc='upper right')

    # Plot filtered data in the second subplot
    axs[1].plot(filtered_signal, **styles['filtered'])
    axs[1].set_title("Filtered Signal - From Scipy LP Filter")
    axs[1].set_xlabel("Index")
    axs[1].set_ylabel("Value")
    axs[1].grid(True, linestyle='--', alpha=0.7)
    axs[1].legend(loc='upper right')

    plt.tight_layout(pad=3.0)
    plt.show()

# Main code

input_file_path = "../input/input.txt"  
output_file_path = "../output/output.txt"  

input_data = read_data_from_file(input_file_path)
output_data = read_data_from_file(output_file_path)

# Validate data lengths
if len(input_data) != len(output_data):
    raise ValueError("Input and Output data lengths do not match.")

filtered_signal = lfilter(fir_coeffs, 1.0, input_data)

plot_data(input_data, output_data, filtered_signal)
