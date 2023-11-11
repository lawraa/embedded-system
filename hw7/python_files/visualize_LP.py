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

def plot_data(input_data, output_data, filtered_signal):
    fig, axs = plt.subplots(3, 1, figsize=(12, 10), sharex=True)

    # Styles
    styles = {'input': {'color': 'royalblue', 'marker': 'x', 'label': 'Input Data'},
              'output': {'color': 'darkorange', 'marker': 'x', 'label': 'Output Data'},
              'filtered': {'color': 'forestgreen', 'marker': 'x', 'label': 'Filtered Signal'}}

    # Plot input data

    axs[0].plot(input_data, **styles['input'])
    axs[0].set_title("Input Data")
    axs[0].set_ylabel("Value")
    axs[0].set_xlabel("Time")
    axs[0].grid(True, linestyle='--', alpha=0.7)

    # Plot output data
    axs[1].plot(output_data, **styles['output'])
    axs[1].set_title("Output Data - From Mbed")
    axs[1].set_ylabel("Value")
    axs[1].set_xlabel("Time")
    axs[1].grid(True, linestyle='--', alpha=0.7)

    # Plot filtered data
    axs[2].plot(filtered_signal, **styles['filtered'])
    axs[2].set_title("Filtered Signal - From Scipy LP Filter")
    axs[2].set_xlabel("Time")
    axs[2].set_ylabel("Value")
    axs[2].grid(True, linestyle='--', alpha=0.7)

    # Legends and Layout Adjustments
    for ax in axs:
        ax.legend(loc='upper right')
    plt.tight_layout(pad=3.0)
    plt.show()



# Main code

input_file_path = "../input/input.txt"  
output_file_path = "../output/output.txt"  

input_data = read_data(input_file_path)
output_data = read_data(output_file_path)

if len(input_data) != len(output_data):
    print(len(input_data))
    print(len(output_data))
    raise ValueError("Input and Output data lengths do not match.")
    

LPsignal = lfilter(fir_coeffs, 1.0, input_data)

plot_data(input_data, output_data, LPsignal)