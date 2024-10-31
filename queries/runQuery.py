import os
import requests
from requests.auth import HTTPBasicAuth
import json
import argparse

def query(namedquery,params:dict={} ):
    # Retrieve the server, database, username, and password from environment variables
    stardog_server = os.getenv('STARDOG_SERVER')
    stardog_database = os.getenv('STARDOG_DATABASE')
    username = os.getenv('STARDOG_USERNAME')
    password = os.getenv('STARDOG_PASSWORD')

    # Check if all required environment variables are set
    if not all([stardog_server, stardog_database, username, password]):
        raise ValueError("One or more required environment variables are not set")

    # Construct the Stardog URL
    stardog_url = f"{stardog_server}/{stardog_database}/query"


    # Set up the headers and payload
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded' ,
        'Accept': 'application/sparql-results+json'
    }
    params['query'] = namedquery

    # Send the request with Basic Authentication
    response = requests.get(
        stardog_url,
        headers=headers,
        params=params,
        # data=payload,
        auth=HTTPBasicAuth(username, password)
    )

    # Check if the request was successful
    if response.status_code == 200:
        # Print the response JSON (assuming it's in JSON format)
        with open("query.json", "w") as outfile:
            print(f"Writing response to {outfile.name}")
            json.dump(response.json(), outfile, indent=4)
    else:
        print(f"Error: {response.status_code}")
        print(response.text)

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Process and post SPARQL files.')
    parser.add_argument('-q', '--query', default='getEntity' , type=str, help='named query - default is getEntity')
    parser.add_argument( '-p',
        "--params",
        type=str,
        help="Comma-separated list of key:value pairs."
    )
    # Parse command-line arguments
    args = parser.parse_args()
    params = {}
    try:
        pairs = args.params.split(',')

        for pair in pairs:
            key, value = pair.split('=')
            params["$"+key.strip()] = value.strip()
    except:
        print(f"No parameters found ({args.params})")
    # Process files in the specified directory with the given pattern
    query(args.query, params)

if __name__ == '__main__':
    main()