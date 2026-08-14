import joblib
import os

old_path = "models/random_forest_model.pkl"
new_path = "models/random_forest_model_compressed.pkl"

print("Loading current model...")
model = joblib.load(old_path)

print("Compressing model...")
joblib.dump(
    model,
    new_path,
    compress=("xz", 3)
)

old_size = os.path.getsize(old_path) / (1024 * 1024)
new_size = os.path.getsize(new_path) / (1024 * 1024)

print(f"Original model: {old_size:.2f} MB")
print(f"Compressed model: {new_size:.2f} MB")
print("Compression completed!")