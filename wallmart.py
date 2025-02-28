import pandas as pd 
import matplotlib.pyplot as plt

data = pd.read_excel("C:\\Users\\Lenovo\\Desktop\\DA_Projects\\Projects\\Python_projects\\Wallmart_data_analysis\\Walmart.xlsx")
print(data.head(10))
print(data.info())

# Checking for NaN values
print(data.isna().sum())

# Removing any duplicate values
data.drop_duplicates(subset='Order ID', keep='first', inplace=True)

# Aggregated sales
aggregrated_sales = data.groupby('Category')['Sales'].sum().reset_index()
print(aggregrated_sales)

# Profit by State
aggregrated_profit = data.groupby('State')['Profit'].sum().reset_index()
print(aggregrated_profit)

# Top Customers
sales_by_customer = data.groupby('Customer Name')['Sales'].sum().reset_index()
print(sales_by_customer)

# Plotting graphs
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(14, 10))

# Sales by Category
axes[0, 0].bar(aggregrated_sales['Category'], aggregrated_sales['Sales'], color='blue')
axes[0, 0].set_title('Total Sales by Category')
axes[0, 0].set_xlabel('Category')
axes[0, 0].set_ylabel('Sales')
axes[0, 0].tick_params(axis='x', rotation=30)

# Card of best customer
best_customer = sales_by_customer.sort_values(by='Sales', ascending=False).head(1)

# Extract customer name and sales values
customer_name = best_customer['Customer Name'].values[0]
sales = best_customer['Sales'].values[0]

# Add the best customer card
#axes[0, 1].text(x=0.5, y=0.8, s=title.capitalize(), fontdict={'fontsize':35, 'color':'red', 'fontfamily': 'fantasy'}, horizontalalignment='center')
axes[0, 1].text(x=0.5, y=0.5, s=customer_name, fontdict={'fontsize':25, 'color':'blue', 'fontfamily': 'fantasy'}, horizontalalignment='center')
axes[0, 1].text(x=0.5, y=0.3, s=sales, fontdict={'fontsize':25, 'color':'green', 'fontfamily': 'fantasy'}, horizontalalignment='center')
axes[0, 1].set_title('Best Customer by Sales')
axes[0, 1].set_xticks([])
axes[0, 1].set_yticks([])

# Profit by State
axes[1, 0].barh(aggregrated_profit['State'], aggregrated_profit['Profit'], color='red')
axes[1, 0].set_title('Total Profit by State')
axes[1, 0].set_xlabel('State')
axes[1, 0].set_ylabel('Profit')
axes[1, 0].tick_params(axis='y', rotation=30)

# Sales Over Time
sales_over_time = data.groupby(data['Order Date'])['Sales'].sum()
axes[1, 1].plot(sales_over_time.index, sales_over_time.values)
axes[1, 1].set_title('Sales Over Time')
axes[1, 1].set_xlabel('Date')
axes[1, 1].set_ylabel('Sales')
axes[1, 1].tick_params(axis='x', rotation=30)
 
# Plotting the graphs
plt.tight_layout() 
plt.show()

