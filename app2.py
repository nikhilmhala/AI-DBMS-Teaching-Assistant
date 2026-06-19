import requests

# Langflow API details
API_KEY = "sk-LjYE_cKhpleNsmSUZxxbpzpH2amaua6AxPseu1wG2es"
URL = "http://localhost:7860/api/v1/run/d0830fd7-4ee6-4bec-887c-8914543820bc"

# Fixed session ID for continuous conversation
SESSION_ID = "nikhil_nutrition_session"

headers = {
    "x-api-key": API_KEY
}

print("=" * 50)
print("DBMS Assistant Chat Started")
print("Type 'exit' to quit")
print("=" * 50)

while True:
    user_input = input("\nYou: ")

    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    payload = {
        "output_type": "chat",
        "input_type": "chat",
        "session_id": SESSION_ID,
        "input_value": user_input
    }

    try:
        response = requests.post(
            URL,
            json=payload,
            headers=headers
        )

        response.raise_for_status()

        data = response.json()

        # Extract response text
        bot_reply = data["outputs"][0]["outputs"][0]["results"]["message"]["text"]

        print("\nBot:", bot_reply)

    except requests.exceptions.RequestException as e:
        print(f"\nAPI Error: {e}")

    except KeyError as e:
        print(f"\nResponse format error: {e}")
        print(data)

    except Exception as e:
        print(f"\nUnexpected error: {e}")