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
using python 3.12 (make sure it's installed on your system):
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
        .venv\Scripts\Activate.ps1
        ```

4. Install dependencies:
    ```bash 
    pip install -r requirements.txt
    ```
## Environment variables & Docker setup
1. Configure environment variables
Create a .env file in the root directory by copying the example template:
    ```bash
    cp .env.example .env
    ```
2. Database container
Start the PostgreSQL database container using Docker Compose:
 ``` bash
 sudo docker compose up -d
 ```
## Running the ETL pipeline
 Run the ETL pipeline to extract data from Kaggle, transform/clean it, and load it into PostgreSQL:
    ```bash
    python -m src.pipeline
    ```
## Resources used
- Editor used: VScode
- Python Version : 3.12.13

## Source data
- The dataset used in this project is sourced from Kaggle: [Logistics Performance Dataset](https://www.kaggle.com/datasets/harshsingh2209/supply-chain-analysis)


## 🧹 Data Processing & Cleaning

The raw dataset underwent several cleaning and transformation steps in the ETL pipeline to optimize performance and ready the data for analysis:

### 1. Column Filtering & Dropping
* **Sensitive Data (PII):** Dropped customer first name and last name columns to ensure data privacy.
* **Redundant Location Data:** Removed `Order Zipcode` as location data is already represented by state and region columns.
* **Empty Columns:** Removed `Product Description` and `Product Status` due to missing/empty data across all records.
* **Duplicate Metrics:** Dropped redundant fields such as `Profit Per Order` and `Benefit Per Order`.

### 2. Renaming & Standardization
* Renamed `Sales` to `Gross Sales` and `Total Sales` to `Net Sales` for business metric clarity.

### 3. Data Type Conversions
* Parsed and converted date columns from raw string formats into standard `DATETIME` objects.

## Project Structure

```text
logistics_etl_project/
├── config/
│   └── config.py
├── data/
├── logs/
├── notebooks/
│   └── data_exploration.ipynb
├── scripts/
├── src/
│   ├── ingestion/
│   │   ├── bootstrap.py
│   │   ├── kaggle_boostraper.py
│   │   └── kaggle_extractor.py
│   ├── pipelines/
│   │   ├── db_loader.py
│   │   ├── time_shifter.py
│   │   └── transform_cleaner.py
│   ├── utils/
│   │   ├── logger_config.py
│   │   ├── responses.py
│   │   └── schemas.py
│   └── pipeline.py
├── tests/
├── docker-compose.yml
├── example.env
├── requirements.txt
├── LICENSE
└── README.md


## 💡 Key Business Insights & Recommendations

## 💡 Key Insights & Recommendations

### 📊 Key Insights

1. **System Issue in Late Delivery Calculation:**
   * Our overall late delivery rate is high (**54.83%**), but the actual shipping delay is only **2 days** on average. Also, most real shipments take **2 days**. This shows that the system itself has an aggressive target and misclassifies normal deliveries as "late".

2. **Unrealistic Delivery Targets for Express Shipping:**
   * **First Class** and **Second Class** shipping modes have very high late delivery percentages because the system gives them unrealistically short scheduled days.

3. **Declining Sales Trend:**
   * Total sales and revenue have been decreasing over the years, showing a need to review pricing and customer demand.

4. **Discount Impact on Profits:**
   * Profits drop significantly whenever discounts exceed **15%**, converting profitable orders into losses.

5. **Margin Pressure on High-Priced Items:**
   * Profitability decreases when product prices are too high, mainly because high prices combined with shipping costs reduce net margins.

---

### 🚀 Actionable Recommendations

1. **Set Realistic Scheduled Delivery Days:**
   * Adjust the scheduled delivery days in the system (e.g., set First Class to 2–3 realistic days instead of 1) to avoid falsely flagging normal orders as late.

2. **Set a Maximum Discount Cap:**
   * Limit automated discounts to **15%** to protect overall profit margins from dropping below zero.

3. **Ensure Price Covers All Costs:**
   * Implement a pricing rule to make sure the selling price always covers the **Product Cost + Shipping Cost + Minimum Profit Margin**.