"""
Furl.py: A script for fetching URLs with parameters from the Wayback Machine.

Usage:
    python furl.py (-d domain.com | -l list.txt) [-o output.txt]

Options:
    -d, --domain       Specify a single domain name to search for (e.g., domain.com).
    -l, --list         Specify a .txt file containing a list of domains, one per line.
    -o, --output       Specify an optional output .txt file name.
"""
import argparse
import sys
from banner import display_banner
from fetch import fetch_parameters_from_wayback
from fetch_list import fetch_parameters_from_list

def main():
    """
    This function coordinates the overall flow of your script, 
    from parsing command-line arguments to invoking the core 
    functionality and controlling the output based on the provided arguments.
    """
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-d', '--domain', help='Single domain name (e.g., domain.com)')
    group.add_argument('-l', '--list', help='Path to a .txt file containing a list of domains')

    parser.add_argument('-o', '--output', help='Specify the output .txt file name')

    args = parser.parse_args(args=None if sys.argv[1:] else ['--help'])

    if args.domain:
        fetch_parameters_from_wayback(args.domain, args.output)
    elif args.list:
        fetch_parameters_from_list(args.list, args.output)

if __name__ == "__main__":
    display_banner()
    main()
