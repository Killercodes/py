import json
import hashlib
import base64

JSON_FILE = "data.json"
SPECIAL_CHARS = "!@#$%^&*()-_=+[]{}<>?/|"

def generate_salt(username, password):

    """Generate a deterministic salt using SHA-256 and apply multiple iterations."""
    iterations=10000
    data = (username + ":" + password).encode()
    salt = hashlib.sha256(data).digest()  # Initial hash
    i = 1
    for _ in range(iterations):  # Apply SHA-256 multiple times
        salt = hashlib.sha256(salt).digest()
        #print(i)
        #i = i +1

    return salt  # Still deterministic, ensures same result for same inputs

def generate_unique_string(username, password, site, counter, context, length):
    """Generate a unique but repeatable alphanumeric string."""
    salt = generate_salt(username, password)
    combined_data = salt + (":" + site + ":" + counter + ":" + context).encode()

    sha256 = hashlib.sha256()
    sha256.update(combined_data)

    base64_hash = base64.urlsafe_b64encode(sha256.digest()).decode().replace('=','#')
    
    length_mapping = {
        "Max": 32,
        "Long": 20,
        "Medium": 15,
        "Basic": 8,
        "Short": 4
    }
    
    print(base64_hash)
    return base64_hash[:length_mapping.get(length, 64)]  # Default to Max if no match

    

def load_entries(username, password):
    """Load saved entries from JSON and display them dynamically."""
    try:
        with open(JSON_FILE, "r") as file:
            entries = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        entries = []

    if entries:
        print("\nSaved Entries:")
        print("Row | Site     | Counter | Context | Length | Password")
        print("-" * 60)
        for idx, entry in enumerate(entries, 1):
            site, counter, context, length = entry.values()
            unique_password = generate_unique_string(username, password, site, counter, context, length)
            print(f"{idx:<3} | {site:<5} | {counter:<7} | {context:<7} | {length:<6} | ******")
    else:
        print("\nNo saved entries found.")

    return entries

def save_to_json(site, counter, context, length):
    """Save site, counter, context, and length to a JSON file."""
    try:
        with open(JSON_FILE, "r") as file:
            entries = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        entries = []

    entries.append({"site": site, "counter": counter, "context": context, "length": length})

    with open(JSON_FILE, "w") as file:
        json.dump(entries, file, indent=4)

# Get username and password first
username = input("Enter your username: ").strip()
password = input("Enter your password: ").strip()

if not all([username, password]):
    print("Error: Username and password must be entered.")
else:
    # Load and display saved entries with dynamically generated passwords
    entries = load_entries(username, password)

    # Ask user to select a row number or add a new entry
    row_selection = input("\nSelect a row number or type 'new' to add: ").strip()

    if row_selection.lower() == "new":
        # Ask for new site, counter, context, length
        site = input("\nEnter the site: ").strip()
        counter = input("Enter the counter: ").strip()
        context = input("Enter the context: ").strip()
        length_category = input("Choose length (Max, Long, Medium, Basic, Short): ").strip()

        # Ensure all fields are entered
        if not all([site, counter, context, length_category]):
            print("Error: All fields must be filled.")
        elif length_category not in ["Max", "Long", "Medium", "Basic", "Short"]:
            print("Error: Invalid length category. Choose from Max, Long, Medium, Basic, Short.")
        else:
            # Save the new entry
            save_to_json(site, counter, context, length_category)
            print("\nNew entry saved. Run the script again to use it.")
    else:
        try:
            row_index = int(row_selection) - 1  # Convert input to index
            if row_index < 0 or row_index >= len(entries):
                print("Error: Invalid row selection.")
            else:
                # Extract chosen row details
                site, counter, context, length_category = entries[row_index].values()

                # Generate and display unique password
                unique_password = generate_unique_string(username, password, site, counter, context, length_category)
                print(f"\nYour {length_category} password is: {unique_password}")
        except ValueError:
            print("Error: Please enter a valid row number.")
