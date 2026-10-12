# Task 5 — Analytics Report & Insights Documentation

**Project:** Titanic Passenger Outcomes — A Data-Driven Safety and Equity Review  
**Author:** Monika

## Objective
Analyze passenger outcomes, compare observed survival rates across groups, communicate findings through visualizations, and make evidence-based recommendations with clear limitations.

## Files
- `Task5_Analytics_Report_Insights.ipynb` — complete analysis notebook with code, charts, calculations, and interpretations.
- `Task5_Analytics_Report.docx` — professional report for submission.
- `figures/` — exported figures used in the report.
- `requirements.txt` — Python dependencies.

## Dataset
Use the `train.csv` file already present in the parent internship repository. Keep it in the same directory as the notebook before running. The notebook computes metrics from the dataset at runtime.

## Run
```bash
pip install -r requirements.txt
jupyter notebook Task5_Analytics_Report_Insights.ipynb
```
Run all cells from top to bottom.

## Main findings (commonly used Titanic training set)
- 891 passenger records.
- 342 survived (38.38%); 549 did not survive (61.62%).
- Observed survival: about 74.2% for females and 18.9% for males.
- Observed survival by class: about 63.0% first class, 47.3% second class, 24.2% third class.

The notebook recalculates these values from `train.csv`. If the dataset version differs, use the notebook's output as the source of truth.

## Limitations
This is a historical observational dataset. Associations do not prove causation, and results should not be generalized to modern transport operations without external validation. Missing data and potential confounding must be considered.
