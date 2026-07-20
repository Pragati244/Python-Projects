# Sales Data Analysis using Pandas

## Overview

This project analyzes a sample sales dataset using Python and Pandas to answer common business questions. The objective is to demonstrate basic data analysis skills, including data exploration, aggregation, visualization, and generating business insights.

## Dataset

The dataset contains sales records with the following columns:

- Order ID
- Product
- Category
- Quantity
- Price
- Region

A new column, **Revenue**, is created by multiplying Quantity and Price.

## Business Questions Answered

The analysis answers the following questions:

- What is the total sales revenue?
- Which product generated the highest revenue?
- Which region generated the highest revenue?
- Which category sold the most units?
- What is the average order value?
- What are the top 5 orders by revenue?
- What is the sales summary by category?
- What is the sales summary by region?

## Technologies Used

- Python
- Pandas
- Matplotlib
- Jupyter Notebook

## Analysis Performed

- Loaded the dataset using Pandas
- Explored the dataset using descriptive statistics
- Created a Revenue column
- Performed aggregations using `groupby()`
- Sorted and filtered data
- Generated summary tables
- Created bar charts for revenue analysis
- Derived business insights and recommendations

## Visualizations

The project includes the following visualizations:

- Revenue by Region
- Revenue by Product

The charts are available in the `images` folder.

## Key Insights

Some examples of insights generated from the analysis include:

- The highest revenue-generating product was identified.
- The best-performing sales region was determined.
- Revenue contribution varies across product categories.
- High sales volume does not always result in the highest revenue.
- Sales performance differs significantly between regions.

## Recommendations

Based on the analysis, recommendations include:

- Increase focus on high-revenue products.
- Study the best-performing region to identify successful strategies.
- Improve marketing efforts in lower-performing regions.
- Explore opportunities to increase revenue from high-volume products.
- Continue monitoring sales trends to support business decisions.

## How to Run

1. Clone the repository.
2. Install the required libraries.

```bash
pip install pandas matplotlib
```

3. Open `sales_analysis.ipynb` in Jupyter Notebook or VS Code.
4. Run all cells to reproduce the analysis and visualizations.

## Learning Outcomes

Through this project, I learned how to:

- Load and analyze datasets using Pandas
- Perform data aggregation using `groupby()`
- Create calculated columns
- Generate summary tables
- Build visualizations with Matplotlib
- Interpret data to produce business insights and recommendations