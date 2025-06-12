import json
import os

LOG_PATH = "logs/session_log.json"

def log_entry(timestamp, user_input, ethics_result, response):
    entry = {
        "timestamp": timestamp,
        "user_input": user_input,
        "ethics_result": ethics_result,
        "response": response
    }

    os.makedirs("logs", exist_ok=True)

    if not os.path.exists(LOG_PATH):
        with open(LOG_PATH, "w") as f:
            json.dump([entry], f, indent=2)
    else:
        with open(LOG_PATH, "r+") as f:
            data = json.load(f)
            data.append(entry)
            f.seek(0)
            json.dump(data, f, indent=2
