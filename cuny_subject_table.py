import requests
from bs4 import BeautifulSoup

url = "https://www.cuny.edu/about/administration/offices/registrar/resources/cuny-subject-table/"


def run_parse():
    response = requests.get(url).text
    soup = BeautifulSoup(response, features = "html.parser")

    tables = soup.find('table')
    rows = tables.find_all('tr')
    header = True
    for row in rows:
        cells = row.find_all("td")
        if header == True:
            print(f"{cells[0].text:<13} | {cells[1].text}")
            print("------------------------------------")
            header = False
        else:
            print(f"{cells[0].text:<13} | {cells[1].text}")


if __name__ == "__main__":
    run_parse()