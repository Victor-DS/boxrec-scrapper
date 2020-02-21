import requests
from bs4 import BeautifulSoup
import json


def get_data(boxer_id):
    boxrec_url = build_url(boxer_id)
    content = get_url_content(boxrec_url)
    data = get_boxer_data(content)
    boxer = {boxer_id: data}
    return json.dumps(boxer)


def get_boxer_data(content):
    soup = BeautifulSoup(content, 'html.parser')
    return {
        "name": pretty_string(soup.findAll('h1')[1]),
        "fights": get_fights(soup)
    }


def build_url(boxer_id):
    return 'https://boxrec.com/en/proboxer/' + str(boxer_id)


def get_url_content(url):
    page = requests.get(url)
    return page.content


def get_fights(soup):
    fight_table = soup.find(class_='dataTable')
    fight_lines = fight_table.findAll('tbody')
    fights = []
    for line in fight_lines:
        fight = get_fight(line)
        fights.append(fight)
    return fights


def get_fight(line):
    line = line.find('tr')
    if len(line) <= 0:
        return None
    return {
        "opponent": get_fight_opponent(line),
        "fight_date": get_fight_date(line),
        "fight_result": get_fight_result(line),
        "fight_result_type": get_fight_result_type(line)
    }


def get_fight_opponent(line):
    if len(line) <= 0:
        return None
    column = line.findAll('td')[3]
    link = column.find('a')
    return pretty_string(link)


def get_fight_date(line):
    column = line.findAll('td')[1]
    link = column.find('a')
    return pretty_string(link)


def get_fight_result(line):
    column = line.findAll('td')[7]
    div = column.find('div')
    return pretty_string(div)


def get_fight_result_type(line):
    column = line.findAll('td')[8]
    return pretty_string(column)


def pretty_string(soup_value):
    return soup_value.string.encode("utf-8").strip()
