# # Unit_12_Web_Scraping_Document_Database
# Melissa Morgan
# # Jupyter Notebook (mission_to_mars) converted to scrape_mars.py file

# Dependencies
import datetime
import pymongo
from bs4 import BeautifulSoup as bs
from splinter import Browser
import re
import pandas as pd
import time


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {
        "executable_path": r"C:/Users/Melissa Morgan/Desktop/chromedriver_win32/chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=True)


def scrape_info():
    browser = init_browser()

    # Visit the NASA News Site
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    time.sleep(1)

    # Create BeautifulSoup object; parse with 'lxml'
    html = browser.html
    soup = bs(html, "html.parser")

    newsTitle = soup.find("div", {"class": "content_title"})

    titleLink = newsTitle.find("a")

    newsTitleText = titleLink.text

    link = titleLink["href"]

    frontBit = "https://mars.nasa.gov"

    fullLink_news = frontBit + link


# Scraper #2
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)

    # Create BeautifulSoup object; parse with 'lxml'
    html = browser.html
    soup = bs(html, "html.parser")

    featImage = soup.find("article", {"class": "carousel_item"})

    link = featImage["style"].split("(")[1].replace(");", "").replace("'", "")

    frontBit = "https://www.jpl.nasa.gov"

    fullLink_featImage = frontBit + link

    # # Scraper #3
    url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(url)

    # Create BeautifulSoup object & parse
    html = browser.html
    soup = bs(html, "html.parser")

    tweet = soup.find('p', {"class": "tweet-text"})

    weather = tweet.text

    # # Scraper #4

    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)

    browser.find_by_css("a.itemLink h3")[0].click()

    # Create BeautifulSoup object & parse
    html = browser.html
    soup = bs(html, "html.parser")

    imageTitle = soup.find("h2", {"class": "title"}).text

    imageLink_panda = soup.find("img", {"class": "wide-image"})["src"]

    frontBit = "https://astrogeology.usgs.gov"
    imageLink_panda1 = frontBit + imageLink_panda

    hemi_data = []

    for i in range(4):
        hemi_dict = {}

        url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
        browser.visit(url)
        browser.find_by_css("a.itemLink h3")[i].click()

        # Create BeautifulSoup object & parse
        html = browser.html
        soup = bs(html, "html.parser")

        imageTitle = soup.find("h2", {"class": "title"}).text
        imageLink_panda = soup.find("img", {"class": "wide-image"})["src"]

        frontBit = "https://astrogeology.usgs.gov"
        imageLink_panda1 = frontBit + imageLink_panda

        hemi_dict["title"] = imageTitle
        hemi_dict["link"] = imageLink_panda1

        hemi_data.append(hemi_dict)

    hemi_data

    list_dfs = pd.read_html("https://space-facts.com/mars/")

    len(list_dfs)

    marsFacts = list_dfs[0]
    marsFacts.columns = ["Name", "Measure"]

    marsFactsHTML = marsFacts.to_html()

    browser.quit()

    # Store data in a dictionary
    mars_data = {
        'newsTitle': newsTitleText,
        'newsLink': fullLink_news,
        'featImageLink': fullLink_featImage,
        'weatherInfo': weather,
        'hemisphereInfo': hemi_data,
        'marsFacts': marsFactsHTML,
        'last_updated': datetime.datetime.utcnow()
    }

    # Return results
    return mars_data
