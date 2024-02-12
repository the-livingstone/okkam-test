from datetime import date

import pandas as pd

from app import config
from app.db import engine


def convert_date(d: str) -> date:
    return date(int(d[:4]), int(d[4:6]), int(d[6:]))


def load_data():
    df = pd.read_csv(
        "data.csv", converters={"Date": convert_date}, index_col=0, sep=";"
    )
    df.columns = map(lambda x: x.lower(), df.columns)
    try:
        df.to_sql(
            "some_research",
            engine,
            if_exists="replace" if config.REPLACE_IF_EXIST else "fail",
        )
    except ValueError:
        pass


if __name__ == "__main__":
    load_data()
