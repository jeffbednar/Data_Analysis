from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import time
import requests



def init_browser():
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    return Browser("chrome", **executable_path, headless=False)

mars_data = {}

def marsnews():
    browser = init_browser()
    news_url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(news_url)
    news_html = browser.html
    news_soup = bs(news_html, 'html.parser')
    news_title = news_soup.find('div', class_="list_text").find('div', class_="content_title").text
    news_p = news_soup.find('div', class_="article_teaser_body").text
    mars_data['news_title'] = news_title
    mars_data['news_p'] = news_p
    browser.quit()
    return mars_data

def marsimage():
    browser = init_browser()
    image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(image_url)
    browser.find_by_id('full_image').click()
    time.sleep(4)
    browser.click_link_by_partial_text('more info')
    time.sleep(4)
    image_html = browser.html
    image_soup = bs(image_html, 'html.parser')
    image = image_soup.find('img', class_='main_image').get('src')
    featured_image_url = "https://www.jpl.nasa.gov" + image
    mars_data['featured_image'] = featured_image_url
    browser.quit()
    return mars_data

# def marsweather():
#     browser = init_browser()
#     weather_url = 'https://twitter.com/marswxreport?lang=en'
#     browser.visit(weather_url)
#     time.sleep(5)
#     browser.execute_script("window.scrollTo(200, document.body.scrollHeight);")
#     time.sleep(3)
#     weather_html = browser.html
#     soup = bs(weather_html, 'html.parser')
#     result = soup.find_all('div', attrs={'data-testid': 'tweet'})
#     weather=result[0].find_all('span', class_='css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0')
#     for tweet in weather:
#         if tweet.text.startswith('InSight'):
#             mars_weather = tweet.text
#     mars_data['mars_weather'] = mars_weather
#     browser.quit()
#     return mars_data
    
def marsfacts():
    browser = init_browser()
    pandas_url = 'https://space-facts.com/mars/'
    browser.visit(pandas_url)
    facts_data = pd.read_html(pandas_url)
    facts_df = facts_data[0]
    facts_df.columns = ['Description', 'Value']
    facts_df.set_index('Description', inplace=True)
    mars_facts = facts_df.to_html()
    mars_facts.replace('\n', '')
    mars_data['mars_facts'] = mars_facts
    browser.quit()
    return mars_data

def marshemisphere():
    browser = init_browser()
    hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hemispheres_url)

    hemispheres_html = browser.html

    hemisphere_soup = bs(hemispheres_html, 'html.parser')

    info = hemisphere_soup.find_all('div', class_='item')

    main_hemisphere_url = "https://astrogeology.usgs.gov"

    hemisphere_image_urls = []


    for i in info:
        title = i.find('h3').text
        title = title.replace('Enhanced','')
        hemi_image_url = i.find('a', class_='itemLink product-item')['href']
        browser.visit(main_hemisphere_url + hemi_image_url)
        image_html = browser.html
        image_soup = bs(image_html, 'html.parser')
        img_url = main_hemisphere_url + image_soup.find('img', class_='wide-image')['src']
        hemisphere_image_urls.append({"title" : title, "img_url" : img_url })
        mars_data['hemisphere_images'] = hemisphere_image_urls
    browser.quit()
    return mars_data

    


