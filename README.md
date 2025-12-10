# space-people-tracker

This project demonstrates API integration fundamentals using Python. It connects to a public API, processes JSON responses, and stores the data locally in CSV format.

## Project Overview

This script tracks astronauts currently in space by querying the Open Notify API. Each execution captures a timestamped snapshot of who is in space and which spacecraft they're aboard, building a historical record over time.

### Tools Used

**Python & requests**: For making HTTP requests to external APIs and handling responses.

## Data Pipeline

### Data Extraction

Raw astronaut data is fetched from the Open Notify API endpoint (`http://api.open-notify.org/astros.json`) using the `requests` library.

The API returns JSON containing the number of people in space and details about each person (name and craft).

### Data Transformation

The `process_data()` function transforms the nested JSON structure into a flat tabular format suitable for CSV storage.

Each astronaut record is enriched with an ISO-formatted timestamp indicating when the data was collected.

The transformation flattens the JSON array into individual rows, each containing: timestamp, astronaut name, and spacecraft name.

### Data Storage

Processed data is appended to `space_people_history.csv` using Python's CSV writer.

The script intelligently handles file creation on first run and appends to existing files on subsequent runs, preserving historical data.

CSV format ensures the data is portable, easily queryable, and compatible with analysis tools like Excel, Pandas, or SQL databases.

## Code Structure

```
fetch_data()
    ├── Makes GET request to API endpoint
    ├── Validates response status
    └── Returns parsed JSON data

process_data()
    ├── Extracts 'people' array from JSON
    ├── Generates current timestamp
    └── Transforms each person into a dictionary row

store_data()
    ├── Checks if CSV file exists
    ├── Writes header row if creating new file
    └── Appends all processed rows to CSV

main()
    └── Orchestrates the ETL pipeline
```

## Key Learning Outcomes

**API Integration**: Understanding how to authenticate, request, and handle responses from REST APIs.

**Error Handling**: Using `raise_for_status()` to catch and handle HTTP errors gracefully.

**Data Serialization**: Converting between JSON (API format) and CSV (storage format).

**Incremental Data Collection**: Building append-only datasets that grow with each script execution.

## Business Value and Use Cases

While this is a learning project, the pattern demonstrated has real-world applications:

**API Monitoring**: Track changes in API responses over time to detect service issues or data drift.

**Historical Analysis**: Build datasets from APIs that only provide current state.
