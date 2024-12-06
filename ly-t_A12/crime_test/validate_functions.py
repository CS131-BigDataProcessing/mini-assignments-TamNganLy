import pandas as pd

def validate_vict_sex(df):
    if 'Vict Sex' not in df.columns:
        return False
    if not df['Vict Sex'].isin(['M', 'F']).all():
        return False
    return True

def validate_vict_age(df):
    if 'Vict Age' not in df.columns:
        return False
    if df['Vict Age'].isnull().any() or not df['Vict Age'].between(1, 100).all():
        return False
    return True

def main(file_path="Crime_Data_from_2020_to_Present.csv"):
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return

    print("Validating 'Vict Sex' and 'Vict Age' columns:")
    if validate_vict_sex(df):
        print("'Vict Sex' validation passed.")
    else:
        print("'Vict Sex' validation failed.")
    
    if validate_vict_age(df):
        print("'Vict Age' validation passed.")
    else:
        print("'Vict Age' validation failed.")

if __name__ == "__main__":
    main()
