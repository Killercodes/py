import json
import os

class Config:
    def __init__(self, config_file="config.json"):
        # Read the config file
        self.config_file = config_file
        self.load_config()

    def load_config(self):
        # Check if the config file exists
        if not os.path.exists(self.config_file):
            raise FileNotFoundError(f"{self.config_file} not found")

        # Open and read the JSON file
        with open(self.config_file, "r") as f:
            config_data = json.load(f)

        # Set each key-value pair as an attribute of the object
        for key, value in config_data.items():
            setattr(self, key, value)

    def __repr__(self):
        # Return a string representation of the config object
        return f"<Config {vars(self)}>"

# Example usage:
if __name__ == "__main__":
    # Create the Config object, which will load config.json
    config = Config()

    # Accessing properties dynamically
    print(config)  # This will show the loaded config properties

    # Example of accessing individual properties
    print(config.debug)
    print(config.newobj["name"])  # Replace 'some_key' with an actual key in config.json
