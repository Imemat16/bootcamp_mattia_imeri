# Project: Magnificent 7 Momentum & Correlation Analysis

## Project Summary
**Objective:** The Magnificent 7 stocks heavily dictate the broader market's direction. This project acquires historical daily trading data for these seven equities to analyze price momentum, trading volume spikes, and cross-asset correlations, ultimately aiming to engineer features that predict short-term price direction[cite: 11]. 

## Stakeholder Context
**Target Audience:** Retail swing traders and portfolio managers[cite: 11].
**Goals:** These stakeholders care about identifying leading indicators—such as a volume breakout in Nvidia predicting a delayed sympathetic move in Microsoft—to optimize entry and exit points for short-term trades[cite: 11].

## Lifecycle Mapping
* **Stage 01:** Problem Framing (This document)[cite: 11]
* **Stage 02:** Tooling Setup (Scaffold and Git version control)[cite: 12]
* **Stage 03:** Python Fundamentals (Reusable financial utilities)[cite: 13]
* **Stage 04:** Data Acquisition (yfinance API pipeline)
* **Stage 05:** Data Storage (Env-driven CSV routing)
* **Stage 06:** Data Preprocessing (Handling trading days and scaling)

## Data Storage Strategy
* **Structure:** Raw, immutable stock data pulled from the API is saved to `data/raw/`. Cleaned and transformed datasets are saved to `data/processed/`[cite: 15].
* **Formats:** CSV is used for raw ingestion to maintain human-readable validation. Processed data is also stored as CSV for cross-platform compatibility[cite: 15].
* **Routing:** All I/O operations dynamically use `os.getenv()` to target paths defined in the local `.env` file[cite: 15].

## Preprocessing & Cleaning Assumptions
* **Missing Data:** Stock markets close on weekends and holidays. Missing dates are forward-filled (`ffill`) assuming the last known closing price remains the active valuation during closed hours[cite: 16].
* **Feature Engineering:** We calculate daily percentage returns rather than using absolute prices, as absolute prices cannot be cleanly compared across assets (e.g., NVDA vs. AAPL)[cite: 16].
* **Scaling:** Trading volumes are normalized using Min-Max scaling so machine learning algorithms don't disproportionately weight companies with inherently higher outstanding share counts[cite: 16].