import webbrowser
import pyinputplus


def delete_lines(n):
    FILENAME = "url_to_open.txt"
    with open(FILENAME, "r") as f:
        url_list = f.read().split()
    url_list = url_list[n:]
    with open(FILENAME, "w") as f:
        f.write("\n".join(url_list) + "\n")
    print(f"Deleted {n} lines")


def save_opened_url(url):
    FILENAME = "opened_urls.txt"
    with open(FILENAME, "a") as f:
        f.write(url)
    print(f"Link saved in {FILENAME}")


def open_in_browser(n):
    with open("url_to_open.txt", "r") as f:
        url_list = f.readlines()
        lines_to_read = n if n < len(url_list) else len(url_list)
        for i in range(lines_to_read):
            webbrowser.open(url_list[i], 3)
            save_opened_url(url_list[i])
        delete_lines(lines_to_read)


if __name__ == '__main__':
    n = pyinputplus.inputNum(prompt="Input number of urls to open: ", min=1, max=20)
    open_in_browser(n)