from scrapper import parse_vals
import json
import maskpass

if __name__ == "__main__":
    user = input("Enter Email ID: ")
    pw = maskpass.askpass(mask="")

    all_info = {}
    parse_vals(user, pw, all_info)    
    all_info = json.dumps(all_info, indent=4)
    print(all_info)