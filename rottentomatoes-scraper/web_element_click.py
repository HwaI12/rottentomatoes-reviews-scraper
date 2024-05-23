from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class UrlMaker:
    """
    取得したタイトルURLからレビューURLを作成するクラス
    """

    def make_url(self, url):
        """
        タイトルURLからレビューURLを作成するメソッド
        """
        audience_url = url + "/reviews?type=user"
        return audience_url

    def make_audience_url(self, titles_df):
        """
        タイトル情報を含むDataFrameからレビューURLのリストを作成するメソッド
        """
        audience_url = []
        for i in range(len(titles_df)):
            url = titles_df["title_url"][i]
            audience_url.append(self.make_url(url))
        return audience_url

def make_title_name(titles_df):
    """
    DataFrameからタイトル名のリストを作成する関数
    """
    title_names = []
    for i in range(len(titles_df)):
        title = titles_df["title"][i]
        title_names.append(title)
    return title_names

class ButtonClicker:
    """
    ウェブページのボタンをクリックするクラス
    """

    def __init__(self, driver):
        self.driver = driver

    def click_button(self, class_name):
        """
        指定されたクラス名のボタンをクリックするメソッド
        """
        try:
            btn = self.driver.find_element(By.CLASS_NAME, class_name)
            btn.click()
        except NoSuchElementException:
            print("クリック失敗")
            pass

    def click_title_actions(self):
        """タイトルアクションボタンをクリックするメソッド"""
        self.click_button("discovery__actions")

    def click_review_actions(self):
        """レビューアクションボタンをクリックするメソッド"""
        self.click_button("load-more-container")
