# Performing Web Scraping to fetch data from Google Scholar 

import requests
import time
import os
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd

class GoogleScholarScraper:
    def __init__(self):
        pass

    # Function for fetching the data from a profile link
    
    def get_data_from_profile_link(self, profile_link):
        
        # Mimicking a web browser 
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        response = requests.get(profile_link, headers=headers)

        if response.status_code == 200:
            
            soup = BeautifulSoup(response.text, 'html.parser') # Return the raw html
            
            name_element = soup.find('div', {'id': 'gsc_prf_in'})
            citations_element = soup.find('td', {'class': 'gsc_rsb_std'})
            h_index_element = soup.find('td', string='h-index').find_next('td') if citations_element else None
            i10_index_element = soup.find('td', string='i10-index').find_next('td') if citations_element else None

            name = name_element.text.strip() if name_element else "Name not found"
            citations = citations_element.text.strip() if citations_element else "Citations not found"
            h_index = h_index_element.text.strip() if h_index_element else "H-Index not found"
            i10_index = i10_index_element.text.strip() if i10_index_element else "i10-Index not found"

            # Returning the data
            
            return {
                'Name': name,
                'Citations': citations,
                'H_Index': h_index,
                'i10_Index': i10_index
            }
        else:
            print(f"Failed to fetch data for {profile_link}")
            return None

    def scrapingMultipleFaculties(self,profile_links,output_file='allFacultyDataUpdated5.xlsx'):
        dataList = []

        for profile_link in profile_links:
            faculty_data = self.get_data_from_profile_link(profile_link)
            if faculty_data:
                dataList.append(faculty_data)
    
        df = pd.DataFrame(dataList)
        df.to_excel(output_file, index=False)
        print(f'Data saved to {output_file}')

profile_links = [
     "https://scholar.google.com/citations?user=tuUO7DQAAAAJ&hl=en&oi=ao",
     "https://scholar.google.com/citations?user=-ZYIiGAAAAAJ&hl=en",
     "https://scholar.google.com/citations?hl=en&user=5Dl7tEYAAAAJ",
     "https://scholar.google.co.in/citations?user=2rePIXIAAAAJ&hl=en",
     "https://scholar.google.co.in/citations?user=jTCHV4kAAAAJ&hl=en",
     "https://scholar.google.co.in/citations?user=_bbxYHsAAAAJ&hl=en&authuser=1",
     "https://scholar.google.com/citations?user=bn6WQUoAAAAJ",
     "https://scholar.google.com/citations?hl=en&user=ThELNO0AAAAJ",
     "https://scholar.google.co.in/citations?user=ryhyx4IAAAAJ&hl=en",
     "https://scholar.google.com/citations?user=prcv4fAAAAAJ&hl=en&oi=ao",
     "https://scholar.google.com/citations?user=eu_o414AAAAJ&hl=en",
     "https://scholar.google.com/citations?hl=en&user=uZXv4XIAAAAJ",
     "https://scholar.google.com/citations?user=Cf2I4OoAAAAJ&hl=en",
     "https://scholar.google.com/citations?hl=en&user=Li0r8uMAAAAJ",
     "https://scholar.google.co.in/citations?user=FlLJ1SYAAAAJ&hl=en",
     "https://scholar.google.com/citations?user=vjZ4yC0AAAAJ&hl=en&authuser=1",
     "https://scholar.google.co.in/citations?user=AIdTGncAAAAJ&hl=en",
     "https://scholar.google.com/citations?user=XPjU9AIAAAAJ&hl=en&authuser=1",
     "https://scholar.google.co.in/citations?hl=en&user=Z34wmvMAAAAJ",
     "https://scholar.google.com/citations?user=vGJxAzEAAAAJ&hl=en",
     "https://scholar.google.com/citations?user=hlTGb-0AAAAJ&hl=en",
     "https://scholar.google.co.in/citations?user=hC5psv4AAAAJ",
     "https://scholar.google.com/citations?user=cE0jxPcAAAAJ&hl=en",
     "https://scholar.google.com/citations?user=IJvuo6cAAAAJ&hl=en",
     "https://scholar.google.com/citations?user=GYjXshwAAAAJ",
     "https://scholar.google.com/citations?hl=en&user=HKK_hlsAAAAJ",
     "https://scholar.google.co.in/citations?user=qIFXtnYAAAAJ&hl=en",
     "https://scholar.google.com/citations?hl=en&user=FmtW9kIAAAAJ",
     "https://scholar.google.com/citations?user=_89sYcIAAAAJ&hl=en&oi=ao",
     "https://scholar.google.com/citations?user=qVkPhiAAAAAJ&hl=en",
     "https://scholar.google.co.in/citations?user=Hj3_OtwAAAAJ&hl=en",
     "https://scholar.google.co.in/citations?user=kNdafyoAAAAJ&hl=en",
     "https://scholar.google.com/citations?hl=en&user=TIywHAYAAAAJ",
     "https://scholar.google.co.in/citations?user=YzvzznoAAAAJ&hl",
     "https://scholar.google.co.in/citations?user=Mz8UAz8AAAAJ&hl=en",
     "https://scholar.google.com/citations?user=5DpheNgAAAAJ&hl=en&authuser=1",
     "https://scholar.google.com/citations?user=ORmwBEQAAAAJ&hl=en&authuser=1",
     "https://scholar.google.com/citations?user=6_DGZukAAAAJ&hl=en&oi=ao",
     "https://scholar.google.com/citations?user=BmSboYDhzK0C&hl=en",
     "https://scholar.google.com/citations?hl=en&user=IkDN14UAAAAJ&view_op=list_works&sortby=pubdate",
     "https://scholar.google.com/citations?user=i4ZqOsMAAAAJ&hl=en",
     "https://scholar.google.co.in/citations?user=3pimobEAAAAJ&hl=en",
     "https://scholar.google.com/citations?user=xfJLs0UAAAAJ&hl=en",
     "https://scholar.google.com/citations?user=fYTPxK8AAAAJ&hl=en&oi=sra",
     "https://scholar.google.com/citations?hl=en&user=Ac5HrokAAAAJ",
     "https://scholar.google.com/citations?user=-M-lmeUAAAAJ&hl=en"
     
    
    ] # Testing with multiple faculty

scraper = GoogleScholarScraper()
scraper.scrapingMultipleFaculties(profile_links)

