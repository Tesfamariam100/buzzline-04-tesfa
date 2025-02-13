import json
import random
import time
from datetime import datetime, timedelta

# Define file path for data storage
data_file = "C:\\DSProjects\\buzzline-04-tesfa\\data\\buzz_input.json"

# Sample words for generating messages
WORDS = ["Hello", "World", "Python", "Kafka", "Streaming", "Data", "Analysis", "AI", "Machine Learning"]

# Function to generate a random sentiment score (0.0 - 1.0)
def generate_sentiment():
    return round(random.uniform(0, 1), 2)

# Function to generate messages
def generate_messages(num_messages=100):
    messages = []
    
    start_time = datetime.now()
    
    for i in range(num_messages):
        message_text = f"{random.choice(WORDS)} {random.choice(WORDS)}"
        timestamp = (start_time + timedelta(seconds=i)).strftime("%Y-%m-%d %H:%M:%S")
        sentiment = generate_sentiment()
        
        messages.append({
            "message": message_text,
            "timestamp": timestamp,
            "sentiment": sentiment
        })
    
    return messages

# Main function to write data to JSON file
def main():
    messages = generate_messages()
    
    try:
        with open(data_file, "w", encoding="utf-8") as file:
            json.dump(messages, file, indent=4)
        print(f"✅ Successfully wrote {len(messages)} messages to {data_file}")
    except Exception as e:
        print(f"❌ Error writing to file: {e}")

if __name__ == "__main__":
    main()
