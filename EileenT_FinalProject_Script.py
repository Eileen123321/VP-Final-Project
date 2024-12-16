#imports
import re
import sys 
from prettytable import PrettyTable
import os
from bs4 import BeautifulSoup
import requests
import nltk

url = 'https://casl.website/' 

# Define Regex Pattern
PhoneRegEx = re.compile(r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}")
ZipRegEx = re.compile(r"\b\d{5}(?:-\d{4})?\b")


# URL of all pages found on website
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

print("\nImages Found on Website:") 
# URL Links to images found on the website & URL of all pages found on the website
images = soup.findAll('img')  # Find the image tags
for eachImage in images:      # Process and display each image
    try:
        imgURL = eachImage['src']
        print(imgURL)
        if imgURL[0:4] != 'http':       # If URL path is relative
            imgURL = url+imgURL         # try prepending the base url
        
        response = requests.get(imgURL)                 # Get the image from the URL
        imageName = os.path.basename(imgURL)
        
        with open(imageName, 'wb') as outFile:
            outFile.write(response.content)
            
    except Exception as err:
        print(imgURL, err)
        continue    

print("\nPage Links:")    
links = soup.findAll('a')  # Find the url tag 
for eachLink in links:
    href = eachLink.get('href')
    if href:
        if href[0:4] != 'http' :
            href = url + href
        href = href.replace("http://", "https://")
        print(href)

# Extract Phone Numbers found on the website & Extract zip codes 
print("\nPhone Numbers and Zip Codes:")
page_text = soup.get_text(separator=' ', strip=True)  # Get all text content from the page
phone_numbers = set(PhoneRegEx.findall(page_text))  # Find all phone numbers
zip_codes = set(ZipRegEx.findall(page_text))  # Find all zip codes


print("\nPhone Numbers:")  # Print extracted phone numbers
for phone in phone_numbers:
    print(phone)


print("\nZip Codes:")  # Print extracted zip codes
for zip_code in zip_codes:
    print(zip_code)

# Find all of unique vocabulary found on website
word_regex = re.compile(r'\b\w+\b')
page_text = soup.get_text(separator=' ')
unique_vocab = set(word_regex.findall(page_text)) # Extract unique vocabulary 
print("\nUnique Vocabulary Found on Website:") # Print extracted Unique Vocabulary 
for word in sorted(unique_vocab):
    print(word)

# Find verbs using Regex
VerbRegEx = re.compile(r'\b\w+ing\b|\b\w+ed\b|\b\w+es\b|\b\w+e\b')
verbs = set(VerbRegEx.findall(page_text))   # Extract verbs 
print("\nVerbs Found on Website:")   # Print the extracted verbs
for verb in verbs:
    print(verb)
    
# Find nouns using Regex  
NounRegEx = re.compile(r'\b\w+(\s\w+)*\b')
nouns = set(NounRegEx.findall(page_text))  # Extract nouns 
print("\nNouns Found on Website:") # Print the extracted nouns 
for noun in nouns:
    print(noun)
    
