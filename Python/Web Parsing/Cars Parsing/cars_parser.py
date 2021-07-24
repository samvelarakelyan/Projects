"""
Program to parsing cars data from 'https://auto.ria.com/' '/newauto' section
*******************
WARNING!
--------
    This script may not work if you рун it.
    It's because this isn't a universal program and by and largemay work correctly
    only at the moment when it is written, depends on the operation of this
    website,the code it contains.
At the time of writing, the program was working correctly, as a result,
the existing files were presented in a tabular format,
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
           'accept': "*/*",
           }
HOST = "https://auto.ria.com"


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


def getMarksData():
    """
    Fuction to get data of all marks in '/newauto' section
    Returns:
    -------
        'list[str]' -> Links to all marks of cars
    """
    # URL to web-site '/newauto' section
    url = "https://auto.ria.com/newauto/"
    # Getting html from page
    html = getHtml(url).content
    # Making BeautifulSoup object from html
    marks = bs(html, 'html.parser')
    # Getting all references to cars marks
    marks = marks.select("section#catalogue div#marks-block a.item-brands")
    # Making list of strings, which contains full references to each mark
    marksHref = [url + a.get("href")[9:] for a in marks][:-1]

    return marksHref


def getCountOfPages(html):
    """
    Function to getting a count of pages current web-page
    Returns:
    -------
        'int' -> Count of pages
    """
    # Making BeautifulSoup object
    soup = bs(html, 'html.parser')
    # Trying to get a count of pages if it's greater than 1
    try:
        pagesCount = soup.select("nav.pager span")[-3]
        pagesCount = pagesCount.a.get_text()
        return int(pagesCount)
    # otherwise we will return 1
    except Exception:
        return 1


def getContent(html):
    """
    Getting content of html in the format we need
    Returns:
    -------
        'list[dict]' -> The data of all the cars on the page
    """
    soup = bs(html, "html.parser")
    items = soup.find_all('a', class_="proposition_link")

    cars = []
    for item in items:
        priceUAH = item.find("span", class_="size16")
        if priceUAH:
            priceUAH = priceUAH.get_text(strip=True)
        else:
            priceUAH = "price is missing"
        cars.append(
            {
                'title': item.select_one("div.proposition_title").get_text(strip=True),
                'link': HOST + item.get("href"),
                'priceUSD': item.find("div", class_="proposition_area").find(\
                                      "div", class_="proposition_price").find(\
                                      "span").get_text(strip=True),
                'priceUAH': priceUAH,
                'city': item.find("span", class_="item region").get_text(strip=True)
            }
        )

    return cars


def dataToCSV(items, path):
    """
    Function to save our data in a csv file
    """
    with open(path, 'w', newline='') as csvFile:
        csvWriter = csv.writer(csvFile, delimiter=';')
        csvWriter.writerow(["Model", "Link", "Price usd($)",
                            "Price UAH", "City"])
        for item in items:
            csvWriter.writerow([item["title"], item["link"], item["priceUSD"],
                                item["priceUAH"], item["city"]])


def parse(url):
    """
    The function takes count of pages in current web-page
    and parding data from its
    Returns:
        'None'
    """
    # Getting html in a current page
    html = getHtml(url)
    # If request succeeded
    if html.status_code == 200:
        cars = []
        # Getting pages count of current web-page
        pagesCount = getCountOfPages(html.text)
        for page in range(1, pagesCount + 1):
            print(f"Parsing page {page} from {pagesCount}...")
            # Getting response of our request to current web-page
            htmlResponse = getHtml(url, params={'page': page})
            # Putting data with content we needed in a cars list
            cars.extend(getContent(htmlResponse.text))
        return cars
    else:
        print("Error!")


allMarks = getMarksData()
for mark in allMarks:
    print(mark)
    cars = parse(mark)
    dataToCSV(cars, f"cars/{mark.split('-')[-1][:-1]}.csv")
