## Data Cleaning Strategy

Our data preprocessing pipeline transforms messy raw data into a machine-learning-ready format. The following modular cleaning functions are applied (found in `src/cleaning.py`):

1. **Median Imputation (`fill_missing_median`)**: Missing numeric values are filled using the column's median to avoid skewing data with extreme outliers.
2. **Targeted Row Deletion (`drop_missing`)**: Rows with missing categorical data are explicitly dropped, as imputing synthetic text categories introduces unacceptable bias.
3. **Min-Max Normalization (`normalize_data`)**: Numeric columns are scaled mathematically to a strict `0.0` to `1.0` range. This standardizes features so algorithms weight them equally regardless of their native unit sizes.

**Workflow:** Raw data is pulled from `data/raw/`, processed through these functions in the preprocessing notebook, and the finalized dataset is output to `data/processed/`.