import pandas as pd
import matplotlib.pyplot as plt

def preprocessing(dataset, start_date, end_date):
    # The date format in the file is in a day-first format, which matplotlib does nto understand.
    # so we need to convert it.
    dataset['Local time'] = pd.to_datetime(dataset['Local time'],dayfirst=True)
    dataset = dataset[dataset['Local time'].between(start_date,end_date)]
    return dataset
    

def plot_data(dates, values):
    fig, ax = plt.subplots()
    ax.plot(dates, values)
    # label the axes
    ax.set_xlabel("Date of observation")
    ax.set_ylabel("Temperature in Celsius")
    ax.set_title("Temperature Observations")
    # adjust tick labels
    fig.autofmt_xdate()
    return ax,fig

