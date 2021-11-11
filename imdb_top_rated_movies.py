import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/"


def remove_nl(content):
    return content.replace('\n', "").replace("     ","").strip()

def run_parse():
    response = requests.get(url).text
    soup = BeautifulSoup(response, features = "html.parser")

    tables = soup.find('table')
    rows = tables.find_all('tr')

    for row in rows:

        header_row = row.find_all('th')
        if header_row:
            print(f"{header_row[1].text:<80} | {header_row[2].text}")
            print("-----------------------------------" * 3)

        cells = row.find_all('td')
        if cells:
            mytitle = remove_nl(cells[1].text)
            print(f"{mytitle:<80} | {float(cells[2].text)}")


if __name__ == "__main__":
    run_parse()