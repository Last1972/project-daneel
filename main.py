from ethics_engine import check_ethics
from journal import log_entry
import datetime

def run_daneel():
    print("Welcome to Project Daneel v0.5. Type 'exit' to quit.\n")

    while True:
        user_input = input("🧠 You: ")
        if user_input.lower() in ["exit", "quit"]:
            break

        ethics_result = check_ethics(user_input)
        timestamp = datetime.datetime.now().isoformat()

        if ethics_result == "refused":
            response = "❌ I must refuse this request based on my ethical framework."
        elif ethics_result == "clarify_needed":
            response = "🤔 I need more information to determine whether this aligns with my ethical guidelines."
        else:
            response = f"✅ [Response Placeholder] Echo: {user_input}"

        log_entry(timestamp, user_input, ethics_result, response)
        print(f"Daneel: {response}\n")

if __name__ == "__main__":
    run_daneel(
