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
The reason why I chose a screenshot of the whole page instead of randomly clicking on a specific workout and then printing it is that sometimes on the page there might be up to 3 workouts so the screenshot can contain more than one workout. This way I simply get more breathing room if I'm not liking that singled out workout the script picked out for me.

## How to Run it

- Check if you have python installed on your system: 

```
python3 --version
```

- If you already have it grab the dependencies:

```
pip install selenium webdriver-manager dropbox
```

- Modify the following placeholders with your own credentials:

    - "crossfit_login_url_here"
    - "your_email_here"
    - "your_password_here"
    - "your_screenshot_path_here"
    - "YOUR_ACCESS_TOKEN"

- After that simply go to the directory of your script and run it:

```
python3 crossfit_scraper.py
```


## Tools I've used

Selenium, various Python libraries, Powershell.
I started out with some basic BeautifulSoup for scraping and Twilio for phone notifications but I quickly abandoned that initial idea.
