import json
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time
import os

# Path to the JSON file (Make sure this matches your producer's output)
FILE_PATH = "data/buzz_live.json"  # Relative path from the consumer's location

# Initialize data for the plot
timestamps = []
sentiments = []

# Function to read new data from the JSON file
def read_json_data(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        return []  # Handle file not found or JSON error gracefully

# Function to process the data and extract timestamps and sentiment
def process_data(data):
    new_timestamps = [entry['timestamp'] for entry in data if entry['timestamp'] not in timestamps] #Avoid duplicates
    new_sentiments = [entry['sentiment'] for entry in data if entry['timestamp'] not in timestamps] #Avoid duplicates
    timestamps.extend(new_timestamps)
    sentiments.extend(new_sentiments)
    return timestamps, sentiments

# Function to set up the plot and animation
def plot_data(timestamps, sentiments):
    fig, ax = plt.subplots()
    line, = ax.plot([], [], lw=2)

    ax.set_xlim(0, 100)  # Initial x-axis limit (adjust as needed)
    ax.set_ylim(-1, 1)  # Example y-axis limits (adjust based on your sentiment range)

    def init():
        return line,

    def update(frame):
        line.set_data(range(min(frame, len(timestamps))), sentiments[:min(frame, len(timestamps))])
        ax.set_xlim(0, max(frame,100)) #Dynamic x-axis
        return line,

    ani = FuncAnimation(fig, update, frames=range(1, 1000), init_func=init, blit=True)  #Frames are now a range

    plt.show()

# Main function to consume and process data
if __name__ == "__main__":
    plot_data(timestamps, sentiments)  # Start the plot

    while True:
        data = read_json_data(FILE_PATH)
        if data:
            timestamps, sentiments = process_data(data)
            time.sleep(1) #Check every sec
