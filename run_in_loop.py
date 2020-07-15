import time
import find_auctions_urls


def every_n_seconds(n):
    while True:
        print("Searching for new links to auctions")
        start_time = time.time()
        find_auctions_urls.perform_search()
        end_time = time.time()
        search_time = int(end_time) - int(start_time)
        wait_time = n - search_time if n - search_time > 0 else 0
        print(f"Finished searching after {search_time} seconds. Waiting for {wait_time} seconds...")
        time.sleep(wait_time)


if __name__ == '__main__':
    every_n_seconds(5 * 60)