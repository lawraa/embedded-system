import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import lfilter

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

def read_data(file_name):
    with open(file_name, "r") as file:
        line = file.readline()
        data = [float(number) for number in line.split()]
    return data

def plot_data(input_data, output_data, ground_truth):
    fig, axs = plt.subplots(2, 1, figsize=(12, 10), sharex=True)

    # Styles
    styles = {'input': {'color': 'royalblue', 'marker': 'x', 'label': 'Input Data'},
              'output': {'color': 'darkorange', 'marker': 'o', 'label': 'Output Data'},
              'truth': {'color': 'red', 'marker': 'x', 'label': 'Ground Truth Signal'}}

    # Plot input data
    axs[0].plot(input_data, **styles['input'])
    axs[0].set_title("Input Data")
    axs[0].set_ylabel("Value")
    axs[0].grid(True, linestyle='--', alpha=0.7)

    # Plot output data and ground truth on the same graph
    axs[1].plot(ground_truth, **styles['truth'])
    axs[1].plot(output_data, **styles['output'])
    
    axs[1].set_title("Output Data and Ground Truth")
    axs[1].set_ylabel("Value")
    axs[1].grid(True, linestyle='--', alpha=0.7)

    # Legends and Layout Adjustments
    for ax in axs:
        ax.legend(loc='upper right')
        ax.set_xlabel("Time")

    plt.tight_layout(pad=3.0)
    plt.show()

# Main code
input_file_path = "../input/input.txt"  
output_file_path = "../output/output.txt"   
ground_truth_path = "../test_ground.txt"
input_data = read_data(input_file_path)
output_data = read_data(output_file_path)
ground_truth_data = read_data(ground_truth_path)

if len(input_data) != len(output_data):
    print(len(input_data))
    print(len(output_data))
    raise ValueError("Input and Output data lengths do not match.")
    
plot_data(input_data, output_data, ground_truth_data)