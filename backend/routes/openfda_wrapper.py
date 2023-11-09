import requests

class OpenFDAWrapper:
    def __init__(self, api_key):
        self.base_url = "https://api.fda.gov"
        self.api_key = api_key

    def get_drug_events(self, search_term, limit=100):
        url = f"{self.base_url}/drug/event.json?search={search_term}&limit={limit}&api_key={self.api_key}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    # Add more methods for different endpoints (e.g., drug labeling, enforcement reports)
