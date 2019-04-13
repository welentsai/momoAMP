# -*- coding: UTF-8 -*- #

import pprint
import json
import requests

from bs4 import BeautifulSoup
from _hashlib import new

def specifyAMPLibrary(soup):
    new_tag = soup.new_tag("script")
    new_tag['src'] = 'https://cdn.ampproject.org/v0.js'
    new_tag['async'] = None
    soup.head.append(new_tag)
    print(new_tag)

def specifyCharSet(soup):
    new_tag = soup.new_tag("meta", charset="utf-8")
    parent_tag = soup.head
    parent_tag.insert(0, new_tag)
#     print(parent_tag)
    
def specifyViewport(soup):
    new_tag = soup.new_tag("meta")
    new_tag['name'] = 'viewport'
    new_tag['content'] = 'width=device-width,minimum-scale=1,initial-scale=1'
    parent_tag = soup.head
    parent_tag.insert(1, new_tag)
#     print(new_tag)

def specifyCanonicalLink(soup):
    new_tag = soup.new_tag("link", rel="canonical")
    new_tag['href'] = 'https://www.google.com'
    soup.head.insert(2, new_tag)
#     print(new_tag)

def specifyAMPBoilerplate(soup):
    new_tag = soup.new_tag("style")
    new_tag['amp-boilerplate'] = None
    new_tag.string = 'body{-webkit-animation:-amp-start 8s steps(1,end) 0s 1 normal both;-moz-animation:-amp-start 8s steps(1,end) 0s 1 normal both;-ms-animation:-amp-start 8s steps(1,end) 0s 1 normal both;animation:-amp-start 8s steps(1,end) 0s 1 normal both}@-webkit-keyframes -amp-start{from{visibility:hidden}to{visibility:visible}}@-moz-keyframes -amp-start{from{visibility:hidden}to{visibility:visible}}@-ms-keyframes -amp-start{from{visibility:hidden}to{visibility:visible}}@-o-keyframes -amp-start{from{visibility:hidden}to{visibility:visible}}@keyframes -amp-start{from{visibility:hidden}to{visibility:visible}}'
    soup.head.append(new_tag)
    
    new_tag = soup.new_tag("noscript")
    new_tag_inner = soup.new_tag("style")
    new_tag_inner['amp-boilerplate'] = None
    new_tag_inner.string = 'body{-webkit-animation:none;-moz-animation:none;-ms-animation:none;animation:none}'
    new_tag.append(new_tag_inner)
    soup.head.append(new_tag)
    
#     print(new_tag)

def specifyAMPAttribute(soup):
    tag = soup.find('html')
    tag['⚡'] = None
#     print(tag)

def specifyHeadCSS(soup):
    new_tag = soup.new_tag("style")
    new_tag['amp-custom'] = None
    new_tag.string = """ 
    header {
          background: Tomato;
          color: white;
          font-size: 2em;
          text-align: center;
        }
    """
    soup.head.append(new_tag)
    
    
# main() program here
if __name__ == "__main__":
    # html file
    html_doc = """
    <!DOCTYPE html>
    <html lang="en">
      <head>
    
        <title>News Article</title>
    
      
    
        
      </head>
      <body>
        <header>
          News Site
        </header>
        <article>
          <h1>Article Name</h1>
    
          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam egestas tortor sapien, non tristique ligula accumsan eu.</p>
        </article>
        <img src="mountains.jpg">
      </body>
    </html>
    """
    
    amp_html_doc = """
        <!DOCTYPE html>
        <html ⚡>
        <head>
          <meta charset="utf-8">
          <title>My AMP Page</title>
          <link rel="canonical" href="self.html" />
          <meta name="viewport" content="width=device-width,minimum-scale=1">
          <style amp-boilerplate>body{-webkit-animation:-amp-start 8s steps(1,end) 0s 1 normal both;-moz-animation:-amp-start 8s steps(1,end) 0s 1 normal both;-ms-animation:-amp-start 8s steps(1,end) 0s 1 normal both;animation:-amp-start 8s steps(1,end) 0s 1 normal both}@-webkit-keyframes -amp-start{from{visibility:hidden}to{visibility:visible}}@-moz-keyframes -amp-start{from{visibility:hidden}to{visibility:visible}}@-ms-keyframes -amp-start{from{visibility:hidden}to{visibility:visible}}@-o-keyframes -amp-start{from{visibility:hidden}to{visibility:visible}}@keyframes -amp-start{from{visibility:hidden}to{visibility:visible}}</style><noscript><style amp-boilerplate>body{-webkit-animation:none;-moz-animation:none;-ms-animation:none;animation:none}</style></noscript>
          <script async src="https://cdn.ampproject.org/v0.js"></script>
          <style amp-custom>
            h1 {
              margin: 1rem;
            }
          </style>
        </head>
        <body>
          <h1>Hello AMPHTML World!</h1>
        </body>
        </html>
    """
    
    soup = BeautifulSoup(html_doc, 'html.parser')
    
    
    # print(soup.title)
    # print(soup.head)
    # print(soup.body)
    
#     original_tag = soup.body
#     new_tag = soup.new_tag("a", href="http://www.google.com")
#     new_tag["testAttr"] = 'testing'  #You can access a tag’s attributes by treating the tag like a dictionary
    # del new_tag['testAttr'] # remove attribute
    # print(new_tag.attrs)
#     original_tag.append(new_tag)
    
#     new_tag.string = "A new Link"
    
    # print(original_tag)
    
    # print(type(original_tag))
    
    specifyAMPLibrary(soup)
    
    specifyCharSet(soup)
    specifyCanonicalLink(soup)
    specifyViewport(soup)
    specifyAMPBoilerplate(soup)
    specifyAMPAttribute(soup)
    specifyHeadCSS(soup)
    
    
    img_tag = soup.find('img')
    img_tag.string = ""
    img_tag['width'] = 266
    img_tag['height'] = 150
    img_tag.name = 'amp-img'
    # print(img_tag)
    
    print("====================================================")
#     print(soup)
    print(soup.prettify())
    
    # print("Hello World")