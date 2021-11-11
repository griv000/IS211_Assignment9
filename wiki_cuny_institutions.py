import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/City_University_of_New_York"


def run_parse():
    response = requests.get(url).text
    soup = BeautifulSoup(response, features = "html.parser")

    for caption in soup.find_all('caption'):
        if caption.get_text() == "CUNY Component Institutions\n":
            tables = caption.find_parent('table')
            rows = tables.find_all('tr')

            for row in rows:

                header_row = row.find_all('th')
                if header_row:
                    print(f'{header_row[0].text.strip():<5} | {header_row[1].text.strip():<25} | {header_row[2].text.strip()}')
                    print("-----------------------------------------------------")

                cells = row.find_all("td")
                if cells:
                    print(f"{int(cells[0].text):<5} | {cells[1].text:<25} | {cells[2].text.strip()}")


if __name__ == "__main__":
    run_parse()