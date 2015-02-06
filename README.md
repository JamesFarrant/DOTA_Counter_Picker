# DotaHut-Scraper
Scrapes Dota Hut (www.dotahut.com), and according to user input (ie, hero name) prints counters to that hero

02/02/2015
Currently outputs counters to any hero in text form to the console

05/02/2015
Cleaned up a lot of the messier code that got us started.
hero_dictionary stored counter_dictionary as Counter_dictionary.txt by using the commented out for loop, which we will use to be the basis of our user input from now on instead of scraping dotahut every time. Json.loads is commented out at the moment because I'm not entirely sure what it does. This should become clear tomorrow. Counter_dictionary.txt contains each hero and their counters.

06/02/2015
Cleaned even more code. Established a better framework for the scraper now that it's out of its formative stages. Got rid of a lot of un-needed commented out things, added in a counter score for heroes and actually trialed its input today by picking according to its predictions in two games of DOTA.
