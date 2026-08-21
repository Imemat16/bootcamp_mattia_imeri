# Spaceship Titanic: Passenger Rescue Prediction

## Project Summary
The Spaceship Titanic, an interstellar passenger liner, collided with a spacetime anomaly, resulting in the disappearance of nearly half of its passengers. The problem we are solving is accurately predicting which specific passengers were transported to an alternate dimension based on their recovered personal records, billing history, and location on the ship. This section satisfies the requirement to provide a short project summary of the problem and why it matters[cite: 1, 2].

Solving this problem matters because it directly dictates emergency response and resource allocation. By identifying the missing passengers, search and rescue teams can prioritize their operations, while interstellar transport authorities can update future safety protocols.

## Stakeholder Persona & Context
**Primary Stakeholders:** Interstellar Search and Rescue (IS&R) Command & Cosmic Transport Executives. This addresses the requirement to include a stakeholder persona or context description[cite: 1, 2].

**Who will use the results and what they care about**[cite: 1, 2]:
* **Resource Efficiency:** They need accurate predictions to avoid wasting time and fuel searching for passengers who are still safely aboard.
* **Risk Factors:** They want to know the structural or demographic factors that made certain passengers vulnerable to the anomaly.

## Goals Lifecycle Deliverables Mapping
To achieve our stakeholder objectives, this project follows a structured data lifecycle, mapping our goals to specific lifecycle stage deliverables[cite: 1, 2]:

* **Stage 01: Problem Framing & Scoping:** Define the real-world problem and stakeholder goals[cite: 1, 2].
  * **Deliverable:** This `README.md` file establishing the project summary and stakeholder context[cite: 1, 2].
* **Stage 02: Tooling Setup:** Set up the project environment and file structure[cite: 3].
  * **Deliverable:** Initialized GitHub repository with the required scaffolding and an explanation of the project purpose[cite: 3].
* **Stage 03: Python Fundamentals:** Ensure foundational scripts are built to support future work[cite: 4].
  * **Deliverable:** Reusable utility functions established for later pipeline stages[cite: 4].
* **Stage 04: Data Acquisition & Ingestion:** Acquire data programmatically[cite: 5]. 
  * **Deliverable:** Raw data saved in the `data/raw/` folder alongside ingestion scripts[cite: 5].
* **Stage 05: Data Storage:** Save and reload raw data reproducibly using environment-driven paths[cite: 6].
  * **Deliverable:** A documented Data Storage section (below) explaining folder structures and file formats[cite: 6].
* **Stage 06: Data Preprocessing:** Clean, transform, and prepare the dataset for modeling[cite: 7].
  * **Deliverable:** Reusable data cleaning functions stored in `src/cleaning.py` and documented preprocessing assumptions[cite: 7].

## Project Structure
The repository is initialized with the following structure to support all future stages of the project lifecycle[cite: 3]:

├── data/            
│   ├── raw/         
│   └── processed/   
├── notebooks/       
├── src/             
├── docs/            
├── reports/         
├── model/           
└── README.md        

## Data Acquisition & Storage
**Sources & Validation:** The raw dataset is acquired programmatically via the Kaggle API (`kagglehub`). We document these sources, parameters, and validations as required[cite: 5]. 

**Storage Conventions:** 
* **Folder Structure:** Raw API downloads are extracted and stored in `data/raw/`, while ML-ready data will be saved to `data/processed/`[cite: 6]. 
* **File Formats:** The data is primarily handled in `.csv` format[cite: 6]. 
* **Data Reading:** The code loads these files securely utilizing an `.env` file to manage API credentials and uses environment-driven paths (e.g., via `os.getenv()`) to ensure the input/output code is reproducible across different machines[cite: 6].

## Data Preprocessing: Assumptions & Rationale
During the data cleaning stage, we developed reusable preprocessing functions stored in `src/cleaning.py`[cite: 7]. Below is the documentation of assumptions made during cleaning and their rationale[cite: 7]:

* **Assumption 1 (CryoSleep Logic):** Passengers in suspended animation cannot spend money. 
  * *Rationale:* If `CryoSleep == True`, missing financial features (RoomService, Spa, etc.) are deterministically imputed as `0`.
* **Assumption 2 (Group Deduction):** Passengers sharing the same Group ID in their `PassengerId` are traveling together (e.g., families).
  * *Rationale:* Missing categorical data like `HomePlanet` and `Cabin` can be safely imputed by copying the known values of other passengers sharing the same Group ID.
* **Assumption 3 (Missingness as a Feature):** Blank cells are not always random errors; they may contain hidden signals.
  * *Rationale:* Before filling any blanks, binary indicator columns (e.g., `Age_is_missing`) are created to preserve the original state of the dataset.