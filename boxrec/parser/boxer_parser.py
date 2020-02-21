import requests
from bs4 import BeautifulSoup


def get_data(boxer_id):
    boxrec_url = build_url(boxer_id)
    content = get_url_content(boxrec_url)
    data = get_boxer_data(content)
    return {boxer_id: data}


def get_boxer_data(content):
    boxer = {"fights": get_fights(content)}
    return boxer


def build_url(boxer_id):
    return 'https://boxrec.com/en/proboxer/' + str(boxer_id)


def get_url_content(url):
    page = requests.get(url)
    return page.content


def get_fights(content):
    soup = BeautifulSoup(content, 'html.parser')
    fight_table = soup.find(class_='dataTable')
    fight_lines = fight_table.findAll('tbody')
    fights = []
    for line in fight_lines:
        fight = get_fight(line)
        fights.append(fight)
    return fights


def get_fight(line):
    line = line.find('tr')
    return {"opponent": get_fight_opponent(line)}


def get_fight_opponent(line):
    return get_text_for_column(line=line, column=3)


def get_text_for_column(line, column):
    return line.findAll('td')[column].find('a').string.encode("utf-8") \
        if len(line) > 0 else None
