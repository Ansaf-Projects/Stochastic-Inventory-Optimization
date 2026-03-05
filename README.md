# Stochastic Inventory Optimization & Safety Stock Analytics

**[📊 Click Here to View the Interactive Excel Dashboard (Google Drive)](https://csciitd-my.sharepoint.com/:x:/g/personal/me2240205_iitd_ac_in/IQAQmjCFdCSUSrVOvKpbCUL6Acs4GtNLfJsvyObZd3eTy2A?e=nTgRNU)**

### Overview
A data-driven supply chain model built to replace static inventory planning with a dynamic, stochastic framework. This project simulates 5 years of daily operations, quantifying the risk of both erratic customer demand and supplier lead-time delays to calculate an optimized, 30-day rolling Reorder Point (ROP).

### Business Impact & Results
Conducted sensitivity analysis on supplier reliability. The model mathematically proved that reducing supplier lead-time variability by 10% yields a **9.32% reduction in total inventory holding costs** without causing a single stockout.

### Tech Stack
* **Python (Pandas, NumPy):** Engineered the simulation engine and calculated daily rolling volatility metrics.
* **Excel & Power Query:** Automated the data pipeline to feed a dynamic, stakeholder-facing visual dashboard. 

### Mathematical Framework
Calculated the Standard Deviation of Demand during Lead Time ($\sigma_{dL}$) by combining independent daily demand variance and supplier lead-time variance. 

$$\sigma_{dL} = \sqrt{\mu_L \sigma_d^2 + \mu_d^2 \sigma_L^2}$$

Applied a 95% Service Level Z-score (1.645) to this combined volatility to generate a robust, mathematically defendable Safety Stock buffer.

---
*Note: Screenshot of the interactive dashboard below.*

![Dashboard Screenshot](https://1drv.ms/i/c/4b02c506aff1c048/IQBymjPC-tFcQKAXkJxexJU0Aei7fFgbHaPOaeTiIBPjL_E?e=TfJp2v)

