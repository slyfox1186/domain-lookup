# Domain Lookup Script

The Domain Lookup Script is a comprehensive Python tool for retrieving domain information. It leverages the `python3-whois` module to collect details about domain names and offers features like IP lookup, geolocation, SSL certificate details, and more.

## Features

- **Domain Information**: Utilizes `python3-whois` for domain data.
- **Availability Check**: Checks if a domain is available for registration.
- **Registrant Details**: Displays name, organization, and registrar.
- **Domain Dates**: Shows creation, expiration, and update dates.
- **Name Servers**: Lists domain's associated name servers.
- **IP and Geolocation**: Performs IP lookup and fetches geolocation.
- **SSL Certificate**: Retrieves SSL certificate validity details.
- **HTTP Headers**: Fetches HTTP header information.
- **Alexa Rank**: Retrieves Alexa traffic rank.
- **Domain Age**: Calculates age from the creation date.
- **Verbose Mode**: Offers detailed domain information.
- **Output File**: Option to save results to a file.

## Requirements

- **Python 3.x**
- **Pip Modules**:
  - `python3-whois`
  - `requests`

```bash
pip install --user python-whois requests
```

## Installation

1. Clone the repository or download the script file.
2. Install the required dependencies:

```bash
pip install python3-whois requests
```

## Usage

Run the script from a terminal or command prompt. Navigate to the script's directory and execute:

```bash
python domain_lookup.py <domain/subdomain> [-v] [-o output_file]
```

- `<domain/subdomain>`: Domain or subdomains to lookup.
- `-v` (optional): Enables verbose mode for more details.
- `-o output_file` (optional): Saves results to the specified file.

### Examples

```bash
python domain_lookup.py example.com
python domain_lookup.py example.com subdomain.example.com -v
python domain_lookup.py example.com -o results.txt
```

## Output

The script displays information for each domain, including:

- Domain name, availability status, and age
- Registrant, organization, and registrar details
- Dates: creation, expiration, update
- Name servers, IP address, reverse IP lookup
- Geolocation, SSL certificate details
- HTTP headers, Alexa traffic rank

Verbose mode reveals additional details. Specifying an output file saves the results accordingly.

## Logging

Incorporates logging for execution tracking, including timestamps, log levels, and messages, aiding in debugging and information tracking.

## Error Handling

Implements error handling for graceful failures and informative error messaging, ensuring the script continues with remaining domains after encountering an error.

## Contributing

Contributions are welcome! For bugs or feature suggestions, please open an issue or submit a pull request on GitHub.

## License

Released under the MIT License.
