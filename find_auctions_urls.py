from bs4 import BeautifulSoup
import requests
import time

def read_opened_links():
    FILENAME = "opened_urls.txt"
    with open(FILENAME, "r") as f:
        return f.read()


def read_saved_links():
    with open("url_to_open.txt", "r") as f:
        return f.read()


def save_found_links(found_links_set):
    with open("url_to_open.txt", "a") as f:
        # In append mode .write() doesn't add \n
        for link in found_links_set:
            f.write(link + "\n")


def find_new_links(search_link):
    html = ""
    try:
        html = requests.get(search_link).text
    except:
        print(f"Invalid search_link: {search_link}")
        return
    soup = BeautifulSoup(html, features="html.parser")
    links = soup.find_all("a")

    already_saved_links = set(read_saved_links().split())
    already_opened_links = set(read_opened_links().split())
    found_links = set()
    for tag in links:
        link = tag.get("href", None)
        class_ = tag.get("class", None)
        KEYWORD = "/oferta/"
        if (
                link is None
                or link in already_saved_links
                or link in already_opened_links
                or link in found_links
                or KEYWORD not in link
                or class_ is not None
        ):
            continue
        print("Auction found!")
        print(time.localtime(time.time))
        found_links.add(link)
    save_found_links(found_links)


def perform_search():
    with open("search_links.txt", "r") as f:
        search_links_list = f.read().split()
    for link in search_links_list:
        find_new_links(link)


if __name__ == '__main__':
    perform_search()
