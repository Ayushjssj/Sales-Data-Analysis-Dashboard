import pandas as pd
from sqlalchemy import create_engine

# Load original dataset
df = pd.read_csv("../data/superstore.csv", encoding='latin1')

# MySQL credentials
username = "root"
password = "Ayush%402003"
host = "localhost"
database = "sales_project"

# Create connection engine
engine = create_engine(
    f"mysql+pymysql://{username}:{password}@{host}/{database}"
)

# Upload dataframe into MySQL
df.to_sql(
    name="sales_data",
    con=engine,
    if_exists="replace",
    index=False
)

print("Data uploaded successfully!")