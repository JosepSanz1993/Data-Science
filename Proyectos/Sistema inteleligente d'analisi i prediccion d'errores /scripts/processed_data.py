import polars as pl
import json
import os
from datetime import datetime

class processed:

    #Cargar datos del json
    def data_load(self,input):
        with open(input, "r") as f:
            data = [json.loads(line) for line in f.readlines()]
        return pl.DataFrame(data)
    
    # De timestamp a datatime, de string a numero y elimianr nulos
    def  preprocess_data(self,df):
        df = df.with_columns([pl.col("timestamp").
                              str.strptime(pl.Datetime, "%Y-%m-%dT%H:%M:%S%.f")
                              .alias("timestamp_parsed")])
        df = df.with_columns([
        pl.col("cpu_usage").cast(pl.Float64),
        pl.col("ram_usage").cast(pl.Float64),
        pl.col("disk_usage").cast(pl.Float64),
        pl.col("temperature").cast(pl.Float64),
        pl.col("network_latency").cast(pl.Float64)])
        df = df.drop()
        return df 
    
    def save_processed_data(self,df, output_path):
        df.write_parquet(output_path)
        print(f"Datos procesados guardados a: {output_path}")

        