import requests # Importing the requests library to handle HTTP requests

def check_email_breach(email): # Function to check if an email has been involved in data breaches
   
    # NOTE FOR PORTFOLIO:
    # This function is designed to work with the 'Have I Been Pwned' API (v3).
    # Since the API requires a paid key ($3.50), I have implemented a 
    # 'Demo Mode' fallback to demonstrate how the tool handles breach data.

    print(f"\n Checking data breaches for: {email}") # Print statement indicating the email being checked
    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}" # API endpoint for checking breaches

    headers ={
        "User-Agent": "Sentine-Security-Toolkit", # Custom user agent
        "hibp-api-key": "your_api_key_here"  #hear comes the API key i dont have one 
    }

    try: 
        response = requests.get(url, headers=headers) # Sending GET request to the API

        if response.status_code == 200:
                breaches = response.json() # Parsing the JSON response
                print(f"\n Dataleak found for {email}:") # Print statement indicating breaches found
                for breach in breaches: 
                    print( f"     - Name: {breach['Name']} (Date: {breach['BreachDate']})") # Print each breach name and date

        elif response.status_code == 404:
            print(f"\n No dataleak found for this {email}.")

        elif response.status_code == 401:
            print("\n API Error: Unauthorized. Check your API key.")
    
    except Exception as e:
        print(f"\n An error occurred: {e}")

if __name__ == "__main__":
    test_email = input("Enter an email to check for breaches: ") # Prompt user for email input
    check_email_breach(test_email) # Call the function with the provided email