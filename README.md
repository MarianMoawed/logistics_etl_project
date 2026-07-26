# logistics_etl_project

## Project overview

This project is an End-to-End ETL Pipeline for logistics data that automates data ingestion from the Kaggle API. It processes, cleans, and structures raw data into a clean format ready for analytical modeling and dashboard reporting.

## Prerequisites
1. Make sure to have python 3.12.x installed on your machine.

2. Make sure you have your Kaggle API credentials (kaggle.json) configured in your environment (~/.kaggle/ on Linux/macOS or %USERPROFILE%\.kaggle\ on Windows).


## Installation & setup

1. clone the repository
```bash
git clone https://github.com/MarianMoawed/logistics_etl_project.git

cd logistics_etl_project
``` 
2. create a virtual environment:
using python 3.10 (make sure it's installed on your system):
    ```bash 
    python3.12 -m venv .venv
    ```

3. activate the virtual environment:
    - linux/macOS:
        ```bash 
        source .venv/bin/activate
        ```
    - Windows (command prompt):
        ```cmd
        .venv\Scripts\Activate.bat
        ```
        
    - windows (PowrShell):
        ```PowerShell 
        .venv\Scrips\Activate.ps1
        ```

4. Install dependencies:
    ```bash 
    pip install -r requirements.txt
    ```
5. Running the pipline
    ```bash
    python -m src.pipeline
    ```
## Resources used
- Editor used: VScode
- Python Version : 3.12.13

## Source data
- The dataset used in this project is sourced from Kaggle: [Logistics Performance Dataset](https://www.kaggle.com/datasets/harshsingh2209/supply-chain-analysis)


## Data processing
*Details coming soon....*

## Project Structure
*Details coming soon....*