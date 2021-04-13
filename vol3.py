from fbprophet import Prophet
import pandas as pd
import datetime
import matplotlib.pyplot as plt

df = pd.read_csv("probka.csv")

orlen = df.loc[df["name"] == "PKNORLEN"]
orlen = orlen.drop(["name", "open", "high", "low", "volume"], axis=1)
orlen.columns = ['ds', 'y']
orlen.ds = pd.to_datetime(orlen.ds, format="%d-%m-%Y")
print(orlen.head())

m = Prophet()
m.fit(orlen)
future_dates = m.make_future_dataframe(periods=252)
start = datetime.datetime.strptime("01-01-2020", "%d-%m-%Y")
end = datetime.datetime.strptime("31-12-2020", "%d-%m-%Y")
interval = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days + 1) if x % 7 not in {2, 3} and x not in {0, 5, 100, 103, 121, 162, 315, 358, 359, 365}]

forecast = m.predict(future_dates)
# fig1 = m.plot(forecast)
# plt.show()
# fig2 = m.plot_components(forecast)
# plt.show()
