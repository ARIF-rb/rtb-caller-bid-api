# RTB Caller Bid API

A Flask web application that integrates with the **Retreaver RTB (Real-Time Bidding) API** to retrieve real-time bid information for incoming caller numbers. Users enter a caller number on the web UI and the app queries the Retreaver RTB endpoint, displaying the bid response.

## Use Case

Call-tracking and pay-per-call advertising platforms use RTB to determine how much a publisher earns per inbound call. This tool provides a lightweight web interface to query the Retreaver RTB endpoint for a given caller number — useful for testing RTB configurations, verifying bid responses, and debugging call routing logic.

## Features

- Simple web form to enter a caller number
- Queries the Retreaver RTB API in real time
- Displays raw bid response (amount, buyer info) in the browser
- Lightweight — no database, no authentication layer

## Tech Stack

| Layer | Tools |
|---|---|
| Language | Python 3.7+ |
| Backend | Flask |
| HTTP Client | requests |
| Frontend | Jinja2 HTML templates, CSS |

## Prerequisites

- Python 3.7 or higher
- A **Retreaver account** with RTB API access and a valid API key
  - Sign up at [retreaver.com](https://retreaver.com)

## Installation

```bash
pip install flask requests
```

## Configuration

Set your Retreaver API credentials as environment variables before running:

```bash
# Windows
set RETREAVER_API_KEY=your_api_key_here
set RETREAVER_CAMPAIGN_KEY=your_campaign_key_here

# Linux / macOS
export RETREAVER_API_KEY=your_api_key_here
export RETREAVER_CAMPAIGN_KEY=your_campaign_key_here
```

Or edit the API key values directly in `app.py` for local testing.

## Running

```bash
python app.py
```

Open `http://localhost:5000` in your browser, enter a caller number, and submit to retrieve the RTB bid response.

## API Endpoints

| Method | Route | Description |
|---|---|---|
| GET | `/` | Home page with caller number entry form |
| GET | `/get_bid?caller_number=<number>` | Queries Retreaver RTB API and returns bid data |

## Project Structure

```
├── app.py              # Main Flask app with RTB API integration (run this)
├── app1.py             # Alternate/development version
├── templates/
│   └── index.html      # Web UI form template
└── static/
    └── styles.css      # Page styling
```

## Output & Results

The `/get_bid` endpoint returns the raw JSON response from Retreaver, including:
- Bid amount (in USD)
- Buyer campaign information
- Call routing target (if a bid was won)

## Notes

- A valid Retreaver RTB API key is required — the app will return an error response without it
- RTB responses depend on active buyer campaigns in your Retreaver account; no active buyers = no bid
- `app1.py` is an alternate version with minor differences — `app.py` is the primary entry point
