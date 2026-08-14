import pandas as pd

file_path = "data/raw/NBT25MON_Outputs.xlsx"

link_loads = pd.read_excel(
    file_path,
    sheet_name="Link_Loads",
    header=2
)

print("Link_Loads dataset size:")
print(link_loads.shape)

print("\nColumn names:")
print(link_loads.columns.tolist())

print("\nFirst 10 rows:")
print(link_loads.head(10))
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

print("\nReshaped NUMBAT size:")
print(long_data.shape)

print("\nFirst 10 reshaped rows:")
print(long_data.head(10))