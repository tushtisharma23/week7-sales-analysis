# Sales Data Analysis System

A comprehensive Python-based Sales Data Analysis System developed as part of my Week 7 internship project at The Developer Arena.

The project loads and cleans sales data, performs business-oriented analysis, identifies important sales trends, generates visualizations, and exports analytical reports in multiple formats.

## Developed By

**Tushti Sharma**

## Project Features

- Load sales data from CSV and Excel files
- Detect and handle missing values
- Remove duplicate records
- Convert and correct data types
- Calculate total sales and average order value
- Analyze sales by product category
- Identify top-selling products
- Analyze monthly sales trends
- Calculate month-over-month sales growth
- Analyze customer purchasing patterns
- Identify peak sales periods
- Analyze geographical sales distribution
- Calculate simple moving averages
- Generate line, bar, and pie charts
- Export analysis results to CSV
- Generate multi-sheet Excel reports
- Generate text-based sales summary reports
- Interactive command-line interface

## Project Structure

    week7-sales-analysis/
    │
    ├── sales_analyzer/
    │   ├── __init__.py
    │   ├── data_loader.py
    │   ├── data_cleaner.py
    │   ├── analyzer.py
    │   ├── visualizer.py
    │   └── reporter.py
    │
    ├── notebooks/
    │   ├── exploration.ipynb
    │   └── analysis.ipynb
    │
    ├── data/
    │   ├── raw/
    │   │   └── sales_data.csv
    │   ├── processed/
    │   │   └── cleaned_sales_data.csv
    │   └── reports/
    │
    ├── tests/
    ├── requirements.txt
    ├── README.md
    ├── .gitignore
    └── main.py

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- OpenPyXL

## Installation

Install the required Python libraries using:

    pip install -r requirements.txt

## How to Run

Run the application from the project root directory:

    python main.py

## Command-Line Options

The application provides the following options:

1. View Basic Statistics
2. View Sales by Category
3. View Top Products
4. View Monthly Sales Trends
5. View Customer Analysis
6. Generate Visualizations
7. Generate Reports
8. Generate All Visualizations and Reports
0. Exit

## Analysis Performed

The system calculates and analyzes:

- Total Sales
- Total Orders
- Average Order Value
- Unique Customers
- Unique Products
- Sales by Product Category
- Top-Selling Products
- Monthly Sales Trends
- Monthly Sales Growth Rate
- Customer Purchase Patterns
- Peak Sales Month
- Regional Sales Performance

## Visualizations

The project generates the following visual reports:

- Monthly Sales Trend Line Chart
- Category Sales Bar Chart
- Category Sales Distribution Pie Chart
- Regional Sales Bar Chart

Generated visualizations are stored inside:

    data/reports/

## Reports Generated

The system exports analysis results in multiple formats:

- Text Summary Report
- CSV Analysis Reports
- Excel Sales Analysis Report

The Excel report contains separate sheets for:

- Summary
- Category Analysis
- Top Products
- Monthly Trends
- Customer Analysis
- Regional Analysis

## Sample Analysis Results

Based on the sample sales dataset:

- Total Sales: Rs. 324,200.00
- Total Orders: 24
- Average Order Value: Rs. 13,508.33
- Unique Customers: 15
- Unique Products: 20
- Highest Sales Month: November 2025
- Peak Monthly Sales: Rs. 65,800.00

## Learning Outcomes

Through this project, I gained practical experience in:

- Data loading and preprocessing
- Data cleaning using Pandas
- Exploratory data analysis
- Business data analysis
- Data aggregation and grouping
- Sales trend analysis
- Data visualization using Matplotlib
- Report generation using Pandas and OpenPyXL
- Building modular Python applications
- Creating command-line interfaces

## Future Improvements

Future versions of the project can include:

- Interactive dashboard
- Advanced sales forecasting
- Customer cohort analysis
- Customer lifetime value analysis
- Automated business recommendations
- Interactive HTML reports

## Author

**Tushti Sharma**

Week 7 Internship Project  
The Developer Arena 