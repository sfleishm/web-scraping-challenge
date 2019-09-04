from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
from IPython.display import Image 
import time

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)

def scrape_info():
    marsData = {}
    # Mars Paragraph
    browser = init_browser()
    marsurl = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(marsurl)
    print('hi')
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    marstitle = soup.find('div', class_= "content_title").find('a')
    print('hi')
    marspara = soup.find('div', class_= "article_teaser_body")
    print('hi') 
    print(marstitle.get_text())
    # print(marspara.get_text())
    # title = str(marstitle.get_text())
    # marsData['title'] = title
    # marsparagraph = str(marspara.get_text())
    # marsData['marsparagraph'] = marsparagraph    
    # marstitle = soup.find(//*[@id="page"]/div[2]/div/article/div/section/div/ul/li[1]/div/div/div[3]).text()

    marsData['title'] = marstitle.get_text()
    # marsData['title'] = marstitle
    print(marspara.contents[0])
    # marsData['marsparagraph'] = marspara.get_text()    
    print('hi')
    # trying stuff here 

    # # title = str(marstitle.get_text())
    # marsData['title'] = soup.find('div', class_= "content_title").get_text()
    # # marsparagraph = str(marspara.get_text())
    # marsData['marsparagraph'] = soup.find('div', class_= "article_teaser_body").get_text()    

    #return marsparagraph

    # Nasa Featured Image
    # jplPictureUrl = "https://www.jpl.nasa.gov/spaceimages/?search=&category=featured#submit"
    # browser.visit(jplPictureUrl)
    # xpath = '//*[@id="full_image"]'
    # results = browser.find_by_xpath(xpath)
    # img = results[0]
    # img.click()
    # html = browser.html
    # soup = BeautifulSoup(html, 'html.parser')
    # img_url = soup.find("img", class_="fancybox-image")["src"]
    # baseURL = 'https://www.jpl.nasa.gov'
    # baseWithImage = baseURL + img_url
    # baseWithImage
    
    # #return baseWithImage

    # # Mars Weather
    # marsWeatherUrl = 'https://twitter.com/MarsWxReport'
    # browser.visit(marsWeatherUrl)
    # html = browser.html
    # soup = BeautifulSoup(html, 'html.parser')
    # marsWeather = soup.find('p', class_= "TweetTextSize")
    # marsWeatherTweet = marsWeather.contents[0]
    # msplit = marsWeatherTweet.splitlines()
    # list2 = msplit[0] + ' ' + msplit[1] + ' ' + msplit[2]

    # #return list2

    # # Mars Facts
    # marsFactsUrl = 'https://space-facts.com/mars/'
    # browser.visit(marsFactsUrl)
    # html = browser.html
    # soup = BeautifulSoup(html, 'html.parser')
    # facts = soup.find('table', id="tablepress-p-mars")
    # tables = facts.find('tbody')
    # #for item in tables:
    # #    print(item.get_text())
    
    # # Mars Hemispheres
    # marsHems = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    # browser.visit(marsHems)
    
    # xpath = '//*[@id="product-section"]/div[2]/div[1]/a/img'
    # results = browser.find_by_xpath(xpath)
    # img = results[0]
    # img.click()
    # html = browser.html
    # soup = BeautifulSoup(html, 'html.parser')
    # pic1 = soup.find('li')
    # cerb = pic1.find('a')['href']
    
    # #return cerb 

    # # Second
    # browser.visit(marsHems)
    # xpath = '//*[@id="product-section"]/div[2]/div[2]/a/img'
    # results = browser.find_by_xpath(xpath)
    # img = results[0]
    # img.click()
    # html = browser.html
    # soup = BeautifulSoup(html, 'html.parser')
    # pic1 = soup.find('li')
    # schiap = pic1.find('a')['href']
    
    # #return schiap

    # # Third
    # browser.visit(marsHems)
    # xpath = '//*[@id="product-section"]/div[2]/div[3]/a/img'
    # results = browser.find_by_xpath(xpath)
    # img = results[0]
    # img.click()
    # html = browser.html
    # soup = BeautifulSoup(html, 'html.parser')
    # pic1 = soup.find('li')
    # syrtis = pic1.find('a')['href']

    # #return syrtis

    # # Fourth
    # browser.visit(marsHems)
    # xpath = '//*[@id="product-section"]/div[2]/div[4]/a/img'
    # results = browser.find_by_xpath(xpath)
    # img = results[0]
    # img.click()
    # html = browser.html
    # soup = BeautifulSoup(html, 'html.parser')
    # pic1 = soup.find('li')
    # valles = pic1.find('a')['href']
    
    # #return valles 

    # # Combine Hem
    # # hemisphere_image_urls = [
    # # {"title": "Valles Marineris Hemisphere", "img_url": valles},
    # # {"title": "Cerberus Hemisphere", "img_url": cerb},
    # # {"title": "Schiaparelli Hemisphere", "img_url": schiap},
    # # {"title": "Syrtis Major Hemisphere", "img_url": syrtis},
    # # ]
    
    browser.quit()
    
    # marsData = {
    #     "marsParagraph": marsparagraph,
    #     "imgUrl": baseWithImage,
    #     "weatherText": list2
    #     # "urls": hemisphere_image_urls
    # }
        
    
    return marsData
    
    
    