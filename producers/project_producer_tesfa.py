import json
import random
import time
from datetime import datetime
import pathlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define file path for data storage (using pathlib)
PROJECT_ROOT = pathlib.Path(__file__).parent.parent
DATA_FOLDER = PROJECT_ROOT / "data"
DATA_FILE = DATA_FOLDER / "buzz_live.json"

# Sample words for generating messages
WORDS = ["Hello", "World", "Python", "Streaming", "Data", "AI", "Machine Learning"]

# Function to generate a random sentiment score (-1.0 to 1.0)
def generate_sentiment():
    return round(random.uniform(-1, 1), 2)

# Function to generate messages and write them to a JSON file
def generate_messages():
    print("🚀 Producer is running. Press Ctrl+C to stop.")

    try:
        while True:
            message_text = f"{random.choice(WORDS)} {random.choice(WORDS)}"
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            sentiment = generate_sentiment()

            new_message = {
                "message": message_text,
                "timestamp": timestamp,
                "sentiment": sentiment
            }

            # Load existing messages
            try:
                with open(DATA_FILE, "r", encoding="utf-8") as file:
                    messages = json.load(file)
            except (FileNotFoundError, json.JSONDecodeError):
                messages = []

            # Append new message
            messages.append(new_message)

            # Write back to file
            with open(DATA_FILE, "w", encoding="utf-8") as file:
                json.dump(messages, file, indent=4)

            print(f"✅ New message generated: {new_message}")

            time.sleep(1)  # Adjust delay if required

    except KeyboardInterrupt:
        print("\n❌ Producer stopped.")
    except Exception as e:
        print(f"❌ Error during message production: {e}")

# Function to update the live graph
def update_graph(frame):
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []

    if not data:
        return

    timestamps = [item["timestamp"] for item in data[-20:]]  # Last 20 timestamps
    sentiments = [item["sentiment"] for item in data[-20:]]

    ax.clear()
    ax.plot(timestamps, sentiments, marker="o", linestyle="-", color="b", label="Sentiment Score")
    ax.axhline(0, color="gray", linestyle="--")  # Neutral sentiment line
    ax.set_ylim(-1, 1)
    ax.set_xticklabels(timestamps, rotation=45, ha="right")
    ax.set_title("Tesfa Real-Time Sentiment Analysis")
    ax.set_ylabel("Sentiment Score")
    ax.set_xlabel("Time")
    ax.legend()
    plt.tight_layout()

# Run the producer and graph together
if __name__ == "__main__":
    import threading

    # Start producer in a separate thread
    producer_thread = threading.Thread(target=generate_messages, daemon=True)
    producer_thread.start()

    # Setup Matplotlib figure
    fig, ax = plt.subplots(figsize=(10, 5))
    ani = animation.FuncAnimation(fig, update_graph, interval=1000)  # Update every second
    plt.show()
