from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome()

# set up the driver and navigate to the page
url_template = 'https://understat.com/team/{}'
driver = webdriver.Chrome()

for league in ['EPL', 'La_liga', 'Bundesliga', 'Serie_A', 'Ligue_1']:
    for year in range(2018, 2019):
        url = url_template.format(f'{league}/{year}')
        driver.get(url)
        wait = WebDriverWait(driver, 30)
        wait.until(EC.presence_of_element_located((By.ID, 'team-data')))

        # parse the HTML content using BeautifulSoup
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        # find the table containing the player stats
        table = soup.find('table', {'id': 'team-data'})

        # loop through each row in the table and extract the relevant stats
        for row in table.tbody.find_all('tr'):
            player_name = row.find('a', {'class': 'player_name'}).text
            goals = row.find('td', {'data-stat': 'goals'}).text
            assists = row.find('td', {'data-stat': 'assists'}).text
            xG = row.find('td', {'data-stat': 'xG'}).text
            xA = row.find('td', {'data-stat': 'xA'}).text
            print(f"League: {league}, Year: {year}, Player: {player_name}, Goals: {goals}, Assists: {assists}, xG: {xG}, xA: {xA}")

# close the driver
driver.quit()