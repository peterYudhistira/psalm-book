from bs4 import BeautifulSoup
import requests
import re

def SoupUp(inputPath:str, outputPath:str):
    with open(inputPath, 'r') as file1, open(outputPath, 'w') as file2:
      
        # Read the content of the file
        html_content = file1.read()

        # Parse the HTML content
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # get all <p>
        pList = soup.find_all("p")
        
        for p in pList:
            # clean the formatting
            cleanText = ' '.join(p.text.split()) + '\n'

            # regex to clean it
            purgedString = re.sub(r'[^a-zA-Z0-9\s.,!?]', '', cleanText)
    
            # write with \n
            file2.write(purgedString.upper())

def SoupSpotify(spotifyURL:str, outputPath:str):
    # with open(outputPath, 'w') as outputFile:
    #     # attempt to scrape it
    #     soup = BeautifulSoup()
    # Specify the URL to scrape

    with open(outputPath, 'w') as outputFile:
        url = spotifyURL
        response = requests.get(url)
        if response.status_code == 200:
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find the div with class "contentSpacing"
            content_div = soup.find('div', class_='contentSpacing')

            # get all <p>
            pList = content_div.find_all("p")
            
            for p in pList:
                # clean the formatting
                cleanText = ' '.join(p.text.split()) + '\n'
            
                # regex to clean it
                purgedString = re.sub(r'[^a-zA-Z0-9\s.,!?]', '', cleanText)
        
                # write with \n
                outputFile.write(purgedString.upper())


# SoupSpotify('https://open.spotify.com/track/72QQbuZJx5rfz5GlNAAsVC', 'static/text/hehe.txt')
SoupUp('static/text/thing.html','static/text/hehe.txt')



