import pandas as pd
import sqlite3

class DatabaseLoader:
    def __init__(self, db: str = "myDB.db", csv_file: str = "ecommerce_dataset_updated.csv"):
        self.db = db
        self.csv_file = csv_file
        self.con = sqlite3.connect(db)
        self.cursor = self.con.cursor()
        
        df = pd.read_csv(csv_file)
        df.to_sql('myTable', self.con, if_exists='replace', index=False)
        self.con.commit()

    def watchRow(self) -> pd.DataFrame:
        df = pd.read_sql_query('SELECT * FROM myTable LIMIT 3', self.con)
        return df

    def close(self):
        self.con.close()

if __name__ == "__main__":
    db_loader = DatabaseLoader()
    
    # Get first three rows
    first_three_rows = db_loader.watchRow()
    print(first_three_rows)
    
    # Close the connection
    db_loader.close()