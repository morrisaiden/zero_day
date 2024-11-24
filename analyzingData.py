import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Task 1: Load and Explore the Dataset
try:
    # Load the dataset
    data = pd.read_csv('iris.csv')  # Replace 'iris.csv' with your dataset's filename
    
    # Display the first few rows
    print("First few rows of the dataset:")
    print(data.head())
    
    # Explore the structure of the dataset
    print("\nDataset Info:")
    print(data.info())
    
    # Check for missing values
    print("\nMissing Values:")
    print(data.isnull().sum())
    
    # Clean the dataset (dropping rows with missing values)
    data_cleaned = data.dropna()
    print("\nDataset after cleaning (missing values dropped):")
    print(data_cleaned.info())
    
except FileNotFoundError:
    print("Error: Dataset file not found. Please ensure the file is in the working directory.")
    exit()

# Task 2: Basic Data Analysis
# Compute basic statistics
print("\nBasic Statistics:")
print(data_cleaned.describe())

# Grouping data (example: grouping by 'species' and computing the mean of 'sepal length (cm)')
if 'species' in data_cleaned.columns and 'sepal length (cm)' in data_cleaned.columns:
    group_mean = data_cleaned.groupby('species')['sepal length (cm)'].mean()
    print("\nMean Sepal Length by Species:")
    print(group_mean)

# Identifying interesting patterns
print("\nInteresting Patterns:")
if 'species' in data_cleaned.columns:
    species_counts = data_cleaned['species'].value_counts()
    print(f"Number of instances per species:\n{species_counts}")

# Task 3: Data Visualization
# Line Chart (example: trends over time; replace column names if necessary)
plt.figure(figsize=(8, 5))
plt.plot(data_cleaned.index, data_cleaned['sepal length (cm)'], label='Sepal Length')
plt.title('Sepal Length Trends')
plt.xlabel('Index')
plt.ylabel('Sepal Length (cm)')
plt.legend()
plt.grid()
plt.show()

# Bar Chart (comparison of average petal length by species)
if 'species' in data_cleaned.columns and 'petal length (cm)' in data_cleaned.columns:
    plt.figure(figsize=(8, 5))
    sns.barplot(x=group_mean.index, y=group_mean.values)
    plt.title('Average Sepal Length by Species')
    plt.xlabel('Species')
    plt.ylabel('Average Sepal Length (cm)')
    plt.show()

# Histogram (distribution of petal length)
plt.figure(figsize=(8, 5))
plt.hist(data_cleaned['petal length (cm)'], bins=10, color='blue', edgecolor='black')
plt.title('Distribution of Petal Length')
plt.xlabel('Petal Length (cm)')
plt.ylabel('Frequency')
plt.show()

# Scatter Plot (relationship between sepal length and petal length)
plt.figure(figsize=(8, 5))
plt.scatter(data_cleaned['sepal length (cm)'], data_cleaned['petal length (cm)'], c='green', alpha=0.5)
plt.title('Sepal Length vs Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.grid()
plt.show()

# Findings or Observations
print("\nFindings:")
print("- The dataset contains information about iris flower species and their measurements.")
print("- The cleaned dataset has no missing values.")
print("- Different species have distinct average sepal lengths, as shown in the bar chart.")
print("- The scatter plot shows a positive correlation between sepal length and petal length.")
