from r2r.client import R2RClient

# Initialize the client with the base URL of your API
base_url = "http://localhost:8000"
client = R2RClient(base_url)

# # Perform a search
print("Searching remote db...")
search_response = client.search("Hey I want the latest airpods")

print(f"Search response:\n{search_response}\n\n")
