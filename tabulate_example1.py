import pandas as pd
from tabulate import tabulate
from collections import Counter

# Example of Counter
x = ['Alice', 'Joe', 'David', 'Bob', 'Bob', 'David','Alice', 'Bob']
y = Counter(x)
print("x = ", x)
print("Counter(x) = ",y)

# Example of tabulate
table_x = [['Alice', 24], ['Bob', 19]]
print("table_x = ", table_x)
print("Printing table_x using Tabulate =")
print(tabulate(table_x, headers=['Name', 'Age']))

# To Print counter using Tabulate
#   First convert the Counter into a proper table --> In this example converting to a Pandas table
#   Then use "tabluate" to format the output
df = pd.DataFrame.from_records(list(dict(y).items()), columns=['Name','Count'])
print("Printing a DataFrame using Tabulate =")
print(tabulate(df,headers=["index", "Name", "Count"], tablefmt="pretty"))