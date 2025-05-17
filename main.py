import phonenumbers
import requests
import subprocess
from phonenumbers import geocoder
from art import tprint

API_KEY = 'd08bc5d5348fb0c4748066d3866cfc3c'
API_URL = 'http://apilayer.net/api/validate'

COUNTRY_FILES = {
    'FR': 'fr.txt',
    'IL': 'il.txt',
    'JO': 'jo.txt',
    'ES': 'es.txt',
    'US': 'us.txt',
    'DE': 'de.txt',
    'GB': 'gb.txt',
    'IT': 'it.txt'
}

def print_header():
    tprint("Created by Yousef")
    print("This is an OSINT tool for phone numbers.")
    print("-" * 40)

def get_phone_info(number):
    full_url = f"{API_URL}?access_key={API_KEY}&number={number}"
    try:
        response = requests.get(full_url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"[Error] API request failed: {e}")
        return None

def display_info(info):
    print("Phone Information:")
    for key in ["number", "local_format", "international_format", "country_prefix",
                "country_code", "country_name", "location", "carrier", "line_type"]:
        print(f"{key.replace('_', ' ').title()}: {info.get(key, 'N/A')}")

def search_in_country_file(number, country_code, local_format=None):
    filename = COUNTRY_FILES.get(country_code)
    if filename:
        print(f"\n[Searching in {filename}]")
        try:
            subprocess.run(["grep", number, filename])
            if local_format:
                subprocess.run(["grep", local_format, filename])
        except FileNotFoundError:
            print(f"[Error] File '{filename}' not found.")
    else:
        print(f"No local file configured for country code: {country_code}")

def run_truecaller_lookup(number):
    print("\n[Running TruecallerJS search]")
    try:
        subprocess.run(["truecallerjs", "-s", number])
    except FileNotFoundError:
        print("TruecallerJS not installed or not found in PATH.")

def main():
    print_header()
    number_input = input("Enter your number without +: ").strip()
    number = "+" + number_input

    phone_info = get_phone_info(number_input)
    if not phone_info or not phone_info.get("valid"):
        print("[!] Invalid number or API error.")
        return

    display_info(phone_info)
    search_in_country_file(number_input, phone_info.get("country_code"), phone_info.get("local_format"))
    run_truecaller_lookup(number)

    print("\nGoodbye!")

if __name__ == "__main__":
    main()
