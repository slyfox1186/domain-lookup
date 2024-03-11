# Domain Lookup Script

The Domain Lookup Script is a comprehensive Python tool for retrieving domain information.

It leverages the `python-whois` module to collect details about domain names and offers features like IP lookup, geolocation, SSL certificate details, and more.

## Features

- **Alexa Rank**: Retrieves Alexa traffic rank.
- **Availability Check**: Checks if a domain is available for registration.
- **Domain Age**: Calculates age from the creation date.
- **Domain Dates**: Shows creation, expiration, and update dates.
- **Domain Information**: Utilizes `python-whois` for domain data.
- **HTTP Headers**: Fetches HTTP header information.
- **IP and Geolocation**: Performs IP lookup and fetches geolocation.
- **Name Servers**: Lists domain's associated name servers.
- **Output File**: Option to save results to a file.
- **Registrant Details**: Displays name, organization, and registrar.
- **SSL Certificate**: Retrieves SSL certificate validity details.
- **Verbose Mode**: Offers detailed domain information.

## Requirements

- Python 3.x
- Pip Modules:
  - `python-whois`
  - `requests`

## Installation

1. Clone the repository or download the script file.
2. Install the required dependencies:

```bash
pip install python-whois requests
```
Or use the APT package manager
```bash
apt install python3-whois
```

## Usage

Run the script from a terminal or command prompt. Navigate to the script's directory and execute:
  - You can pass multiple domains to the script

```bash
python3 domain_lookup.py <domain> <subdomain.domain> [-v] [-o output_file]
```

- `<domain/subdomain>`: Domain or subdomains to lookup.
- `-v` (optional): Enables verbose mode for more details.
- `-o output_file` (optional): Saves results to the specified file.

### Examples

```bash
python3 domain_lookup.py example.com
python3 domain_lookup.py example.com subdomain.example.com -v
python3 domain_lookup.py example.com -o results.txt
```

## Output

The script displays information for each domain, including:

- Dates: creation, expiration, update
- Domain name, availability status, and age
- Geolocation, SSL certificate details
- HTTP headers, Alexa traffic rank
- Name servers, IP address, reverse IP lookup
- Registrant, organization, and registrar details

Verbose mode reveals additional details. Specifying an output file saves the results accordingly.

## Logging

Incorporates logging for execution tracking, including timestamps, log levels, and messages, aiding in debugging and information tracking.

## Error Handling

Implements error handling for graceful failures and informative error messaging, ensuring the script continues with remaining domains after encountering an error.

## Contributing

Contributions are welcome! For bugs or feature suggestions, please open an issue or submit a pull request on GitHub.

## License

Released under the MIT License.
