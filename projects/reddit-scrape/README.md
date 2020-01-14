# reddit-scrape
This little program uses PRAW, and Pandas to scrape the top 100 posts from r/learnpython and store the results in a csv file called `learpython-data.csv`.

### Using `reddit-scrape`:

You will need to create a reddit app. You are going to need the app's client id, client secret, and a username and password.

1. First clone this repo to your machince.

2. `cd` into the the `reddit-scrape` directory. Example: `cd python/reddit-scrape`

3. Make sure you edit scrape.py and put in your client id, client secret, username, and password. You can also change what subreddit it will scrape by changing line 12 `subreddit = reddit.subreddit('learnpython')`. Just change learnpython to the name of the subreddit you wish to scrape. You may also want to change `learnpython-data.csv` on line 43 to a more fiting name.

4. Run `python scrape.py`

5. Enjoy.
