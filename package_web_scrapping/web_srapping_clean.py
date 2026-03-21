from bs4 import BeautifulSoup
import requests


class BsScraper:
    def __init__(self):
        self.target_url = "https://www.sidhakura.com/policy?page="
        self.news_list = []

    def scrap_page(self, page=1):
        response = requests.get(f"{self.target_url}{page}")
        html_text = response.text
        soup = BeautifulSoup(html_text, "html.parser")

        full_news_div = soup.find("div", {"class": "full-samachar-list"})

        if full_news_div:
            for i in full_news_div.find_all("div"):
                title_tag = i.find("h2")
                image_tag = i.find("img")
                date_tag = i.find("span")

                if title_tag and image_tag and date_tag:
                    title = title_tag.find("a").text.strip()
                    image = image_tag.get("data-src")
                    publish_date = date_tag.text.strip()

                    self.news_list.append({
                        "title": title,
                        "image": image,
                        "publish_date": publish_date,
                    })

                    print(f"""
TITLE :: {title}
IMAGE :: {image}
PUBLISHED :: {publish_date}
""")

    def scrap_all(self):
        for i in range(1, 5):
            self.scrap_page(i)


# Create instance
instance = BsScraper()
instance.scrap_all()

print(f"TOTAL NEWS SCRAPED: {len(instance.news_list)}")


#code for scrapped new data  store in database using sqlalchemy and psycopg2 library.

# # pip install pandas sqlalchemy
import pandas as pd
from sqlalchemy import create_engine,text
from sqlalchemy.orm import sessionmaker

# Extract data → Process it →  Store it in a database

class SQLUtils:
    DB_NAME = "ok_test3"
    DB_USER = "postgres"
    DB_PASS = "easy"
    DB_HOST = "localhost"
    DB_PORT = "5432"

    def __init__(self):
        self.url = f"postgresql://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    
    def get_seed_data(self):
        data = [
            {
                "title": f"Title #{i}", 
                "description" : f"Description for #{i}"
            } for i in range(5000)]
        return pd.DataFrame(data)

    def insert(self):
        try:
            table_name="dummy_table_1"
            engine = create_engine(url=self.url) 
            # Creates a connection to the database
            Session = sessionmaker(bind=engine)
            session = Session()
            self.get_seed_data().to_sql(
                name=table_name, con=engine, 
                if_exists='append',index=False
            ) # if table exists, overwrite the table.
            print('Dummy Data Inserted Successfully!')
            session.commit()
        except Exception as e:
            session.rollback()
            print(f'Error occurred during loading to database: {str(e)}')
        finally:
            session.close()


    def read_data(self):
        engine = create_engine(self.url)

        query = """
                SELECT * from dummy_table_1;
            """

        with engine.connect() as connection:
            result = connection.execute(text(query))
            return result

instance = SQLUtils()

# instance.insert()



data = instance.read_data()

for i in data:
    title, description = i
    print(f"Title :: >> {title}, Description :: >> {description}\n", "-"*50)