import json
import os

def create_json_file(filename, data):
    """Create a JSON file with the given data."""
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    print(f"JSON file '{filename}' created successfully.")

def read_json_file(filename):
    """Read and return data from a JSON file."""
    if not os.path.exists(filename):
        print(f"File '{filename}' does not exist.")
        return None

    with open(filename, 'r') as json_file:
        data = json.load(json_file)
    return data

def search_in_json(data, search_term):
    """Search for a term in the JSON data."""
    results = []
    for key, value in data.items():
        if search_term.lower() in str(value).lower():
            results.append((key, value))
    return results

if __name__ == "__main__":
    # Example data
    data = {
        "name": "ChatGPT",
        "description": "A language model by OpenAI",
        "version": "3.5"
    }

    filename = "data.json"

    # Create JSON file
    create_json_file(filename, data)

    # Read JSON file
    json_data = read_json_file(filename)
    if json_data:
        # Search for a term
        search_term = input("Enter a word to search: ")
        search_results = search_in_json(json_data, search_term)

        if search_results:
            print("Search results:")
            for key, value in search_results:
                print(f"{key}: {value}")
        else:
            print("No results found.")
