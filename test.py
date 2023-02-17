import pandas as pd

# Read the CSV file into a DataFrame object
df = pd.read_csv('C:/Users/USER/Desktop/filename.csv')

# Print the first five rows of the DataFrame
print(df.head())

# Filter the DataFrame to include only rows where the 'column_name' column is greater than 5
filtered_df = df[df['column_name'] > 2]

# Print the filtered DataFrame
#print(filtered_df)

# Compute the mean of the 'column_name' column
#mean_value = df['column_name'].mean()

# Print the mean value
#print(mean_value)

# Save the filtered DataFrame to a new CSV file
#filtered_df.to_csv('C:/Users/USER/Desktop/new_filename.csv')