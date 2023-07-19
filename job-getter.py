# scrape the deloitte jobs website for relevant jobs
# and save them to a csv file

import requests
from bs4 import BeautifulSoup
import csv
import time
import datetime
import os

# get the current date and time
now = datetime.datetime.now()
date = now.strftime("%Y-%m-%d")
time = now.strftime("%H%M%S")

# create a csv file to store the data
filename = "deloitte-jobs-" + date + "-" + time + ".csv"
csv_writer = csv.writer(open(filename, 'w'))

# write the header row
csv_writer.writerow(['date', 'time', 'title', 'location', 'link', 'clearance'])

# function for looping through job listings
def get_job_listings(job_listings):
     for job_listing in job_listings:
    
        # get the title
        title = job_listing.find('h3', class_='article__header__text__title').text.strip()
    
        # get the location that is within the third span tag inside a div tag
        location = job_listing.find('div', class_='article__header__text__subtitle').find_all('span')[2].text.strip()
    
        # get the link
        link = job_listing.find('a', class_='link')['href']

        # navigate to the job page
        link = job_listing.find('a', class_='link')['href']

        job_page = requests.get(link, headers=headers)
        job_soup = BeautifulSoup(job_page.content, 'html.parser')

        # get the job description
        job_description = job_soup.find_all('article', class_='article--details')[1].find('div', class_='article__content').text.strip()

        # search for the word 'clearance' in the job description and store thirty characters before and after
        if 'clearance' in job_description:
            clearance_index = job_description.find('clearance')
            clearance = job_description[clearance_index-30:clearance_index+30]
        else:
            clearance = 'no clearance specified'
    
        # write the data to the csv file
        csv_writer.writerow([date, time, title, location, link, clearance])

# set the headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
}

# get the html of the jobs page
url = "https://apply.deloitte.com/careers/SearchJobs/data%20engineer?sort=relevancy"
page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

# loop while there is a next page
while soup.find('a', class_='paginationNextLink'):

    # get the job listings
    job_listings = soup.find_all('article', class_='article--result')

    # loop through the job listings
    get_job_listings(job_listings)

    # get the html of the next page
    url = soup.find('a', class_='paginationNextLink')['href']
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

# print a message to the console
print("Job data has been scraped and saved to " + filename)

# print a message to the console
print("Clearance data has been scraped and saved to " + filename)

# open the csv file in Excel on a mac
os.system("open -a 'Microsoft Excel.app' " + filename)



