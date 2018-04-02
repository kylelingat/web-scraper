---
author:
- Somewha7
title: 'A Bit of This Coin, a Bit of That Coin'
type: Activity
---

Summary
=======

Activity for learning about web scraping in python using the Beautiful Soup library

Objective
=========

You've watched its price spike and plummet, scaring even seasoned investors, but you've psyched yourself up -- you're finally going to invest in Bitcoin! However, a fool and his money are soon parted. You've decided to scope out the market before throwing yourself in the deep end. You want to be able to regularly check on the price of Bitcoin, but who knows what might be going on in the background of those sites? They might even be burning out your CPU to mine Bitcoin for themselves! Therefore, you've decided to create a web scraper to scrape the price of bitcoin off of the the site coinmarketcap.com, so that you can keep track of the price from the safety of your terminal.

Prerequisites
=============

-   Basic usage of Python REPL


Requirements
============

-   Shell terminal or Python IDE
-   bs4 library, installed using pip install bs4
-   urllib.request library, pre-installed by python
-   A hearty interest in profit

Desired Outcomes
================

-   Basic understanding of web scraping using python

Tasks
=====

1.   Create a new python file, or create a new REPL in repl.it
2.   Import urlopen from urllib.request, and BeautifulSoup from bs4
3.   Create a function, calling it something like scrape(url):
4.   Inside the function, create a soup of the page's HTML using urlopen and BeautifulSoup
5.   Inside your function, find the price of bitcoin in USD using find (\*HINT:* you will need to use find 3 times, searching for ids / classes you found by inspecting the HTML of the website)
6.   Have the function print the price you've found
7.   Run the function, using the URL https://coinmarketcap.com/currencies/bitcoin/

### Choto Stretch Goals
-   find out how to print *just* the price, without the surrounding tags.
-   Have your code output the value it finds to a new line in a .txt file.
-   Move the webscraping out of the function, and use a cronjob to automate running the function once a day
-   Add a portion to your code that will write the date & time next to each price
# web-scraper
# web-scraper
# web-scraper
# web-scraper
