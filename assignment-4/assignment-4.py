#loud and inspect
df = pd.read_csv("data/raw_weather.csv")

print(df.head())
print(df.info())
print(df.describe())
#Cleaning & Preprocessing
# Convert Date column
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Drop rows with invalid dates
df = df.dropna(subset=['Date'])

# Select relevant columns
cols = ['Date', 'Temperature', 'Rainfall', 'Humidity']
df = df[cols]

# Handle missing values
df['Temperature'] = df['Temperature'].fillna(df['Temperature'].mean())
df['Rainfall'] = df['Rainfall'].fillna(0)
df['Humidity'] = df['Humidity'].fillna(df['Humidity'].median())
df.to_csv("output/cleaned_weather.csv", index=False)
df.head()
#Statistical Analysis (NumPy)
daily_mean_temp = np.mean(df['Temperature'])
monthly_stats = df.resample('M', on='Date').agg({
    'Temperature': ['mean', 'min', 'max', 'std'],
    'Rainfall': 'sum'
})
yearly_stats = df.resample('Y', on='Date').agg({
    'Temperature': ['mean', 'min', 'max']
})

print("Daily Temp Mean:", daily_mean_temp)
print("Monthly Stats:\n", monthly_stats)
print("Yearly Stats:\n", yearly_stats)
#Matplotlib Visualizations
 #1:Daily Temperature Trend
plt.figure(figsize=(10,5))
plt.plot(df['Date'], df['Temperature'], color='red')
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.title("Daily Temperature Trend")
plt.savefig("output/daily_temperature_trend.png")
plt.show()
 #2:Monthly Rainfall Bar Chart
monthly_rain = df.resample('M', on='Date')['Rainfall'].sum()

plt.figure(figsize=(10,5))
plt.bar(monthly_rain.index, monthly_rain.values)
plt.xlabel("Month")
plt.ylabel("Rainfall (mm)")
plt.title("Monthly Rainfall Totals")
plt.savefig("output/monthly_rainfall.png")
plt.show()
 #3:Humidity vs Temperature Scatter Plot
plt.figure(figsize=(7,5))
plt.scatter(df['Temperature'], df['Humidity'], alpha=0.6)
plt.xlabel("Temperature (°C)")
plt.ylabel("Humidity (%)")
plt.title("Humidity vs Temperature")
plt.savefig("output/humidity_vs_temperature.png")
plt.show()
#4:Combined Plot
fig, ax = plt.subplots(2, 1, figsize=(10,10))

ax[0].plot(df['Date'], df['Temperature'], color='red')
ax[0].set_title("Daily Temperature Trend")

ax[1].scatter(df['Temperature'], df['Humidity'], alpha=0.5)
ax[1].set_title("Humidity vs Temperature")

plt.tight_layout()
plt.savefig("output/combined_plots.png")
plt.show()
 #5:Grouping & Aggregation
df['Month'] = df['Date'].dt.month
df['Season'] = df['Month'].map({
    12:"Winter",1:"Winter",2:"Winter",
    3:"Spring",4:"Spring",5:"Spring",
    6:"Summer",7:"Summer",8:"Summer",
    9:"Autumn",10:"Autumn",11:"Autumn"
})

seasonal_summary = df.groupby("Season")['Temperature','Rainfall','Humidity'].mean()
monthly_summary = df.groupby("Month")['Temperature','Rainfall','Humidity'].mean()

print(seasonal_summary)
print(monthly_summary)
 #6:Export Output
df.to_csv("output/cleaned_weather.csv", index=False)
print("Export Successful!")
