import pandas as pd

def calculate_mean_age(df):
    return df['Vict Age'].mean()

def calculate_median_age(df):
    return df['Vict Age'].median()

def main(file_path="Crime_Data_from_2020_to_Present.csv"):
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return

    print("Calculating the mean and median age:")
    print("Mean:", calculate_mean_age(df))
    print("Median:", calculate_median_age(df))

if __name__ == "__main__":
    main()