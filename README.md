# Bootcamp Repository
## Folder Structure
- **homework/** → All homework contributions will be submitted here.
- **project/** → All project contributions will be submitted here.
- **class_materials/** → Local storage for class materials. Never pushed to
GitHub.

## Homework Folder Rules
- Each homework will be in its own subfolder (`homework0`, `homework1`, etc.)
- Include all required files for grading.
## Project Folder Rules
- Keep project files organized and clearly named.

## Data Storage Layer Specification

### Architecture & Folder Framework
The storage framework routes raw data and processed files into specific, separated directories:
* `data/raw/`: Dedicated landing zone for incoming immutable data snapshots (stored as CSV format).
* `data/processed/`: Optimized analytical workspace containing validated, clean data layers saved as binary Parquet files.

### Environment Variables Configuration
To ensure portability across different host servers and systems, paths are tracked outside the codebase using environment configuration settings:
* `DATA_DIR_RAW`: Establishes the folder path for original raw data.
* `DATA_DIR_PROCESSED`: Establishes the folder path for cleaned parquet data.

### Format Strategy
* **CSV (Raw)**: Preserves text-based human legibility and open-standard compatibility for raw files.
* **Parquet (Processed)**: Provides fast columnar data compression, speeds up lookups, and keeps precise numeric tracking types intact for calculations.

## Preprocessing & Cleaning Strategy
* **Imputation**: Numeric missing values are handled via median imputation to prevent severe outliers from heavily distorting the distribution.
* **Deletion**: Missing categorical attributes are systematically dropped. It is assumed that interpolating structural text attributes introduces unacceptable synthetic bias.
* **Scaling**: Continuous numeric features are transformed via Min-Max normalization to standard ranges, assuming downstream models require scale-agnostic feature balancing.