import pandas as pd

def data_agent(file_path:str="data/sales_data.csv")->pd.DataFrame:
    df=pd.read_csv(file_path)
    return df