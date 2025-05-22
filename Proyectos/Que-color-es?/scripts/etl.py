import polars as pl
import json
from global_var import *

class ETL:
    def __init__(self):
        self.df = pl.read_csv(DATA_NOT_PROCESSED)

    def __normalitzated_data(self):
        df = self.df.with_columns(
            pl.col("Red").cast(pl.Int32),
            pl.col("Green").cast(pl.Int32),
            pl.col("Blue").cast(pl.Int32),
            pl.col("Clear").cast(pl.Int32),
            pl.col("Lux").cast(pl.Int32),
            pl.col("Color").cast(pl.String),
        )
        return df.drop(["Data", "Object"])

    def save_json(self):
        df = self.__normalitzated_data()
        with open(DATA_PROCESSED, "w") as f:
            json.dump(df.to_dicts(), f, indent=4)
        print("Data saved in JSON format")

etl = ETL()
etl.save_json()