import csv
import os
import requests
from requests.auth import HTTPBasicAuth

# Retrieve the server, database, username, and password from environment variables
stardog_server = os.getenv('STARDOG_SERVER')
stardog_database = os.getenv('STARDOG_DATABASE')
username = os.getenv('STARDOG_USERNAME')
password = os.getenv('STARDOG_PASSWORD')

# Check if all required environment variables are set
if not all([stardog_server, stardog_database, username, password]):
    raise ValueError("One or more required environment variables are not set")


# Define the default value for the "model" column
DEFAULT_MODEL = None


def load(filename, uri, context, model):
    """
    Load a data file into stardog, so that it appears as a named graph.
    The named graph is included in an "alias" - allowing multiple queryable data collections to co-exist.

    Todo: force entailment using the named "model" as a reasoning graph

    Parameters:
    - name: The filename of the graph.
    - uri: The URI for the named graph.
    - context: The alias (collection) graph to include the new data in.
    - [ model: The reasoning model (T-box) . ]
    """
    # Set up the headers
    with open(filename, 'r') as file:
        data = file.read()

        headers = {
            'Content-Type': 'text/turtle',
            'Accept': 'application/sparql-results+json'
        }
        # Construct the Stardog URL
        stardog_url = f"{stardog_server}/{stardog_database}?graph={uri}"

        # Send the POST request with Basic Authentication
        response = requests.put(
            stardog_url,
            headers=headers,
            data=data,
            auth=HTTPBasicAuth(username, password)
        )

        # Check if the request was successful
        if response.status_code in [200,201]:
            # Print the response JSON (assuming it's in JSON format)
            print(f"{filename} - > {uri} : {response.status_code}")
        else:
            print(f"Error: {filename} - > {uri} : {response.status_code}")
            print(response.text)


def process_csv(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row.get('filename')
            uri = row.get('uri')
            context = row.get('context')
            model = row.get('model', DEFAULT_MODEL)  # Use default model if not present

            # Call the load function with the values from the CSV row
            load(name, uri, context, model)


# Specify the path to your CSV file
csv_file_path = 'manifest.csv'

# Process the CSV file
process_csv(csv_file_path)
