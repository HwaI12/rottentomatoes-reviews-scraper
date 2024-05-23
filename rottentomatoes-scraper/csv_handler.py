import pandas as pd
import os

class CSVHandler:
    def __init__(self, columns):
        """
        CSVHandlerクラスのコンストラクタ
        """
        self.df = pd.DataFrame(columns=columns)

    def add_info(self, add_dict):
        """
        辞書形式のデータをDataFrameに追加するメソッド
        """
        self.df = pd.concat([self.df, pd.DataFrame([add_dict])], ignore_index=True)

    def save_file(self, file_name):
        """
        DataFrameをCSVファイルに保存するメソッド
        """
        directory = os.path.dirname(file_name)
        if not os.path.exists(directory):
            os.makedirs(directory)
        if not os.path.exists(file_name):
            self.df.to_csv(file_name, index=False)
        else:
            self.df.to_csv(file_name, mode="a", header=False, index=False)

    @staticmethod
    def read_csv(file_name):
        """
        CSVファイルを読み込んでDataFrameを返す静的メソッド
        """
        return pd.read_csv(file_name)
