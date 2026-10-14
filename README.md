# SmartNest India

### A place to call yours.

SmartNest makes finding your next home simpler. Explore property listings, narrow your search to what matters, save your favourites, and estimate monthly payments—all in a clean, responsive interface.

## Features

- **Search your way** — Filter homes by state, city, budget and bedroom count. Use only the filters you need.
- **Compare the essentials** — Sort by price or floor area and review bedrooms, bathrooms, size and asking price.
- **Keep your favourites** — Save homes to a shortlist that stays available in the same browser.
- **Get to know a place** — Read property descriptions, neighbourhood information and listing insights.
- **Plan your budget** — Estimate monthly loan payments with adjustable down payment, annual interest rate and loan term.
- **Pick up where you left off** — Share search URLs and return from a property page with your filters preserved.
- **Browse comfortably** — Responsive layouts, labelled inputs, keyboard focus indicators, empty states and image fallbacks.
- **Preview account pages** — Matching login and sign-up screens with email validation, password visibility and password confirmation.

> **Account pages are UI previews.** They do not create accounts or log users in. Entered credentials are neither submitted nor stored.

## Getting started

### Requirements

- Python 3.10 or newer
- Git to clone the repository
- A modern web browser

### 1. Get the project

```sh
git clone https://github.com/s-pushpahasini27/smartnest.git
cd smartnest
python -m venv .venv
```

On macOS or Linux, use `python3` if `python` is unavailable.

### 2. Install and run

**Windows PowerShell**

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m flask --app app run
```

**macOS / Linux**

```sh
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m flask --app app run
```

Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser. Stop the server with `Ctrl+C`.

The catalogue runs locally without API keys or a database. An internet connection is needed to install dependencies and load externally hosted property photos and fonts.

## Explore the app

| Page | Address | What you can do |
| --- | --- | --- |
| Home | `/` | Discover featured homes and start a search |
| All homes | `/?browse=1` | Filter and sort the catalogue |
| Saved homes | `/?browse=1&saved=1` | Revisit your browser’s shortlist |
| Property details | `/property/<id>` | Review a home, share its link and estimate payments |
| Login preview | `/login` | Try the login interface; also available at `/sign-in` |
| Sign-up preview | `/signup` | Try the registration interface |

You can browse and save homes without an account. Saved homes use local storage: they do not sync between browsers or devices, and clearing browser data removes the shortlist.

## Project structure

```text
smartnest/
├── app.py                 # Flask routes, catalogue, filters and price formatting
├── requirements.txt       # Python dependencies
├── static/
│   ├── style.css          # Shared design and responsive layouts
│   ├── app.js             # Saved homes, city filters, sharing and payment estimates
│   ├── auth.css           # Account-page styles
│   └── auth.js            # Account-preview validation and password controls
├── templates/
│   ├── base.html          # Shared page layout and navigation
│   ├── index.html         # Landing page
│   ├── results.html       # Search results and saved homes
│   ├── detail.html        # Property details
│   ├── auth.html          # Login and sign-up previews
│   ├── _filters.html      # Shared search form
│   ├── _card.html         # Shared property card
│   └── 404.html           # Missing-page view
└── tests/
    └── test_app.py        # Catalogue and route checks
```

Property records are defined in `app.py`. Keep each property’s ID unique and provide its title, location, price, bedrooms, bathrooms, area, image, description, neighbourhood and trends. Prices are in Indian rupees and floor areas are in square feet.

## Run checks

**Windows PowerShell**

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

**macOS / Linux**

```sh
.venv/bin/python -m unittest discover -s tests -v
```

The checks cover catalogue rendering, property detail pages, missing properties, filtering, sorting, empty results, invalid filter values, legacy search submissions, price formatting and static assets. Browser interactions such as saved homes and account-preview validation should also be checked in a browser.

## Current scope

- Listings and market text are sample catalogue content, not a live property feed. Availability and market claims have not been independently verified.
- Property photos come from external hosts. Unavailable photos display a fallback.
- EMI figures are illustrative loan estimates, excluding fees, taxes and insurance.
- Account authentication, agent contact and viewing bookings are not connected.
- Flask’s built-in server is for local development. Use a production WSGI server and an appropriate deployment configuration when hosting the app.
