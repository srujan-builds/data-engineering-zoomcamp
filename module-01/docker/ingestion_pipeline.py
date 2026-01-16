import pandas as pd
from sqlalchemy import create_engine, text


def read_data():

    # Green taxi trip data
    green_trip_df = pd.read_parquet("/app/data/green_tripdata_2025-11.parquet")
    green_trip_df.columns = [c.lower() for c in green_trip_df.columns]

    # taxi zone lookup data
    taxi_zone_df = pd.read_csv("/app/data/taxi_zone_lookup.csv")
    taxi_zone_df.columns = [c.lower() for c in taxi_zone_df.columns]

    return {"green_trip_data":green_trip_df, "taxi_zone_lookup_data": taxi_zone_df}



def conn_to_db():
    user = "postgres"
    password = "postgres"
    db_name = "ny_taxi"
    host = "postgres"
    port = 5432
  

    url = f"postgresql://{user}:{password}@{host}:{port}/{db_name}" 

    try:
        engine = create_engine(url=url)
        with engine.connect() as conn:
            conn.execute(text("Select 1"))
        print("Connected to db")
        return engine
    except Exception as e:
        print(f"Error while connecting to db: {e}")
        return None


def load_data(df, table_name, engine):
    if engine is not None:
        try:
            df.to_sql(name=table_name, con=engine, index=False, if_exists="replace")
            print(f"Rows {len(df)} loaded to table: {table_name}")
        except Exception as e:
            print(f"Error while loading data to table: {table_name}")
    
if __name__ == "__main__":

    data = read_data()
    green_trip_data = data["green_trip_data"]
    taxi_zone_lookup_data = data["taxi_zone_lookup_data"]

    engine = conn_to_db()

    load_data(df=green_trip_data, table_name="green_trip", engine=engine)
    load_data(df=taxi_zone_lookup_data, table_name="taxi_zone_lookup", engine=engine)