"""
Furl.py: A script for fetching URLs with parameters from the Wayback Machine.

Usage:
    python furl.py -d domain.com [-o output.txt]

Options:
    -d, --domain       Specify the domain name to search for (e.g., domain.com).
    -o, --output       Specify an optional output .txt file name.
"""
import argparse
import urllib.parse
import requests
from requests.exceptions import RequestException

def fetch_parameters_from_wayback(domain, output_filename=None):
    """
    This function is used to fetch URLs with parameters from the Wayback Machine 
    for a given domain and potentially save them to an output file
    """
    wayback_url = (
        f"http://web.archive.org/cdx/search/cdx?url={domain}/*"
        "&output=json&fl=original&collapse=urlkey&limit=10000"
    )

    try:
        response = requests.get(wayback_url, timeout=3)
        data = response.json()

        if data:
            interesting_extensions = {'.html', '.php', '.asp', '.aspx', '.jsp', '.js', '.css'}
            urls_with_parameters = []

            for item in data:
                url = item[0]
                parsed_url = urllib.parse.urlparse(url)

                # Check if the URL has query parameters and the extension is interesting
                if (
                    parsed_url.query and
                    any(parsed_url.path.endswith(ext) for ext in interesting_extensions)
                ):
                    urls_with_parameters.append(url)

            if urls_with_parameters:
                if output_filename:
                    with open(output_filename, 'w', encoding='utf-8') as output_file:
                        for url in urls_with_parameters:
                            output_file.write(url + '\n')
                    print(f"Filtered URLs saved to {output_filename}")
                else:
                    for url in urls_with_parameters:
                        print(url)
            else:
                print(f"No URLs with parameters found for {domain} in the Wayback Machine.")
        else:
            print(f"No snapshots found for {domain} in the Wayback Machine.")

    except RequestException as e:
        print(f"An error occurred during the request: {e}")

def main():
    """
    This function coordinates the overall flow of your script, 
    from parsing command-line arguments to invoking the core 
    functionality and controlling the output based on the provided arguments.
    """
    parser = argparse.ArgumentParser(description="Fetch parameters from the Wayback Machine")
    parser.add_argument('-d', '--domain', required=True, help='Domain name (e.g., domain.com)')
    parser.add_argument('-o', '--output', help='Specify the output .txt file name')

    args = parser.parse_args()
    fetch_parameters_from_wayback(args.domain, args.output)

if __name__ == "__main__":
    main()
