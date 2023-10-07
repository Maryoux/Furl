"""
Furl.py: A main script from Furl for fetching URLs with parameters from the Wayback Machine.

Usage:
    python furl.py -d domain.com [-o output.txt]

Options:
    -d, --domain       Specify the domain name to search for (e.g., domain.com).
    -o, --output       Specify an optional output .txt file name.
"""
import argparse
import sys
from banner import display_banner
from fetch import fetch_parameters_from_wayback

def main():
    """
    This function coordinates the overall flow of your script, 
    from parsing command-line arguments to invoking the core 
    functionality and controlling the output based on the provided arguments.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--domain', required=True, help='Domain name (e.g., domain.com)')
    parser.add_argument('-o', '--output', help='Specify the output .txt file name')
    args = parser.parse_args(args=None if sys.argv[1:] else ['-help'])
    fetch_parameters_from_wayback(args.domain, args.output)

if __name__ == "__main__":
    display_banner()
    main()
