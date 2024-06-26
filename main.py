import webbrowser
import schedule
import time

def get_urls_from_user():
    """
    This function prompts the user to input URLs until the user enters '0'.
    It returns a list of entered URLs.
    """
    urls = []
    while True:
        url = input("Enter a URL (enter 0 to stop): ")
        if url == '0':
            break
        urls.append(url)
    return urls

def open_url_in_browser(url):
    """
    This function opens a single URL in the default web browser.
    """
    webbrowser.open(url)

def open_all_urls_with_interval(urls, interval):
    """
    This function opens all URLs in the provided list with a specified interval between each.
    """
    for url in urls:
        open_url_in_browser(url)
        print(f"Opened URL: {url}")
        time.sleep(interval)

def schedule_opening_urls(interval_hours, open_function, urls, interval_between_urls):
    """
    This function schedules the opening of URLs at a specified hourly interval.
    """
    def job():
        open_function(urls, interval_between_urls)
    
    schedule.every(interval_hours).hours.do(job)

def main():
    """
    The main function that runs the program.
    """
    # Get URLs from the user
    urls = get_urls_from_user()
    # Define the interval between opening each URL (in seconds)
    interval_between_urls = 20
    # Define the interval for scheduling the job (in hours)
    interval_hours = 3
    # Schedule the job
    schedule_opening_urls(interval_hours, open_all_urls_with_interval, urls, interval_between_urls)
    
    while True:
        # Run scheduled tasks
        schedule.run_pending()
        time.sleep(1)

# Check if this script is being run as the main program
if __name__ == "__main__":
    main()
