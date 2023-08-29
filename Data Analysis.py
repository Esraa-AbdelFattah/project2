# importing pandas module
import pandas as pd

# Define a dictionary containing employee data
data1 = {'Name': ['Ahmed', 'Mohamed', 'Ali', 'Mahmoud',
                  'Ali', 'Mahmoud', 'Mohamed', 'Ahmed'],
         'Age': [27, 24, 22, 32,
                 33, 36, 27, 32],
         'Address': ['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj',
                     'Jaunpur', 'Kanpur', 'Allahabad', 'Aligarh'],
         'Qualification': ['Msc', 'MA', 'MCA', 'Phd',
                           'B.Tech', 'B.com', 'Msc', 'MA']}

# Convert the dictionary into DataFrame
df = pd.DataFrame(data1)

print("Original Dataframe")
display(df)

# applying groupby() function to
# group the data on Name value.
gk = df.groupby('Name')

# Let's print the first entries
# in all the groups formed.
print("After Creating Groups")
gk.first()