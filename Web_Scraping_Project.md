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






User-agent: FriendlyCrawler
User-agent: img2dataset
