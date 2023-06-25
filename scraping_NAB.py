import requests
from bs4 import BeautifulSoup

login_url = 'https://portal.notarzt-boerse.de/index/start/'
payload = {'username': 'Dr.Schleifer', 'password': 'Einsatzchecker123'}

# Create a session
session = requests.Session()

response = session.post(login_url, data=payload)


# Check the response status
if response.status_code == 200:
    # Request successful, now you can access the protected page
    protected_page = session.get(protected_url)
    print(protected_page.content)  # Print or process the protected page content as needed
else:
    print("Login failed with status code:", response.status_code)

