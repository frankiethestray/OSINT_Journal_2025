This project will set up a data pipeline to collect data from a chosen source.
It is important that that data source we select allows data collection.  

CHOOSING A DATA SOURCE
Google Search and robots.txt :-
Using the Google search engine to querry websites that allowed webscraping resulted in a webpage titled "The 10 most scraped websites in 2025" (Octoparse)
These websites presented a strong liklihood of my web scraper working.  I decided to go with Indeed's Canadian domain (https://www.indeed.ca)
To make sure, I checked the robots.txt searching the URL https://www.indeed.ca/robots.txt.
The list of allowed files or sub-directories are printed below.  This provided a legal 'taget' for the scraper to 'peruse'.


PARSING | EXTRACTING | BY TAG
From bs4 import BeautifulSoup
import requests

url = 'https://ca.indeed.com/jobs?q=OSINT&l=Canada&from=searchOnHP&vjk=ef203914e62e1848'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# By Tag
for item in soup.find_all('h1'):
    print(item.text)

RESULT
"REQUEST IS BLOCKED"

# By Class or ID
for element in soup.find_all(class_='gnav'):
   print(element.text)
for element in soup.find_all(id='id_name'):
   print(element.text)

RESULT
Find jobs   Company Reviews   Find salaries    Sign in       Upload your resume   Sign in   Employers / Post Job   Find jobs   Company Reviews   Find salaries



Robots.txt of https://www.indeed.ca

User-agent: *
Allow: /
Allow: /hire/*?*isid=
Allow: /personeel/*?*isid=
Allow: /reclutamiento/*?*isid=
Allow: /recruiting/*?*isid=
Allow: /recrutement/*?*isid=
User-agent: Googlebot
User-agent: OAI-SearchBot
User-agent: ChatGPT-User
User-agent: Bingbot
User-agent: Slurp
User-agent: DuckDuckBot
User-agent: YahooJP
Allow: /
Allow: /hire/*?*isid=
Allow: /m/viewjob?
Allow: /personeel/*?*isid=
Allow: /reclutamiento/*?*isid=
Allow: /recruiting/*?*isid=
Allow: /recrutement/*?*isid=
Allow: /viewjob?
Allow: /
User-agent: GPTBot
User-agent: Google-Extended
User-agent: CCBot
User-agent: anthropic-ai
User-agent: FacebookBot
User-agent: AmazonBot
User-agent: Applebot-Extended
User-agent: Bytespider
User-agent: Baiduspider
User-agent: cohere-training-data-crawler



REFERENCES
https://www.octoparse.com/blog/top-10-most-scraped-websites
https://www.indeed.ca
https://www.indeed.ca/robots.txt


User-agent: FriendlyCrawler
User-agent: img2dataset
