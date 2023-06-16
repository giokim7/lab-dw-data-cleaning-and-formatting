import pandas as pd

def rename_columns(file1):
    file1 = file1.rename(columns={'ST': 'State', 'GENDER': 'Gender'})
    return file1

def clean_invalid_values(file1):
    gender_mapping = {
        'F': 'Female',
        'M': 'Male',
        'Femal': 'Female',
        'Male': 'Male',
        'female': 'Female'
    }
    file1['Gender'] = file1['Gender'].replace(gender_mapping)
    return file1

def format_dataset(file1):
    file1["Customer"] = file1["Customer"].astype(str)
    file1["State"] = file1["State"].astype(str)
    file1["Gender"] = file1["Gender"].astype(str)
    file1["Education"] = file1["Education"].astype(str)
    file1["Income"] = file1["Income"].astype(float)
    file1["Monthly Premium Auto"] = file1["Monthly Premium Auto"].astype(float)
    file1["Policy Type"] = file1["Policy Type"].astype(str)
    file1["Vehicle Class"] = file1["Vehicle Class"].astype(str)
    file1["Total Claim Amount"] = file1["Total Claim Amount"].astype(float)
    return file1

def drop_nulls(file1):
    file1 = file1.dropna()
    return file1

def dealing_duplicates(file1):
    file2 = file1.drop_duplicates()
    file2 = file1.duplicated(keep=False)
    return file1, file2

def main():
    # Read the dataset
    file1 = pd.read_csv("https://raw.githubusercontent.com/data-bootcamp-v4/data/main/file1.csv")

    # Rename columns
    file1 = rename_columns(file1)

    # Clean invalid values
    file1 = clean_invalid_values(file1)

    # Format the dataset
    file1 = format_dataset(file1)

    # Drop null values
    file1 = drop_nulls(file1)

    # Deal with duplicates
    file1, file2 = dealing_duplicates(file1)

    # Print the processed data
    print(file1.head())
    print(file2.head())

# Call the main function
main()