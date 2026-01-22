import requests

def check_email_breach(email):
    print(f"\n[*] Checking XposedOrNot database for: {email}")
    
    # De officiële API URL voor XposedOrNot
    url = f"https://api.xposedornot.com/v1/check-email/{email}"

    # We hebben alleen een User-Agent nodig, GEEN API-key!
    headers = {
        "User-Agent": "Sentinel-Security-Toolkit"
    }

    try: 
        response = requests.get(url, headers=headers)

        # 200 = Lekken gevonden
        if response.status_code == 200:
            data = response.json()
            # XposedOrNot zet de lekken in een lijst genaamd 'breaches'
            breaches = data.get('breaches', [])
            
            print(f"\n [!] WAARSCHUWING: Dataleaks gevonden voor {email}:")
            for breach in breaches: 
                # XposedOrNot stuurt vaak alleen de namen als tekst in een lijst
                print(f"     - Gevonden in: {breach}")

        # 404 = Geen lekken gevonden (veilig!)
        elif response.status_code == 404:
            print(f"\n [+] Veilig: Geen datalekken gevonden voor {email}.")
            
        else:
            print(f"\n [-] Server reageerde met status: {response.status_code}")
    
    except Exception as e:
        print(f"\n [-] Er is een fout opgetreden: {e}")

if __name__ == "__main__":
    test_email = input("Enter an email to check for breaches: ")
    check_email_breach(test_email)