# Crossfit_Workouts_Web_Scraper

If your go-to crossfit gym is now addicted to giving 90 burpees every other day this python script will pick a better alternative for your training session.

## Description 

The main automation events are:

- The script logs in your official CrossFit account.
- Selects the 'workouts' tab and from a couple of drop-down menus it picks a random month and a year (as far back as 2001). 
- After that it randomly scrolls down (or stays put) over the list of workouts that are now listed.
- Grabs a screenshot, saves it to your computer.
- Finally it uploads it to your Dropbox account using your Dropbox API key.

There are many other small pieces of logic and QoL tweaks but these are the most important stops of the script.
The reason why I chose a screenshot of the page instead of randomly clicking on a specific workout and then printing it is that sometimes on the workouts page there might be up to 3 workouts so the script screenshots 3 instead of 1. This way I simply get more breathing room if I'm not feeling the single workout the script picks out for me.

## Tools I've used

Selenium, various Python libraries, Powershell.
I started out with some basic BeautifulSoup for scraping and Twilio for phone notifications but I quickly abandoned that initial idea.
