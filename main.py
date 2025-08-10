import os
import pandas as pd

# Load renaming plan
plan_path = "RENAMING_PLAN.md"
df = pd.read_csv(plan_path, sep="|", skiprows=2, names=["old", "new", "extra"], engine="python")
df = df[["old", "new"]].applymap(str.strip)

# Rename files/folders
base_path = "."  # change if needed
for old_name, new_name in zip(df["old"], df["new"]):
    old_path = os.path.join(base_path, old_name)
    new_path = os.path.join(base_path, new_name)

    if os.path.exists(old_path) and old_name != new_name:
        os.rename(old_path, new_path)
        print(f"Renamed: {old_name} -> {new_name}")
    else:
        print(f"Skipped: {old_name} (not found or same name)")

print("✅ Renaming completed.")
