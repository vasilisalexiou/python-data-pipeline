import requests
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3
import time

def scrape_quotes(pages_to_scrape=3):
    """
    Scrapes quotes, authors, and tags from a public sandbox website.
    """
    base_url = "http://quotes.toscrape.com/page/{}/"
    all_quotes = []

    print("Starting web scraping...")
    
    for page_num in range(1, pages_to_scrape + 1):
        url = base_url.format(page_num)
        response = requests.get(url)
        
        if response.status_code != 200:
            print(f"Failed to retrieve page {page_num}. Status code: {response.status_code}")
            break
            
        soup = BeautifulSoup(response.text, 'html.parser')
        quotes = soup.find_all('div', class_='quote')
        
        for quote in quotes:
            text = quote.find('span', class_='text').get_text(strip=True)
            author = quote.find('small', class_='author').get_text(strip=True)
            tags = [tag.get_text(strip=True) for tag in quote.find_all('a', class_='tag')]
            
            all_quotes.append({
                'quote': text,
                'author': author,
                'tags': ", ".join(tags) # Join list of tags into a single string
            })
            
        print(f"Scraped page {page_num}")
        time.sleep(1) # Be polite to the server

    return all_quotes

def process_and_store_data(quotes_data):
    """
    Processes the raw scraped data using Pandas and stores it in an SQLite database.
    """
    if not quotes_data:
        print("No data to process.")
        return

    # 1. Convert to Pandas DataFrame
    df = pd.DataFrame(quotes_data)
    
    # 2. Data Cleaning/Transformation
    # Let's add a column that counts how many tags each quote has
    df['tag_count'] = df['tags'].apply(lambda x: len(x.split(',')) if x else 0)
    
    print(f"Successfully processed {len(df)} quotes.")

    # 3. Store in SQLite Database
    db_name = 'quotes_data.db'
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Create table (drops it if it already exists so we can re-run the script)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS scraped_quotes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            quote TEXT,
            author TEXT,
            tags TEXT,
            tag_count INTEGER
        )
    ''')
    cursor.execute('DELETE FROM scraped_quotes') # Clear old data for a fresh run

    # Insert data using Pandas
    df.to_sql('scraped_quotes', conn, if_exists='append', index=False)
    
    conn.commit()
    conn.close()
    print(f"Data successfully saved to {db_name}")

    # 4. Print a quick summary (Data Analysis)
    print("\n--- Top 3 Authors by Quote Count ---")
    print(df['author'].value_counts().head(3))

if __name__ == "__main__":
    # Run the pipeline
    scraped_data = scrape_quotes(pages_to_scrape=3)
    process_and_store_data(scraped_data)