""" Fetch URLs from Wayback Machine """
import urllib.parse
import requests
from requests.exceptions import RequestException

def fetch_parameters_from_wayback(domain, output_filename=None, parameter_value="FUZZ"):
    """
    Fetch unique URLs with parameters from the Wayback Machine for a given domain
    and append them to an output file or print them to the console.

    Args:
        domain (str): The domain to fetch URLs for.
        output_filename (str, optional): The name of the output file. If provided,
            unique URLs will be saved to this file. If not provided, unique URLs
            will be printed to the console. Default is None.
        parameter_value (str, optional): The value to replace query parameters with.
            Default is "FUZZ".

    Returns:
        None
    """
    try:
        data = get_wayback_data(domain)

        if data:
            interesting_extensions = get_interesting_extensions()
            urls_with_parameters = filter_urls_with_parameters(
                data, interesting_extensions, parameter_value)

            if urls_with_parameters:
                process_urls(urls_with_parameters, output_filename)
            else:
                print(f"No URLs with parameters found for {domain}.")
        else:
            print(f"No snapshots found for {domain}.")

    except RequestException as e:
        print(f"An error occurred during the request for {domain}: {e}")

def get_wayback_data(domain):
    """
    Retrieve Wayback Machine data for a given domain.

    Args:
        domain (str): The domain to fetch data for.

    Returns:
        list: A list of data records from the Wayback Machine.
    """
    wayback_url = (
        f"http://web.archive.org/cdx/search/cdx?url={domain}/*"
        "&output=json&fl=original&collapse=urlkey&limit=10000"
    )

    response = requests.get(wayback_url, timeout=3)
    data = response.json()
    return data

def get_interesting_extensions():
    """
    Get a set of file extensions considered interesting.

    Returns:
        set: A set of interesting file extensions.
    """
    return {
        '.html', '.htm', '.php', '.asp', '.aspx', '.jsp', '.js', '.css',
        '.xml', '.json', '.rss', '.atom', '.md', '.pdf', '.doc',
        '.docx', '.ppt', '.pptx', '.xls', '.xlsx', '.csv', '.zip', '.rar',
        '.tar', '.gz', '.7z', '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.ico',
        '.webp', '.woff', '.woff2', '.eot', '.ttf', '.otf', '.mp4', '.txt'
    }

def filter_urls_with_parameters(data, interesting_extensions, parameter_value):
    """
    Filter URLs with query parameters from Wayback Machine data.

    Args:
        data (list): List of data records from the Wayback Machine.
        interesting_extensions (set): Set of interesting file extensions.
        parameter_value (str): The value to replace query parameters with.

    Returns:
        list: List of URLs with modified query parameters.
    """
    urls_with_parameters = []

    for item in data:
        url = item[0]
        parsed_url = urllib.parse.urlparse(url)

        if (
            parsed_url.query and
            any(parsed_url.path.endswith(ext) for ext in interesting_extensions)
        ):
            query_params = urllib.parse.parse_qs(parsed_url.query, keep_blank_values=True)

            for param_name in query_params:
                query_params[param_name] = [parameter_value]

            query_string = urllib.parse.urlencode(query_params, doseq=True)
            modified_url = urllib.parse.urlunparse(parsed_url._replace(query=query_string))

            urls_with_parameters.append(modified_url)

    return urls_with_parameters

def process_urls(urls, output_filename):
    """
    Process URLs by either printing unique ones to the console or saving them to a file.

    Args:
        urls (list): List of URLs to process.
        output_filename (str): The name of the output file. If provided,
            unique URLs will be saved to this file. If not provided, unique URLs
            will be printed to the console.

    Returns:
        None
    """
    unique_urls = list(set(urls))
    count = len(unique_urls)
    if output_filename:
        with open(output_filename, 'a', encoding='utf-8') as output_file:
            for url in unique_urls:
                output_file.write(url + '\n')
        print(f"Filtered {count} unique URLs saved to {output_filename}")
    else:
        for url in unique_urls:
            print(url)
