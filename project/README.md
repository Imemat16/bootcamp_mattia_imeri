# Project Title: [Insert Name Here]

## Project Summary
**Objective:** [State what real-world problem you are solving and why it matters in 1-2 paragraphs].

## Stakeholder Context
**Target Audience:** [Who will use this? e.g., Quantitative analysts, risk managers, or retail investors].
**Goals:** [What do they care about? e.g., Minimizing latency, maximizing risk-adjusted returns].

## Lifecycle Mapping
* **Stage 01:** Problem Framing (This document)
* **Stage 02:** Tooling Setup (Scaffold and Git)
* **Stage 03:** Python Fundamentals (Reusable utilities)
* **Stage 04:** Data Acquisition (API/Scraping pipeline)
* **Stage 05:** Data Storage (Parquet/CSV env-routing)

## Data Storage
* **Structure:** Raw, immutable data is stored in `data/raw/`. Cleaned, analytical data is stored in `data/processed/`.
* **Formats:** We use CSV for human-readable raw ingestion, and Parquet for processed data to preserve strict numeric dtypes and columnar compression.
* **Routing:** All I/O operations utilize `os.getenv()` to pull `DATA_DIR_RAW` and `DATA_DIR_PROCESSED` from the local environment variables.