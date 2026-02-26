import json
from datetime import datetime

def log_change(changes_log_file, version, change_description):
    try:
        # Load existing changes
        try:
            with open(changes_log_file, 'r') as file:
                changes = json.load(file)
        except FileNotFoundError:
            changes = {}

        # Add new change
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if version not in changes:
            changes[version] = []
        changes[version].append({
            "timestamp": current_time,
            "description": change_description
        })

        # Save updated changes
        with open(changes_log_file, 'w') as file:
            json.dump(changes, file, indent=4)

    except Exception as e:
        print(f"Error logging change: {str(e)}")
