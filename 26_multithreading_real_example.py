import time
import concurrent.futures
import requests

# Simulated API call
def fetch_flight_data(api_url):
    print(f"Calling {api_url}...")
    response = requests.get(api_url)   # pretend this takes time
    return {api_url: response.status_code}

# Simulated local task
def validate_user_input():
    print("Validating user input...")
    time.sleep(2)
    print("Validation complete.")

api_urls = [
    "https://api.airline1.com/flights",
    "https://api.airline2.com/flights",
    "https://api.airline3.com/flights"
]

# Run API calls in parallel threads
with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = [executor.submit(fetch_flight_data, url) for url in api_urls]

    # Do local work while APIs are running
    validate_user_input()

    # Collect API results
    for future in concurrent.futures.as_completed(futures):
        print("API result:", future.result())

"""
O/P
Calling https://api.airline1.com/flights...
Calling https://api.airline2.com/flights...
Calling https://api.airline3.com/flights...
Validating user input...
Validation complete.
API result: {'https://api.airline2.com/flights': 200}
API result: {'https://api.airline1.com/flights': 200}
API result: {'https://api.airline3.com/flights': 200} """
