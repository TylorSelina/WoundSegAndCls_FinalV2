# Wound Infection Assessment: Deep Learning vs Clinical Experts
This repository contains the minimal dataset and analysis code for the study:  
"Diagnostic accuracy of a two-stage deep learning model in assessing wound infection: a comparative study with expert clinicians"
##  Repository Contents
### Data Files
- `model_predictions.csv` - Deep learning model predictions on the independent test set
- `expert_assessments.csv` - Assessments from four clinical experts
- `test_set_metadata.csv` - Sample identifiers and ground truth labels

### Code Files
- `analysis_scripts/` - Python scripts for reproducing all statistical analyses and figures
- `requirements.txt` - Python package dependencies
## Minimal Dataset Description
The dataset represents the **independent test set** used for final model evaluation, containing:
### Core Data Structure
- 198 wound image samples with unique identifiers
- **Ground truth labels** for infection status (Non-infected/Infected) and severity levels (Non-infected/Mild/Moderate/Severe)
- Model prediction probabilities for each infection class
- Expert assessment probabilities from four clinical evaluators
