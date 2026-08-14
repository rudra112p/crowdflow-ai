import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib


data = pd.read_csv("data/processed/numbat_2025_combined.csv")
data = data.sample(
    n=100000,
    random_state=42
)

print("Training dataset size:", data.shape)

features = [
    "From Station",
    "To Station",
    "Line",
    "Dir",
    "Day_Type",
    "Time_Slot"
]

target = "Passenger_Load"


X = data[features]
y = data[target]


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


categorical_features = features


preprocessor = ColumnTransformer(
    transformers=[
        (
            "categorical",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_features
        )
    ]
)


model = RandomForestRegressor(
    n_estimators=30,
    random_state=42,
    n_jobs=-1
)


pipeline = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("model", model)
    ]
)


print("Training model...")

pipeline.fit(X_train, y_train)

print("Training completed!")


predictions = pipeline.predict(X_test)


mae = mean_absolute_error(y_test, predictions)
rmse = mean_squared_error(y_test, predictions) ** 0.5
r2 = r2_score(y_test, predictions)


print("\nModel Evaluation:")
print("MAE:", mae)
print("RMSE:", rmse)
print("R²:", r2)


joblib.dump(
    pipeline,
    "models/random_forest_model.pkl"
)


print("\nModel saved successfully!")