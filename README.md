# Enterprise Data Engineering Pipeline 

## Project Overview
This project simulates a real-world enterprise data environment. It ingests raw transaction data, processes it through an ETL pipeline using **SSIS**, stores it in a Star Schema Data Warehouse in **SQL Server**, and performs advanced analytics using **Python** and **PySpark**.

## Architecture
1. **Source:** Raw CSV files (Sales, Products, Customers).
2. **ETL (Extract, Transform, Load):** SSIS package for data cleaning, Unicode handling, and error management.
3. **Data Warehouse:** SQL Server (Star Schema: `fact_Sales`, `dim_Customers`, `dim_Products`).
4. **Analytics:**
   - **Python (Pandas):** Data quality audit and revenue visualization.
   - **PySpark:** Big Data simulation for high-volume aggregation.

## Key Features
-  **Automated ETL:** SSIS package handles data truncation and type conversion.
-  **Business Intelligence:** SQL Views for calculating `TotalRevenue` and `CustomerLTV`.
-  **Scalability:** PySpark script designed to handle 1M+ rows.

## Technologies Used
- **Database:** Microsoft SQL Server, T-SQL
- **ETL:** SQL Server Integration Services (SSIS)
- **Languages:** Python 3.10, PySpark
- **Libraries:** Pandas, SQLAlchemy, Matplotlib

## How to Run
1. Execute the SQL script `01_Schema_Setup.sql` to create tables.
2. Open the SSIS solution `EnterpriseETL.sln` and run the package.
3. Run the Python audit script: `python project_audit.py`.