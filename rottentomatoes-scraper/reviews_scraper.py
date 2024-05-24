# reviews_scraper.py

import os
import time
import pprint
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from click_button import ButtonClicker
from csv_handler import CSVHandler
from maker import convert_date

class ReviewsScraper:
    def __init__(self, driver, URL, title_name, open_date, fail_counter, click_button_count_review, csv_review_filename):
        self.driver = driver
        self.URL = URL
        self.title = title_name
        self.open_date = open_date
        self.fail_counter = fail_counter
        self.click_button_count_review = click_button_count_review
        self.csv_review_filename = csv_review_filename

    def scrape_reviews(self):
        review_columns = [
            "title", "open_date", "reviewer",
            "review_date", "evaluation", "review"
        ]
        csv_handler = CSVHandler(review_columns)
        self.driver.get(self.URL)
        time.sleep(1)
        button_clicker = ButtonClicker(self.driver)
        for _ in range(self.click_button_count_review):
            button_clicker.click_review_actions()
            time.sleep(2)
        self._get_inf(csv_handler)
        csv_handler.save_to_csv(self.csv_review_filename)
        print(self.fail_counter)

    def _get_inf(self, csv_handler):
        try:
            all_reviews = self.driver.find_elements(By.CSS_SELECTOR, ".audience-review-row")
            for review_element in all_reviews:
                review_dic = self._extract_review_info(review_element)
                csv_handler.add_info(review_dic)
                pprint.pprint(review_dic)
        except NoSuchElementException:
            self.fail_counter["get_inf"] += 1

    def _extract_review_info(self, review_element):
        review_dic = {
            "reviewer": self._get_reviewer(review_element),
            "review_date": None,
            "evaluation": None,
            "review": None,
            "title": self.title,
            "open_date": self.open_date
        }
        review_dic["review"], review_dic["review_date"], review_dic["evaluation"] = self._get_review_info(review_element)
        return review_dic

    def _get_reviewer(self, review_element):
        try:
            reviewer_element = review_element.find_element(By.CSS_SELECTOR, ".audience-reviews__name")
            return reviewer_element.text.strip()
        except NoSuchElementException:
            return "Anonymous"

    def _get_review_info(self, review_element):
        try:
            review_text_element = review_element.find_element(By.CSS_SELECTOR, ".audience-reviews__review.js-review-text")
            review_text = review_text_element.text.strip()

            date_element = review_element.find_element(By.CLASS_NAME, "audience-reviews__duration")
            date = convert_date(date_element.text.strip())

            score_elements = review_element.find_elements(By.CSS_SELECTOR, ".star-display__filled, .star-display__half")
            score = sum(1 if "star-display__filled" in e.get_attribute("class") else 0.5 for e in score_elements)

            return review_text, date, score
        except NoSuchElementException:
            return None, None, None
