
from Load_Data import load_data
import pandas as pd
# Load the data using the reusable function
data = load_data()

# visualization of the distribution
import matplotlib.pyplot as plt
numeric_cols = ['Age', 'Purchase Amount (USD)','Review Rating', 'Previous Purchases']
plt.figure(figsize=(15,20))

for i, col in enumerate(numeric_cols, 1):
    plt.subplot(5, 2, i)
    plt.hist(data[col], bins=20, edgecolor='k', alpha=0.7)
    plt.title(f'Distribution of {col}')
    plt.xlabel(col)
    plt.ylabel('Frequency')

plt.tight_layout()
plt.show()

## Age Based Analysis

# create age group
bins = [18, 30, 40, 50, 60, 70, 80, 90, 101]
labels = ['18-29', '30-39', '40-49', '50-59', '60-69', '70-79', '80-89', '90-100']
data['AgeGroup'] = pd.cut(data['Age'], bins=bins, labels=labels, right=False)

# Sorting the age group
df = data.sort_values(by='AgeGroup', ascending=True)
df.head()

# Spending as per age group

total_spending_by_age = df.groupby('AgeGroup', observed=True)['Purchase Amount (USD)'].sum().reset_index()
total_spending_by_age.columns = ['AgeGroup', 'Total_Spending']
total_spending_by_age

# Average review rating by age group
Age_review = df.groupby('AgeGroup', observed=True)['Review Rating'].mean().reset_index()
print(Age_review)

##Gender Based Analysis

# gender based spending

gender_based = data.groupby('Gender')['Purchase Amount (USD)'].sum().reset_index(name='Total_Sales')
gender_based


#How much did each gender spend in each category
gender_based = data.groupby(['Gender', 'Category'])['Purchase Amount (USD)'].sum().reset_index(name='Total_Sales')
gender_based

# checking Male purchasing behavior

# Filter for males
male_df = data[data['Gender'] == 'Male']

# Group by category and sum purchase amounts
male_category_spending = (
    male_df.groupby('Category')['Purchase Amount (USD)'] .sum().reset_index().sort_values(by='Purchase Amount (USD)', ascending=False)
)

print(male_category_spending)


# for female spending
# Filter for female
female_df = data[data['Gender'] == 'Female']

# Group by category and sum purchase amounts
female_category_spending = (
    female_df.groupby('Category')['Purchase Amount (USD)'] .sum().reset_index().sort_values(by='Purchase Amount (USD)', ascending=False)
)

print(female_category_spending)

## Customer Based Analysis
# Total spending per customer.
spending_per_customer = data.groupby('Customer ID')['Purchase Amount (USD)'].sum().reset_index()
spending_per_customer.head(10)

# identify high-value vs low-value customer

#  Calculate total spending per customer
data['Total_Spent'] = data['Purchase Amount (USD)']  
customer_spending = data.groupby('Customer ID')['Total_Spent'].sum().reset_index()

#  Define a threshold to split high vs low value
threshold = customer_spending['Total_Spent'].median()  

#  Label customers
customer_spending['Customer_Value'] = customer_spending['Total_Spent'].apply(
    lambda x: 'High-Value' if x >= threshold else 'Low-Value'
)

print(customer_spending.head(10))


# Average purchase amount per category.

Average_purchase = data.groupby('Category')['Purchase Amount (USD)'].mean().reset_index()
Average_purchase

#Frequency of purchases (number of  customers purchases per month).


# Filter for Monthly purchasers
monthly_df = data[data['Frequency of Purchases'] == 'Weekly']

# Count number of 'Previous Purchases' records in that monthly group
num_of_purchase_per_month = monthly_df['Previous Purchases'].count()

print("Number of customers who purchase monthly:", num_of_purchase_per_month)


