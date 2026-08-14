import pandas as pd

file_path = "data/raw/LUTrainLoadingData (3).xls"

data = pd.read_csv(file_path)

print("Dataset size:")
print(data.shape)

print("\nColumn names:")
print(data.columns.tolist())

print("\nFirst 5 rows:")
print(data.head())
id_vars = [
    "From_Station",
    "To_Station",
    "Line",
    "Line_Direction",
    "Platform_Direction",
    "NAPTAN_From",
    "NAPTAN_To",
    "Direction"
]

time_columns = [col for col in data.columns if "-" in col]

long_data = data.melt(
    id_vars=id_vars,
    value_vars=time_columns,
    var_name="Time_Slot",
    value_name="Passenger_Load"
)

print("\nReshaped dataset size:")
print(long_data.shape)

print("\nFirst 10 reshaped rows:")
print(long_data.head(10))
clean_data = long_data.dropna(subset=["Passenger_Load"])

print("\nCleaned dataset size:")
print(clean_data.shape)

print("\nFirst 10 cleaned rows:")
print(clean_data.head(10))

clean_data.to_csv(
    "data/processed/cleaned_train_loading.csv",
    index=False
)

print("\nCleaned dataset saved successfully!")
print("\nPassenger Load Statistics:")
print(clean_data["Passenger_Load"].describe())

print("\nMinimum Passenger Load:")
print(clean_data["Passenger_Load"].min())

print("\nMaximum Passenger Load:")
print(clean_data["Passenger_Load"].max())