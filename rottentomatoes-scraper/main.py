from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manger import webdriver_manager

from titles_scraper import TitlesScraper
from reviews_scraper import ReviewsScraper
from csv_handler import CSVHandler
from maker import UrlMaker

def eiga_name(csv_title_filename, click_button_count_title, fail_counter):
    driver = webdriver_manager()
    URL = "https://www.rottentomatoes.com/browse/movies_at_home/sort:popular"
    scraper = TitlesScraper(driver, URL, fail_counter, csv_title_filename, click_button_count_title)
    scraper.scrape_titles()
    driver.quit()

def eiga_review(csv_title_filename, click_button_count_review, csv_review_filename, fail_counter):
    # レビュアー・レビュー日・レビューを取得
    driver = webdriver_manager()
    titles_df = CSVHandler.read_csv(csv_title_filename)
    url_maker = UrlMaker()
    for i, row in titles_df.iterrows():
        title_url = row["title_url"]
        title_name = row["title"]
        open_date = row["open_date"]
        audience_url = url_maker.make_url(title_url)
        scraper = ReviewsScraper(driver, audience_url, title_name, open_date, fail_counter, click_button_count_review, csv_review_filename)
        scraper.scrape_reviews()
    driver.quit()

def main():
    fail_counter = {"main": 0, "get_inf": 0, "get_inf_for": 0}
    
    csv_title_filename = "./titles.csv"
    click_button_count_title = 0
    eiga_name(csv_title_filename, click_button_count_title, fail_counter)

    csv_review_filename = "./reviews.csv"
    click_button_count_review = 1
    eiga_review(csv_title_filename, click_button_count_review, csv_review_filename, fail_counter)

if __name__ == "__main__":
    main()