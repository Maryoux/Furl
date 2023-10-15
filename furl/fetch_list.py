"""
    Fetching URLs from list of domains
"""
from .fetch import fetch_parameters_from_wayback

def fetch_parameters_from_list(input_filename, output_filename=None, parameter_value="FUZZ"):
    """
    This function is used to fetch parameters from the Wayback Machine 
    for domains listed in a file and potentially save them to an output file
    """
    with open(input_filename, 'r', encoding='utf-8') as input_file:
        domains = input_file.read().splitlines()

    for domain in domains:
        fetch_parameters_from_wayback(domain, output_filename,parameter_value)
