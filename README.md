# Stochastic Inventory Optimization & Safety Stock Analytics
## Overview
A data-driven supply chain model built to replace static inventory planning with a dynamic, stochastic framework. This project simulates 5 years of daily operations, quantifying the risk of both erratic customer demand and supplier lead-time delays to calculate an optimized, 30-day rolling Reorder Point (ROP).

## Tech Stack

Python (Pandas, NumPy): Engineered the simulation engine and calculated daily rolling volatility metrics.

Excel & Power Query: Automated the data pipeline to feed a dynamic, stakeholder-facing visual dashboard.

## Mathematical Framework
Calculated the Standard Deviation of Demand during Lead Time by mathematically combining daily demand variance and supplier lead-time variance. Applied a 95% Service Level Z-score to generate a robust Safety Stock buffer.

## Business Impact & Results
Conducted sensitivity analysis on supplier reliability. The model mathematically proved that reducing supplier lead-time variability by 10% yields a 9.32% reduction in total inventory holding costs without causing a single stockout.


