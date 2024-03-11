# Domain Lookup Script

The Domain Lookup Script is a Python tool that allows you to retrieve comprehensive information about domain names. It utilizes the `python3-whois` module to gather domain details and provides additional features such as IP address lookup, geolocation information, SSL certificate details, and more.

## Features
- Retrieves domain information using the `python3-whois` module
- Checks domain availability for registration
- Displays registrant name, organization, and registrar details
- Provides creation, expiration, and updated dates for the domain
- Lists name servers associated with the domain
- Retrieves IP address and performs reverse IP lookup
- Fetches geolocation information for the IP address
- Retrieves SSL certificate details, including validity period
- Fetches HTTP header information
- Retrieves Alexa traffic rank for the domain
- Calculates domain age based on creation date
- Supports verbose mode for additional domain details
- Allows saving results to an output file

## Requirements
- Python 3.x
- `python3-whois` module
- `requests` module

## Installation
Clone the repository or download the script file. Install the required dependencies using pip:

```bash
pip install python3-whois requests
```

## Usage
To use the Domain Lookup Script, open a terminal or command prompt and navigate to the directory where the script is located. Then, run the script with the following command:

```bash
python domain_lookup.py <domain/subdomain> [-v] [-o output_file]
```

- `<domain/subdomain>`: Specify one or more domain names or subdomains to lookup, separated by spaces.
- `-v` (optional): Enable verbose mode to display additional domain details.
- `-o output_file` (optional): Specify the output file name to save the results.

### Examples

```bash
python domain_lookup.py example.com
python domain_lookup.py example.com subdomain.example.com -v
python domain_lookup.py example.com -o results.txt
```

## Output
The script will display the domain information for each specified domain, including:
- Domain name and availability status
- Registrant name, organization, and registrar details
- Creation, expiration, and updated dates
- Name servers
- IP address and reverse IP lookup
- Geolocation information
- SSL certificate details
- HTTP header information
- Alexa traffic rank
- Domain age

If verbose mode is enabled, additional domain details will be displayed. If an output file is specified, the results will be saved to the specified file.

## Logging
The script includes logging functionality to capture relevant information during execution. Logs are displayed in the console and include timestamps, log levels, and messages for better tracking and debugging.

## Error Handling
The script incorporates error handling to gracefully handle potential issues and provide informative error messages. If an error occurs during domain processing, an error message will be logged, and the script will continue processing the remaining domains.

## Contributing
Contributions to the Domain Lookup Script are welcome! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request on the GitHub repository.

## License
This script is released under the MIT License.