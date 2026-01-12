import requests
def get_rejection_reason():
    url = "https://naas.isalman.dev/no"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return f"Rejection: {data.get('reason')}"
        else:
            return f"Error: Recieved status code {response.status_code}"
    except Exception as e:
        return f"An error occurred: {e}"
if __name__ == "__main__":
    print(get_rejection_reason())