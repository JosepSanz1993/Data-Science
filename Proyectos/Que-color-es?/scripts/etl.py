import polars as pl
import json
class ETL:
    def __init__(self,path):
        self.df = pl.read_csv(path)

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

    def save_json(self,path):
        df = self.__normalitzated_data()
        with open(path, "w") as f:
            json.dump(df.to_dicts(), f, indent=4)
        print("Data saved in JSON format")

