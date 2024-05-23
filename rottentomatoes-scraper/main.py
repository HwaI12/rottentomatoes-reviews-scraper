from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from reviews_scraper import ReviewsScraper
from csv_handler import CSVHandler
from web_element_click import UrlMaker, make_title_name

def main():
    """
    メイン関数

    CSVからタイトル情報を読み込み、URLを生成してレビューをスクレイプする。
    """
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

    csv_filename = "csv_data/eiga_titles.csv"
    titles_df = CSVHandler.read_csv(csv_filename)
    url_maker = UrlMaker()
    for i, row in titles_df.iterrows():
        title_url = row["title_url"]
        title_name = row["title"]
        open_date = row["open_date"]
        audience_url = url_maker.make_url(title_url)
        scraper = ReviewsScraper(driver, audience_url, title_name, open_date)
        scraper.scrape_reviews()

    # WebDriverを終了
    driver.quit()

if __name__ == "__main__":
    main()
