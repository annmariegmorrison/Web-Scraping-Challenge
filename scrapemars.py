# Mission to Mars web scraping app calling on news, images, weather, facts, and hemisphere information for Mars
from bs4 import BeautifulSoup
import requests
import pymongo
from splinter import Browser
import pandas as pd
import time
import re

# Initialize PyMongo to work with MongoDBs
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

def init_browser():
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)

def scrape():
    browser = init_browser()
    
    NASAurl= "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(url)
    time.sleep(2)

    html = browser.html
    soup = bs(html, 'html.parser')
    misc = soup.select_one('ul.item_list li.slide')
    title = misc.find('div', class_='content_title').get_text()
    paragraph = title.find('div', class_='article_teaser_body').get_text()

    imageurl = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)
    html = browser.html
    imagesoup = bs(html, 'html.parser')
    images = imagesoup.select_one('figure.lede a img').get("src")    
    featured_image_url = 'https://www.jpl.nasa.gov' + images

    marsweatherurl= "https://twitter.com/marswxreport?lang=en"
    browser.visit(url)
    html = browser.html
    marsweathersoup = bs(html, "html.parser")    
    twitter_list= [tag.text for tag in soup_twitter.find_all('div',{'dir':"auto"})]
    new_twitter_list= [text for text in twitter_list if 'InSight sol' in text]
    new_twitter_list[0]

    marsfactsurl= "https://space-facts.com/mars/"
    browser.visit(url)
    html = browser.html
    tables = pd.read_html(factsurl
    Marsdf = tables[0]
    Marsdf.set_index([0])
    Marsdf = Marsdf.rename(columns={0:'', 1:'Measurement'})
    Marsdf.set_index([""], inplace=True)
    Marstable = Marsdf.to_html(classes='table table-borderless table-hover table-dark')

    marshemispheresurls = []

    marshemiurl = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hem_url)
    time.sleep(5)
    hem_html = browser.html
    hem_soup = BeautifulSoup(hem_html, 'html.parser')
    tag = list(hem_soup.find_all('h3'))

    for x in range(0,4):
        browser.find_by_text(tag[x].text.strip()).click()
    
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
    
       
        image = soup.find('div', class_='downloads').find('ul').find('li')
        image_url = image.find('a')
        title = soup.find('h2', class_='title')
    

        hem_url.append({'title':title.text.strip(), 'image_url':image_url["href"]})
    
        browser.back()

    Mars_data = {'News':[news_title,
                        news_content],
                'Image': featured_url,
                'Weather': mars_weather,
                'Facts': Mars_table,
                'Hemispheres': hemisphere_image_urls}

    for index in range(len(links)):
        hemi= {}
        browser.find_by_css("a.product-item h3")[index].click()
        image= browser.find_link_by_text("Sample").first
        hemi["img_url"]= image["href"]
        hemi["title"]= browser.find_by_css("h2.title").text
        hemispheres.append(hemi)
        browser.back()
        time.sleep(5)

    mars_data = {
        "news_title": newstitle,
        "news_p": newsbody,
        "featured_image_url": featured_image_url,
        "mars_weather": new_twitter_list[0],
        "mars_table_html": mars_table_html,
        "hemispheres": hemispheres}

    browser.quit()

    return mars_data