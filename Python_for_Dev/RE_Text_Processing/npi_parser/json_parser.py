import requests
import json
import api

def fetch_information(npi):
    """
    I/P - npi number
    What it does? - extracts API link and formats using npi, generates get response for the corresponding url.
    O/P - returns json
    """
    try:
        url = api.link.format(npi)
        response = requests.get(url)
        data = response.json()
        return data["results"][0]
    except Exception as e:
        return {"NPI":npi, "Error":str(e)}
    

def address_parser(address):
    """
    I/O - takes address field as argument
    What is does? - formats address in the required format
    O/P - returns subdictionary
    """
    return {
        "Street 1": address.get("address_1", ""),
        "Street 2": address.get("address_2", ""),
        "City": address.get("city", ""),
        "State": address.get("state", ""),
        "PIN": address.get("postal_code", ""),
        "Phone": address.get("telephone_number", ""),
        "Fax": address.get("fax_number", "")
    }

def address_subdict(data):
    """
    I/P - original dictionary extracted from API response
    What it does? - fetches Mailing address and Primary Practice Address from "address" key of the dictionary
    O/P - return address subdictionary
    """
    try:
        addresses = data["addresses"]
        return {
            "Mailing Address": address_parser(addresses[0]),
            "Primary Practice Address": address_parser(addresses[1])
        }
    except Exception as e:
        return {"Error":str(e)}

if __name__ == "__main__":
    try:
        npi = input("Enter NPI: ")
        result = fetch_information(npi)
        result["addresses"] = address_subdict(result)
        print(json.dumps(result, indent=4))
    except requests.exceptions.ConnectionError:
        print("Error in connecting to API.")
    except requests.exceptions.JSONDecodeError:
        print("Error in decoding JSON. Check NPI or URL.")