
import requests, re, json
from requests import Session
from bs4 import BeautifulSoup 

# Define the URLs 
root_url = "https://country-leaders.onrender.com"
countries_url = root_url + "/countries"
leaders_url = root_url + "/leaders"
cookie_url = root_url + "/cookie"
leaders_url = root_url + "/leaders"
status_url = root_url + "/status"

# Send GET request for status_url
response = requests.get(status_url)

# Check if status code is equal to 200
if response.status_code == 200:
    # If status code is 200, print the text of the response
    print(response.text)
else:
    # If status code is not 200, print the status code
    print(f"Error: Status code {response.status_code}")


"""
Function 'get_leaders' fetches information about country leaders from the country-leaders API 
and extracts the introductory paragraph from their respective Wikipedia pages.
"""
def get_leaders():
    # Create a session object 
    session = requests.Session()

    # Retrieves cookies using the session object
    response = session.get (cookie_url)
    cookies = response.cookies
    
    # Retrieve information about countries using the session object
    req = session.get (countries_url, cookies=cookies)
    countries = req.json()
    print(countries)

    # Loop over countries and save their leaders in a dictionary 
    leaders_per_country = {}  
    for country in countries:
        while True:
            try:
                leaders = requests.get(leaders_url, params={"country": country}, cookies=cookies)
                # Check if cookies have expired
                if leaders.status_code == 403:  
                    # Refresh the cookies
                    cookies = session.get(cookie_url).cookies  
                    continue
                else:
                    leaders = leaders.json()
                    leaders_per_country[country] = []
                    for leader in leaders:
                        leader["first_paragraph"] = get_first_paragraph(leader["wikipedia_url"], session)
                        leaders_per_country[country].append(leader)
                        print(f"The leader: {leader['first_name']} {leader['last_name']} from {leader['place_of_birth']}")
                        print(f"First Paragraph: {leader['first_paragraph']}")
                        print()
                break
            except Exception as e:
                print(f"An error occurred for country '{country}': {str(e)}")
                break
    return leaders_per_country
"""
The following function extracts the initial paragraph from a Wikipedia URL using a Session object.
Parameters:
    - wikipedia_url (str): The URL of the Wikipedia page.
    - session (Session): The Session object employed for request handling.
Returns:
    - first_paragraph (str): The sanitized introductory paragraph of the Wikipedia page.
"""

def get_first_paragraph (wikipedia_url, Session):
    # print(wikipedia_url)
    leader_info = Session.get (wikipedia_url)
    # Print soup.prettify
    soup = BeautifulSoup(leader_info.text, "html.parser")
    # Print paragraphs
    paragraphs = soup.find_all("p")

    for paragraph in paragraphs: 
        if paragraph.text.split():
            first_paragraph = paragraph.text
            break 
    
    # Sanitize the first paragraph by removing unwanted elements using regex
    first_paragraph= re.sub(r"\[[0-9a-zA-Z]+\]|\xa0–|\n", ' ', first_paragraph)
    return first_paragraph

"""
# Define a function save to save the 'leaders_per_country' dictionary as a ison file.
Parameters:
    leaders_per_country (dict): A dictionary containing data on leaders for each country.
"""
def save(leaders_per_country):
    with open ("leaders.json", "w") as json_file: 
        json.dump (leaders_per_country, json_file, indent = 4)
    return

leaders_per_country = get_leaders()
print(leaders_per_country)
save(leaders_per_country)
