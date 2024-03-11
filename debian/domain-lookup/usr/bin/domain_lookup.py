#!/usr/bin/python3

import whois
import sys
import socket
import requests
import ssl
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

def format_dates(dates):
    if isinstance(dates, list):
        return dates[0].strftime('%m-%d-%Y %H:%M:%S UTC')
    elif dates:
        return dates.strftime('%m-%d-%Y %H:%M:%S UTC')
    else:
        return "N/A"

def get_reverse_ip(ip_address):
    try:
        return socket.gethostbyaddr(ip_address)[0]
    except socket.herror:
        return "No reverse DNS record found"
    except Exception as e:
        return f"Error retrieving hostname"

def get_geolocation(ip_address):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip_address}")
        data = response.json()
        return f"Geolocation:\n  - Country: {data['country']}\n  - City: {data['city']}\n  - ISP: {data['isp']}"
    except Exception as e:
        return "Error retrieving geolocation"

def get_ssl_info(domain_name):
    try:
        context = ssl.create_default_context()
        with socket.create_connection((domain_name, 443), timeout=10) as sock:
            with context.wrap_socket(sock, server_hostname=domain_name) as ssock:
                cert = ssock.getpeercert()
                valid_from = datetime.strptime(cert['notBefore'], '%b %d %H:%M:%S %Y %Z').strftime('%m-%d-%Y %H:%M:%S UTC')
                valid_until = datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y %Z').strftime('%m-%d-%Y %H:%M:%S UTC')
                return f"SSL Valid:\n  - From:  {valid_from}\n  - Until: {valid_until}"
    except Exception as e:
        return "Error retrieving SSL certificate"

def get_http_headers(domain_name):
    try:
        response = requests.get(f"http://{domain_name}", timeout=10)
        headers = response.headers
        key_headers = ['Server', 'Content-Type', 'Last-Modified']
        header_info = "\n".join([f"  - {header}: {headers.get(header, 'Not Available')}" for header in key_headers])
        return header_info
    except requests.ConnectionError:
        return "Could not establish a connection"
    except requests.Timeout:
        return "Connection timed out"
    except Exception as e:
        return "Error retrieving HTTP headers"

def get_alexa_rank(domain_name):
    try:
        response = requests.get(f"http://data.alexa.com/data?cli=10&url={domain_name}")
        rank = response.text.split('<POPULARITY URL')[1].split('TEXT="')[1].split('"')[0]
        return f"Alexa Traffic Rank: {rank}"
    except Exception as e:
        return "Alexa Traffic Rank: N/A"

def calculate_domain_age(creation_date):
    if isinstance(creation_date, list):
        creation_date = creation_date[0]
    if creation_date:
        age = datetime.now() - creation_date
        return f"Domain Age: {age.days // 365} Years, {age.days % 365} Days"
    return "Domain Age: N/A"

def display_info(domain_info, domain_name, verbose=False):
    output = [f"\n{'=' * 40}\n\nDomain: {domain_name}"]

    output.append(f"Registrant Name: {domain_info.name}")
    output.append(f"Registrant Organization: {domain_info.org}")
    output.append(f"Registrar: {domain_info.registrar}")

    output.append(f"\nCreation Date: {format_dates(domain_info.creation_date)}")
    output.append(f"Expiration Date: {format_dates(domain_info.expiration_date)}")
    output.append(f"Updated Date: {format_dates(domain_info.updated_date)}")

    nameservers = sorted(set([ns.lower() for ns in domain_info.name_servers]))
    if nameservers:
        output.append("\nName Servers:")
        for ns in nameservers:
            output.append(f"  - {ns}")

    if domain_info.dnssec:
        output.append(f"\nDNSSEC: {domain_info.dnssec}")

    if domain_info.emails:
        output.append("\nContact Emails:")
        if isinstance(domain_info.emails, list):
            output.extend([f"  - {email}" for email in domain_info.emails])
        else:
            output.append(f"  - {domain_info.emails}")

    try:
        ip_address = socket.gethostbyname(domain_name)
        output.append(f"\nIP Address: {ip_address}")
        output.append(f"Reverse IP: {get_reverse_ip(ip_address)}")
        output.append(f"\n{get_geolocation(ip_address)}")
    except Exception as e:
        output.append("\nIP Address: Error retrieving IP")

    output.append(f"\n{get_alexa_rank(domain_name)}")
    output.append(f"{calculate_domain_age(domain_info.creation_date)}")

    http_headers = get_http_headers(domain_name)
    if http_headers.startswith("Error") or http_headers.startswith("Could not") or http_headers.startswith("Connection timed"):
        output.append(f"\nHTTP Header Information: {http_headers}")
    else:
        output.append("\nHTTP Header Information:")
        output.append(http_headers)

    ssl_info = get_ssl_info(domain_name)
    if "SSL Valid:" in ssl_info:
        output.append("\n" + ssl_info)
    else:
        output.append("\nSSL Information: " + ssl_info)

    if verbose:
        output.append("\n[Verbose Mode]")
        if hasattr(domain_info, 'status'):
            output.append(f"  Domain Status: {domain_info.status}")
        if hasattr(domain_info, 'whois_server'):
            output.append(f"  Whois Server: {domain_info.whois_server}")

    return "\n".join(output)

def is_domain_available(domain):
    try:
        whois_result = whois.whois(domain)
        return not bool(whois_result.domain_name)
    except Exception as e:
        return False

def process_domains(domains, verbose=False, output_file=None):
    results = []
    for domain in domains:
        try:
            domain_info = whois.whois(domain)
            if not domain_info.domain_name:
                availability = is_domain_available(domain)
                result = f"Domain '{domain}' is {'available' if availability else 'not available'} for registration."
            else:
                result = display_info(domain_info, domain, verbose)
        except Exception as e:
            result = f"An error occurred while processing '{domain}'. Please check the logs for more information."

        results.append(result)

    final_output = "\n".join(results)
    print(final_output)

    if output_file:
        try:
            with open(output_file, "w") as file:
                file.write(final_output)
        except IOError as e:
            pass

def main():
    if len(sys.argv) < 2:
        print(f"Usage: python3 {sys.argv[0]} <domain/subdomain> [-v] [-o output_file]")
        sys.exit(1)

    verbose = "-v" in sys.argv
    output_file_flag = "-o" in sys.argv
    output_file = sys.argv[sys.argv.index("-o") + 1] if output_file_flag and sys.argv.index("-o") + 1 < len(sys.argv) else None
    domain_list = [arg for arg in sys.argv[1:] if arg != "-v" and arg != "-o" and arg != output_file]

    process_domains(domain_list, verbose, output_file)

if __name__ == "__main__":
    main()