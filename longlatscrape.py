# Fettet, Louis
# Open Data Day DC, Millennium Challenge Corporation Project
# 02/23/2013
# Scraping the Longitude and Latitude of a Country's Capital City from Google Instant Answers (Rejection of the Search API)

import urllib
from urllib import FancyURLopener

class Not_A_Bot (FancyURLopener):  
    # here we define our user-agent
    version = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.60 Safari/537.17'

not_a_bot = Not_A_Bot()                                         # initialize new instance of user-agent

def getCapital(CountryName):
    """
    Sends a query to Google for the capital of a country, and parses the 
    HTML for the search page until it finds, concatenates, and returns 
    the answer.
    """
    query = 'Capital City of ' + CountryName                    # concatenate search query
    url = 'https://www.google.com/search?num=100&q='+ query     # concatenate address
    page = not_a_bot.open(url)                                  # opens url with new user-agent
    google_answer = 'vk_ans vk_dgy answer_predicate'            # magic term for Google's instant answer
    print ("The capital of " + CountryName + " is:")
    for block in page.readlines():                              # look into each code "block"
        if google_answer in block:                              # if the term is in the block, we do a lot of parsing and concatenating...
            index = block.index(google_answer)
            start = index+len(google_answer)+2                  # getting the right index where answer starts
            end = start                                         # put end at start so we can increment correctly in the loop
            answer = ''                                         # initialize empty string
            done = False 
            while (not done):
                if block[end] == '<':                           # this will be the escape character of our answer
                    done = True                                 # so we're done!
                else:
                    answer += block[end]                        # add one character to the end of the string
                    end += 1                                    # increment end
            print answer
            return answer
    print ("Error, data could not be retrieved.")
                        
def getCoordinates(Capital, CountryName):
    """
    Returns the coordinates for a country's capital city in the same manner
    of the previous function.
    """
    query = 'Coordinates of ' + Capital + ' ' + CountryName
    url = 'https://www.google.com/search?num=100&q='+ query
    page = not_a_bot.open(url)
    google_answer = 'vk_ans vk_dgy answer_predicate'
    print ("The coordinates of " + Capital + " are:")
    for block in page.readlines():
        if google_answer in block:
            index = block.index(google_answer)
            start = index+len(google_answer)+2
            end = start
            answer = ''
            done = False
            while (not done):
                if block[end] == '<':
                    done = True
                else:
                    answer += block[end]
                    end += 1
            print answer
            return answer
    print ("Error, data could not be retrieved.")

CountryList = ['Armenia', 
               'Honduras',
               'Jordan',
               'Moldova',
               'Mongolia',
               'Nicaragua',
               'Philippines',
               'El Salvador',
               'Vanuatu',
               'Armenia',
               'Indonesia',
               'Malawi',
               'Mozambique',
               'Tanzania',
               'Kenya',
               'Lesotho',
               'Zambia',
               'Madagascar',
               'Namibia']

for country in CountryList:
    getCoordinates(getCapital(country), country)
