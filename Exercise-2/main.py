import requests
import pandas
from bs4 import BeautifulSoup

def find_name():
    return 

def main():
    url = "https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/"
    timestamp = "2024-01-19 15:35" # Chose a different timestamp, since the one provided doesn't exist any more.
    req = requests.get(url)
    # Not using lxml to minimize the amount of things to install
    soup = BeautifulSoup(req.content, 'html.parser')
    td = soup.find("td", string=timestamp)
    if td:
        # Find the parent "tr" block of the "td" block containing the given timestamp, then get the text within "a"
        csv_name = td.find_parent("tr").a.get_text() # Since we want a hyperlink name, we just need the "a" attribute
        download_url = url + csv_name
    csv = requests.get(download_url).content
    # Save the csv locally, then open it for reading via pandas
    with open(csv_name, 'wb') as f:
        f.write(csv)
    with open(csv_name, 'rb') as f:
        df = pandas.read_csv(f, low_memory=False)
    max_row = df.iloc[df['HourlyDryBulbTemperature'].idxmax()]
    print(max_row)
    

if __name__ == "__main__":
    main()
