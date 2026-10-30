# Automated Data Pipeline & Web Scraper (Python)

## 📌 Overview
A Python-based ETL (Extract, Transform, Load) pipeline designed to automate the collection, processing, and storage of web data. The script extracts data from a public web source, cleans and transforms it using Pandas, and persists it into a local SQLite database for querying and analysis.

## 🚀 Features
- **Extract:** Utilizes `requests` and `BeautifulSoup` to navigate through paginated web pages and extract raw text data.
- **Transform:** Structures raw HTML data into a clean Pandas DataFrame and performs data manipulation (e.g., calculating data metrics).
- **Load:** Initializes an SQLite database and inserts the processed data, ensuring persistent storage for future analysis.
- **Analyze:** Executes SQL queries to generate summary statistics (e.g., top authors by quote count) directly in the terminal.

## 🛠️ Technologies Used
- **Python 3**
- **Requests** (HTTP library for fetching web pages)
- **BeautifulSoup4** (HTML parsing and extraction)
- **Pandas** (Data cleaning and manipulation)
- **SQLite3** (Relational database for persistent storage)

## ⚙️ How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/python-data-pipeline.git

## 📸 Screenshots
<img width="933" height="486" alt="7" src="https://github.com/user-attachments/assets/1e3c0b11-5d61-4a1a-a5f2-6b0a23c37dfc" />

