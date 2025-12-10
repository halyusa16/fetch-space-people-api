import requests
import csv
import datetime

API_URL = "http://api.open-notify.org/astros.json"
CSV_FILE = "space_people_history.csv"


def fetch_data():
    """
    Fetch data from API endpoint
    """
    print("Fetching data from API...")
    response = requests.get(API_URL)
    response.raise_for_status()
    return response.json()


def process_data(data):
    """
    Transform raw JSON into tabular format
    """
    people = data.get("people", [])
    timestamp = datetime.datetime.now().isoformat()

    rows = []
    for person in people:
        rows.append({
            "timestamp": timestamp,
            "name": person.get("name"),
            "craft": person.get("craft")
        })

    print(f"Processed {len(rows)} records.")
    return rows


def store_data(rows):
    """
    Store results into CSV file,
    append if exists, create if not.
    """
    file_exists = False

    try:
        with open(CSV_FILE, 'r'):
            file_exists = True
    except FileNotFoundError:
        pass

    with open(CSV_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=['timestamp', 'name', 'craft'])

        if not file_exists:
            writer.writeheader()

        for row in rows:
            writer.writerow(row)

    print(f"Saved {len(rows)} rows into {CSV_FILE}")


def main():
    data = fetch_data()
    rows = process_data(data)
    store_data(rows)


if __name__ == "__main__":
    main()