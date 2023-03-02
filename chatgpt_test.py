# import csv
# import requests
# from bs4 import BeautifulSoup

# def crawl_naver_news_articles(query):
#     # Set the URL you want to webscrape from
#     url = f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={query}"

#     # Connect to the URL
#     response = requests.get(url)

#     # Parse HTML and save to BeautifulSoup object
#     soup = BeautifulSoup(response.text, "html.parser")
#     print(soup)
#     # Find all div elements with the class "thumb_type thumb_type_best"
#     articles = soup.findAll("a", {"class": "news_tit"})
    
#     breakpoint()
#     # Create a CSV file
#     with open("articles.csv", "w", newline="") as csvfile:
#         fieldnames = ["title", "link"]
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#         writer.writeheader()

#         # For each article, find the title and link
#         for article in articles:
#             title = article['title']
#             link = article["href"]

#             # Write the article's title and link to the CSV file
#             writer.writerow({"title": title, "link": link})

# # Crawl Naver News for articles about BTS
# crawl_naver_news_articles("BTS")

import youtube_dl

# Set the URL of the video you want to download
url = "https://www.youtube.com/watch?v=pRmBn_INljM"

# Initialize the YouTube downloader
ydl = youtube_dl.YoutubeDL({'outtmpl': '%(title)s.%(ext)s'})

# Download the video
ydl.download([url])
