import requests

def check_email_breach(email):
    print(f"\n[*] Checking XposedOrNot database for: {email}")
    
    
    url = f"https://api.xposedornot.com/v1/check-email/{email}"

    
    headers = {
        "User-Agent": "Sentinel-Security-Toolkit"
    }

    try: 
        response = requests.get(url, headers=headers)

        
        if response.status_code == 200:
            data = response.json()
            #
            breaches = data.get('breaches', [])
            
            print(f"\n [!] WAARSCHUWING: Dataleaks gevonden voor {email}:")
            for breach in breaches: 
                
                print(f"     - Gevonden in: {breach}")

        
        elif response.status_code == 404:
            print(f"\n [+] Veilig: Geen datalekken gevonden voor {email}.")
            
        else:
            print(f"\n [-] Server reageerde met status: {response.status_code}")
    
    except Exception as e:
        print(f"\n [-] Er is een fout opgetreden: {e}")

if __name__ == "__main__":
    test_email = input("Enter an email to check for breaches: ")
    check_email_breach(test_email)