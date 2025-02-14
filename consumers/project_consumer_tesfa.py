import json
import random
import time
from datetime import datetime, timedelta
import os
import pathlib

# Define file path for data storage (using pathlib)
PROJECT_ROOT = pathlib.Path(__file__).parent.parent
DATA_FOLDER: pathlib.Path = PROJECT_ROOT.joinpath("data")
DATA_FILE: pathlib.Path = DATA_FOLDER.joinpath("buzz_input.json")

# Sample words for generating messages
WORDS = ["Hello", "World", "Python", "Kafka", "Streaming", "Data", "Analysis", "AI", "Machine Learning"]

# Function to generate a random sentiment score (0.0 - 1.0)
def generate_sentiment():
    return round(random.uniform(0, 1), 2)

# Function to generate messages (modified for continuous operation)
def generate_messages():
    while True:  # Run indefinitely
        message_text = f"{random.choice(WORDS)} {random.choice(WORDS)}"
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Current time
        sentiment = generate_sentiment()

        yield {  # Use yield to return messages one at a time
            "message": message_text,
            "timestamp": timestamp,
            "sentiment": sentiment
        }
        time.sleep(1) # Adjust delay if required

 # Generate and send messages continuously
    try:
        for message_dict in generate_messages(): # No argument needed, it's a generator
            producer.send(topic, value=message_dict)
            logger.info(f"Sent message to topic '{topic}': {message_dict}")
            # time.sleep(interval_secs)  # If you need an interval between messages
    except KeyboardInterrupt:
        logger.warning("Producer interrupted by user.")
    except Exception as e:
        logger.error(f"Error during message production: {e}")
    finally:
        producer.close()
        logger.info("Kafka producer closed.")

    logger.info("END producer.")
    
    try:
        with open(data_file, "w", encoding="utf-8") as file:
            json.dump(messages, file, indent=4)
        print(f"✅ Successfully wrote {len(messages)} messages to {data_file}")
    except Exception as e:
        print(f"❌ Error writing to file: {e}")

def main():  # Define main() FIRST
    # ... (code for your main function) ...
                if __name__ == "__main__":  # THEN call main()
                                    main()
