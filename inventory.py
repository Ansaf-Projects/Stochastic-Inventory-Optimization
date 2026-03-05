import pandas as pd
import numpy as np

# Set a random seed so your results are reproducible during interviews
np.random.seed(42)

# 1. Define Base Parameters for the Simulation
days = 1825 # 5 years of daily data
mu_demand = 100    # Average daily demand (units)
sigma_demand = 20  # Volatility of daily demand
mu_lead_time = 7   # Average supplier lead time (days)
sigma_lead_time = 2 # Volatility of supplier lead time
service_level_z = 1.645 # Z-score for a 95% Service Level

# 2. Generate Stochastic Data (Normal Distribution)
# np.maximum ensures we don't generate physically impossible negative demand or lead times
daily_demand = np.maximum(0, np.random.normal(mu_demand, sigma_demand, days))
lead_times = np.maximum(1, np.random.normal(mu_lead_time, sigma_lead_time, days))

# 3. Build the DataFrame
dates = pd.date_range(start="2021-01-01", periods=days)
df = pd.DataFrame({
    'Date': dates,
    'Daily_Demand': np.round(daily_demand, 0),
    'Lead_Time_Days': np.round(lead_times, 0)
})

# 4. Engineer the Dynamic Rolling Metrics (30-day window)
# This is what makes your ROP "dynamic" as claimed on your CV
df['Rolling_Avg_Demand'] = df['Daily_Demand'].rolling(window=30).mean()
df['Rolling_Std_Demand'] = df['Daily_Demand'].rolling(window=30).std()
df['Rolling_Avg_LT'] = df['Lead_Time_Days'].rolling(window=30).mean()
df['Rolling_Std_LT'] = df['Lead_Time_Days'].rolling(window=30).std()

# 5. Execute the Probabilistic Model Math
# Calculate Std Dev of Demand during Lead Time
df['Std_Dev_LT_Demand'] = np.sqrt(
    (df['Rolling_Avg_LT'] * (df['Rolling_Std_Demand']**2)) + 
    ((df['Rolling_Avg_Demand']**2) * (df['Rolling_Std_LT']**2))
)

# Calculate Final Safety Stock and ROP (Rounded up to nearest whole unit)
df['Safety_Stock'] = np.ceil(service_level_z * df['Std_Dev_LT_Demand'])
df['Dynamic_ROP'] = np.ceil((df['Rolling_Avg_Demand'] * df['Rolling_Avg_LT']) + df['Safety_Stock'])

# Drop the first 29 rows because they don't have enough data for a 30-day rolling average
df = df.dropna()

# 6. Export the Engine Output
df.to_csv('stochastic_inventory_data.csv', index=False)
print("Simulation complete! Check your folder for 'stochastic_inventory_data.csv'")