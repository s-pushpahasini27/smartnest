# SmartNest India


## Run locally

Requires Python 3.10 or newer.

```sh
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1
# macOS/Linux:
# source .venv/bin/activate
pip install -r requirements.txt
flask --app app run
```

Visit http://127.0.0.1:5000. Use a production WSGI server when deploying.

## Features

- Optional state, city, budget and bedroom filters, with shareable GET URLs.
- Price and floor-area sorting, with filters preserved when returning from a listing.
- Saved homes using this browser's local storage; no account or server storage.
- Payment estimates with adjustable down payment, interest and term.
- Responsive layouts, labelled inputs, keyboard focus, image fallbacks and empty states.

The listing data, imagery and market text come from the original sample catalogue. They are not live or independently verified. Photos depend on external hosts; unavailable photos show a fallback. Agent contact and viewing booking are not implemented.

## Checks

```sh
python -m unittest discover -s tests -v
```
