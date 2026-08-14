import pandas as pd


files = {
    "Monday": "data/raw/NBT25MON_Outputs.xlsx",
    "TWT": "data/raw/NBT25TWT_Outputs.xlsx",
    "Friday": "data/raw/NBT25FRI_Outputs.xlsx",
    "Saturday": "data/raw/NBT25SAT_Outputs.xlsx",
    "Sunday": "data/raw/NBT25SUN_Outputs.xlsx"
}


id_vars = [
    "Link",
    "Line",
    "Dir",
    "Order",
    "From NLC",
    "From ASC",
    "From Station",
    "To NLC",
    "To ASC",
    "To Station"
]


all_data = []


for day_type, file_path in files.items():

    print(f"Processing {day_type}...")

    link_loads = pd.read_excel(
        file_path,
        sheet_name="Link_Loads",
        header=2
    )

    time_columns = [
        col for col in link_loads.columns
        if isinstance(col, str) and "-" in col
    ]

    long_data = link_loads.melt(
        id_vars=id_vars,
        value_vars=time_columns,
        var_name="Time_Slot",
        value_name="Passenger_Load"
    )

    long_data["Day_Type"] = day_type

    all_data.append(long_data)


combined_data = pd.concat(
    all_data,
    ignore_index=True
)


combined_data = combined_data.dropna(
    subset=["Passenger_Load"]
)


combined_data.to_csv(
    "data/processed/numbat_2025_combined.csv",
    index=False
)


print("\nCombined dataset created successfully!")

print("\nDataset size:")
print(combined_data.shape)

print("\nDay types:")
print(combined_data["Day_Type"].value_counts())

print("\nPassenger load statistics:")
print(combined_data["Passenger_Load"].describe())

print("\nFirst 10 rows:")
print(combined_data.head(10))