
# # .............This is complete code of scrapping and also store these news in database............#

# import requests

# import subprocess
# import sys

# def install_package(package):
#     try:
#         subprocess.check_call([sys.executable, "-m", "pip", "install", package])
#     except subprocess.CalledProcessError as e:
#         print(f"Failed to install {package}: {e}")
#         sys.exit(1)

# # Check if pip is available
# try:
#     import pip
# except ImportError:
#     print("Pip not found. Installing pip...")
#     try:
#         subprocess.check_call([sys.executable, "-m", "ensurepip", "--upgrade"])
#     except:
#         print("Failed to install pip. Please install pip manually.")
#         sys.exit(1)

# # List of required packages
# required_packages = [
#     "requests",
#     "pandas",
#     "beautifulsoup4",
#     "psycopg2-binary",
#     "sqlalchemy"
# ]

# # Check and install missing packages
# for package in required_packages:
#     try:
#         __import__(package.replace("-", "_"))  # For packages like psycopg2-binary, import as psycopg2
#     except ImportError:
#         print(f"Installing {package}...")
#         install_package(package)




# Function to fetch news articles from the website


import re
import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from urllib.parse import urljoin

from sqlalchemy import create_engine, text


# -----------------------------
# SCRAPER CLASS (EKANTIPUR)
# -----------------------------
class EkantipurScraper:
    def __init__(self, category="news"):
        # category examples: news, politics, business, sports, entertainment, world, technology, etc.
        self.base_url = "https://ekantipur.com/"
        self.category = category.strip("/")

        self.listing_url = urljoin(self.base_url, f"{self.category}")
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        })

        self.news_list = []
        self.seen_urls = set()

    def _get_soup(self, url: str) -> BeautifulSoup | None:
        try:
            r = self.session.get(url, timeout=20)
            if r.status_code != 200:
                print(f"Failed to fetch: {url} | status={r.status_code}")
                return None
            return BeautifulSoup(r.text, "html.parser")
        except Exception as e:
            print(f"Error fetching {url}: {e}")
            return None

    def _extract_article_links_from_listing(self, soup: BeautifulSoup) -> list[dict]:
        """
        Ekantipur category pages contain many <h2><a href="...">Title</a></h2>.
        We'll capture links that look like real article URLs:
          /<category>/<yyyy>/<mm>/<dd>/<something>.html
        """
        results = []
        pattern = re.compile(rf"^/{re.escape(self.category)}/\d{{4}}/\d{{2}}/\d{{2}}/.+\.html$")

        for a in soup.select("h2 a[href]"):
            href = a.get("href", "").strip()
            title = a.get_text(" ", strip=True)

            if not href or not title:
                continue

            # Only keep links that match article format for that category
            if not pattern.match(href):
                continue

            full_url = urljoin(self.base_url, href.lstrip("/"))
            if full_url in self.seen_urls:
                continue

            results.append({"title": title, "url": full_url})
            self.seen_urls.add(full_url)

        return results

    def _extract_details_from_article(self, article_url: str) -> dict:
        """
        Extract publish date + image using robust meta tags.
        """
        soup = self._get_soup(article_url)
        if not soup:
            return {"publish_date": None, "image": None}

        # Publish date (try common meta patterns)
        publish_date = None
        for key in [
            ("meta", {"property": "article:published_time"}),
            ("meta", {"name": "article:published_time"}),
            ("meta", {"name": "publish-date"}),
            ("meta", {"property": "og:updated_time"}),
        ]:
            tag = soup.find(*key)
            if tag and tag.get("content"):
                publish_date = tag["content"].strip()
                break

        # Main image (og:image is usually best)
        image = None
        og_img = soup.find("meta", {"property": "og:image"})
        if og_img and og_img.get("content"):
            image = og_img["content"].strip()

        return {"publish_date": publish_date, "image": image}

    def scrape_latest(self, max_articles=30, polite_delay=0.6):
        # 1) listing
        listing_soup = self._get_soup(self.listing_url)
        if not listing_soup:
            return

        items = self._extract_article_links_from_listing(listing_soup)
        if not items:
            print("No article links found. The site layout may have changed.")
            return

        # 2) visit article pages for details
        for item in items[:max_articles]:
            details = self._extract_details_from_article(item["url"])
            self.news_list.append({
                "title": item["title"],
                "url": item["url"],
                "image": details["image"],
                "publish_date": details["publish_date"],
                "category": self.category,
            })
            time.sleep(polite_delay)

        print(f"Total Ekantipur articles scraped: {len(self.news_list)}")


# -----------------------------
# DATABASE CLASS
# -----------------------------
class SQLUtils:
    DB_NAME = "ok_test3"
    DB_USER = "postgres"
    DB_PASS = "easy"
    DB_HOST = "localhost"
    DB_PORT = "5432"

    def __init__(self):
        self.url = (
            f"postgresql://{self.DB_USER}:{self.DB_PASS}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )
        self.engine = create_engine(self.url)

    def insert_dataframe(self, df, table_name="news_table"):
        try:
            df.to_sql(
                name=table_name,
                con=self.engine,
                if_exists="append",
                index=False
            )
            print("Data Inserted Successfully!")
        except Exception as e:
            print(f"Error inserting data: {e}")

    def read_data(self, table_name="news_table"):
        query = f"SELECT * FROM {table_name};"
        with self.engine.connect() as connection:
            result = connection.execute(text(query))
            return result.fetchall()


# -----------------------------
# MAIN EXECUTION
# -----------------------------
if __name__ == "__main__":
    scraper = EkantipurScraper(category="news")   # try: politics, business, sports, world...
    scraper.scrape_latest(max_articles=30)

    if scraper.news_list:
        df = pd.DataFrame(scraper.news_list)

        db = SQLUtils()
        db.insert_dataframe(df, table_name="news_table")

        data = db.read_data("news_table")
        for row in data:
            print(row)
    else:
        print("No data scraped.")