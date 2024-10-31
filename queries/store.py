import os
import glob
import sys
import requests
import argparse
from requests.auth import HTTPBasicAuth

# Retrieve the server, database, username, and password from environment variables
stardog_server = os.getenv('STARDOG_SERVER')
stardog_database = os.getenv('STARDOG_DATABASE')
username = os.getenv('STARDOG_USERNAME')
password = os.getenv('STARDOG_PASSWORD')

# Check if all required environment variables are set
if not all([stardog_server, stardog_database, username, password]):
    raise ValueError("One or more required environment variables are not set")



def store_query(file_path):
    """
    Loads the content of a .sparql file and posts it to a specified URL.

    Parameters:
    - file_path: Path to the .sparql file.
    - url: The URL to which the file content will be posted.
    """
    try:
        # Read the content of the .sparql file
        with open(file_path, 'r') as file:
            sparql_query = file.read()

        file_base=os.path.basename(file_path).split('.')[0]

        # Construct the Stardog URL
        stardog_url = f"{stardog_server}/admin/queries/stored"

        headers = {
            'Content-Type': 'text/turtle',
            'Accept': 'application/sparql-results+json'
        }
        payload = f'''@prefix system: <http://system.stardog.com/> .

                system:Query_prov_{file_base}
                    a system:StoredQuery, system:SharedQuery , system:ReasoningQuery ;
               system:queryName "{file_base}" ;
               system:queryString "{sparql_query}" ;
               system:queryCreator "{username}" ;
               system:queryDatabase "{stardog_database}" .
   '''

        # Send the PUT request with Basic Authentication
        response = requests.put(
            stardog_url,
            headers=headers,
            data=payload,
            auth=HTTPBasicAuth(username, password)
        )

        # Check if the request was successful
        if response.status_code != 204:
            print(f"Error: {response.status_code}")
            print(response.text)
    except Exception as e:
        print(f"Error processing {file_path}: {e}")


def process_sparql_files(directory='.', pattern='*.sparql'):
    """
    Finds all .sparql files in the given directory and posts them to a specified URL.

    Parameters:
    - directory: The directory to search for .sparql files.
    - url: The URL to which the file content will be posted.
    """
    # Use glob to find all .sparql files in the specified directory
    sparql_files = glob.glob(os.path.join(directory, pattern))

    # Process each .sparql file
    for sparql_file in sparql_files:
        store_query(sparql_file)

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Process and post SPARQL files.')
    parser.add_argument('-d', '--directory', default='.' , type=str, help='The directory containing the files')
    parser.add_argument('-p', '--pattern', default='*.sparql', type=str, help='The file pattern to match (e.g., *.sparql)')


    # Parse command-line arguments
    args = parser.parse_args()

    # Process files in the specified directory with the given pattern
    process_sparql_files(args.directory, args.pattern)

if __name__ == '__main__':
    main()