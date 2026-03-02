# RTB Caller Bid API

A Flask web application that integrates with the **Retreaver RTB API** to retrieve real-time bid information for incoming caller numbers. Users enter a caller number on the web UI and the app queries the Retreaver RTB endpoint, displaying the bid response.

## Tech Stack

- **Python** — Flask, requests
- **Frontend** — Jinja2 HTML templates, CSS

## Project Structure

```
├── app.py              # Main Flask app with RTB API integration
├── app1.py             # Alternate version
├── templates/
│   └── index.html      # Web UI template
└── static/
    └── styles.css      # Styling
```

## Endpoints

| Method | Route | Description |
|--------|-------|-------------|
| GET | `/` | Home page with caller number form |
| GET | `/get_bid?caller_number=<number>` | Fetches bid from Retreaver RTB API |

## Running

```bash
pip install flask requests
python app.py
```

Open `http://localhost:5000` and enter a caller number to retrieve bid data.
