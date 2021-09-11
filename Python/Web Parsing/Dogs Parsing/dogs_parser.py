"""
Program to parsing dogs data from 'https://www.dogbreedslist.info/'
                                  '/all-dog-breeds/' section

***************************
*This program has been run*
***************************
    Processor -> 'AMD A6'
    Platform  -> 'LINUX, Kernel verssion 5.11.0-16-generic'
    OS        -> 'Unbuntu 21.04'
This program is written only in python.
Don't use non-standard libraries.

WARNING!
--------
    This script may not work if you рун it.
    It's because this isn't a universal program and by and largemay work correctly
    only at the moment when it is written, depends on the operation of this
    website,the code it contains.
At the time of writing, the program was working correctly, as a result,
the existing file were presented in a tabular format,
in which all the necessary data was collected.
*******************
"""
# Importing needed modules
import requests
from bs4 import BeautifulSoup as bs
import csv


"""
HEADERS we need to send with 'HTTP' requests that
the site where we want to parse data, thinks, which
those requests doing just browser and don't blocking us
"""
HEADERS = {'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)\
                          Chrome/92.0.4515.107 Safari/537.36",
           'accept': "*/*"}
URL = "https://www.dogbreedslist.info/all-dog-breeds/"


def getHtml(url, params=None):
    """
    Funciton to get 'HTTP' request.
    Arguments:
    ---------
        positional:
        ----------
            url: 'str' -> URL whre from we want to get response
        optional:
        --------
            params: 'dict' -> params will be count of pages
    Returns:
    -------
        'response' -> Response from web-page in response to our request
        For example <response 200> It means request successed
    """
    response = requests.get(url, headers=HEADERS, params=params)
    return response


def getCountOfPages(url):
    """
    Function to getting a count of pages current web-page
    Returns:
    -------
        'int' -> Count of pages
    """
    # Making BeautifulSoup object
    htmlResponse = getHtml(url)
    soup = bs(htmlResponse.text, "html.parser")
    countOfCurrentPage = int(soup.select("div.pages ul li")[-1].text)
    linkToCurrentPage = URL + soup.select("div.pages ul li")[-1].find("a")["href"]
    i = 5

    while True:
        htmlResponse = getHtml(linkToCurrentPage)
        soup = bs(htmlResponse.text, "html.parser")
        countOfCurrentPage = int(soup.select("div.pages ul li")[-1].text)
        i += 2
        if i > countOfCurrentPage:
            break
        linkToCurrentPage = URL + soup.select("div.pages ul li")[-1].find("a")["href"]

    return countOfCurrentPage


def getContent(html):
    """
    Getting content of html in the format we need
    Returns:
    -------
        'list[dict]' -> The data of all the cars on the page
    """
    soup = bs(html, "html.parser")
    allObjects = soup.select("div.main-r div.list")
    dogs = []
    for obj in allObjects:
        dogs.append(
            {
                "name": obj.select_one("div.list-1 div.right div.right-t p a").text,
                "lifespan": obj.select_one("div.list-1 div.right div.right-t span").text.split(':')[-1].strip(),
                "price": obj.select_one("div.list-1 div.right div.right-b p").text.split(':')[-1].strip(),
                "popularity": obj.select_one("div.list-2 p").text + "\nrank",
                "temperament": '\n'.join([p.text for p in obj.find("div", class_="list-3")][:-1]) + "\n...",
                "hypoallergenic": obj.select_one("div.list-4 p").text.upper(),
                "intelligence": obj.select_one("div.list-5 p").text + "\nrank"
            }
        )
    return dogs


def dataToCSV(data, path):
    """
    Function to save our data in a csv file
    """
    with open(path, 'w', newline='') as csvFile:
        csvWriter = csv.writer(csvFile, delimiter=';')
        csvWriter.writerow(["Name", "Lifespan", "Price", "Popularity",
                            "Temperament", "Hypoallergenic", "Intelligence"])

        for item in data:
            csvWriter.writerow([item["name"], item["lifespan"], item["price"],
                                item["popularity"], item["temperament"],
                                item["hypoallergenic"], item["intelligence"]])


def parse(url):
    """
    The function takes count of pages in current web-page
    and parding data from its
    Returns:
        'None'
    """
    # Getting html in a current page
    htmlResponse = getHtml(url)
    if htmlResponse.status_code == 200:
        dogs = []
        pagesCount = getCountOfPages(url)

        for page in range(1, pagesCount + 1):
            print(f"Parsing page {page} from {pagesCount}...")
            htmlResponse = getHtml(url, params={"page-": page})
            dogs.extend(getContent(htmlResponse.text))
        return dogs
    else:
        print("Error!")


dogsData = parse(URL)
dataToCSV(dogsData, "dogs/dogsdata.csv")
