import pandas as pd   # Pandas library is used for Data Manipulation

data = {
    "id": [1, 2, 3],
    "name": ["Alice", "Bob", "Charlie"],
    "salary": [500, 600, 700]
}

df = pd.DataFrame(data)

# CREATE
new_employee = pd.DataFrame({
    "id": [4],
    "name": ["Gajodhar"],
    "salary": [5500]
})

df = pd.concat([df, new_employee], ignore_index=True)

# UPDATE
df.loc[df["name"] == "Bob", "salary"] = 6500

# READ
print("Data after Create & Update:")
print(df)

# DELETE (Delete employee with id = 3)
df = df[df["id"] != 3]

# Delete the 'name' column
df.drop("name", axis=1, inplace=True)

print("\nFinal DataFrame:")
print(df)
