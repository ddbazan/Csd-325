import csv
from datetime import datetime
from matplotlib import pyplot as plt
import sys

filename = 'sitka_weather_2018_simple.csv'

def get_date_and_temperatures(data_type):
    """
    Get dates and specified temperature data from the CSV file.
    """
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        # Get dates and temperatures from this file.
        dates, temps = [], []
        for row in reader:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            dates.append(current_date)
            if data_type == 'highs':
                temps.append(int(row[5]))
            elif data_type == 'lows':
                temps.append(int(row[6]))

    return dates, temps

def plot_temperatures(data_type):
    """
    Plot the specified temperature data against dates.
    """
    dates, temps = get_date_and_temperatures(data_type)

    fig, ax = plt.subplots()
    ax.plot(dates, temps, c='red' if data_type == 'highs' else 'blue')
    plt.title(f"Daily {data_type} temperatures - 2018", fontsize=24)
    plt.xlabel('Date', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.show()

def main():
    while True:
        print("Menu: Select an option")
        print("1. View High Temperatures")
        print("2. View Low Temperatures")
        print("3. Exit")

        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            plot_temperatures('highs')
        elif choice == '2':
            plot_temperatures('lows')
        elif choice == '3':
            print("Exiting the program. Thank you!")
            sys.exit()
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()