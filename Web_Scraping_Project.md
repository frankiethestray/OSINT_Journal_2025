GENERAL OBJECTIVE
This project will set up a data pipeline to collect data from a chosen source.

PARAMETERS
It is important that the data source allows data collection.  
No AI support is to be used

CHOOSING A DATA SOURCE
Google's News site (https://www.news.google.com)  was selected as a beginner friendly news site to be used for scraping.

LEGAL COSTRAINTS
The robots.txt page for the site was reviewed (https://www.news.google.com/robots.txt).  The sub-directory (https://www.news.google.com/home/) was selected to be scraped as it was allowed by the site.

User-agent: *
Disallow: /
Allow: /$
Allow: /?
Allow: /home$
Allow: /home?
Allow: /home/
Allow: /nwshp$
Allow: /topics/
Allow: /publications/
Allow: /stories/
Allow: /swg/
Allow: /about$
Allow: /about?
Allow: /about/
User-agent: Googlebot
Disallow: /
Allow: /$
Allow: /?
Allow: /home$
Allow: /home?
Allow: /home/
User-agent: CCBot
User-agent: GPTBot
User-agent: ChatGPT-User
User-agent: PerplexityBot
User-agent: anthropic-ai
User-agent: ClaudeBot
User-agent: Claude-Web
Disallow: /

METHODOLOGY
The BeautifulSoup library will be used to scrape the site and Requests library will be used to parse.  The idea is to get the main summaries of news from the site.  A pre-deployment reconnaissance of the site pages shows 'Class' 

SCRIPT
# import libraries
from bs4 import BeautifulSoup 
import requests

# Define URL to be used or site to be scraped.
url = 'https://news.google.com/home?hl=en-US&gl=US&ceid=US:en'

# Send a Get request to the site
response = requests.get(url)

# Parse using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# By Class which reprsents summary of news for the day
for element in soup.find_all(class_='Ly25Ed'):
    print(element.text)

#Storing data - Store data in data.txt file
with open('data.txt', 'w') as file:
    for item in soup.find_all(class_='Ly25Ed'):
       file.write(f'{item.text}\n')


RESULTS
Top stories
Local news
Picks for you
Top storiesBBCMoreTrump raises tariffs on Canadian goods in response to Reagan advert2 hours agoBy Max MatzaCNNMoreThe Reagan foundation did Trump a solid on tariffs – at the expense of Reagan’s ideals12 hours agoBy Aaron BlakeNewsweekMoreTrump Announces Canada Tariff Increase over Reagan Ad ‘Fraud’17 minutes agoBy Peter AitkenBBCMoreWhat's in Reagan advert that caused US-Canada trade talks to collapse?YesterdayBy Maia DaviesFull CoverageThe Washington PostMoreTrump to meet with Xi as he travels to Asia to contain trade war4 hours agoBy Katrina Northrop, Rebecca Tan & Natalie AllisonThe New York TimesMoreTrump Administration Live Updates: President to Start Asia Visit With Tariffs and China on Agenda35 minutes agoBy Sui-lee Wee, Erica L. Green & Katie RogersCNNMoreTrump’s Asia trip to test his dealmaking abilities with old rivals and new friends17 minutes agoBy Betsy KleinBBCMoreUkraine war: Trump hopes China will help bring end to Russia war12 hours agoFull CoverageNBC NewsMoreHurricane Melissa could be Jamaica's most powerful storm in history1 hour agoBy Kate Reilly & Dennis RomeroFull CoverageThe GuardianMoreTrump backer Timothy Mellon identified as donor of $130m for US troop pay during government shutdown1 hour agoBy Nina LakhaniFull Coverage

CHALLENGES
1. The main challenge here is to display the results in a more user-friendly manner. The right code is needed to make the news summaries more easily discerible or to appear in separate lines.




















 
