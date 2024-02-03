from bs4 import BeautifulSoup

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
        
            # write with \n
            file2.write(cleanText.upper())

SoupUp("thing.html", "hehe.txt")







