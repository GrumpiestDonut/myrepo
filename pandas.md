# Pandas for Python Notes:


### Install Pandas to Virtual Environment:

Open terminal and enter below inside line by line
```bash
$ python -m venv PATH$
$ source <venv>/bin/activate
$ pip install pandas
```

### To add Pandas to a project:

```python
import pandas as pd
```

### Create a basic DataFrame:

```python
# adding the columns and index allows you to specify those elements
df = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]], columns=["A","B","C"] , index=["x","y","z"])
```
### Basic Functions:

```python
df.columns # to see the columns
df.index.tolist() # to get the index ids df.index, to see them add the .tolist()
df.info() # to see details about your DataFrame
df.describe() # provides quick statistics about the series
df.unique() # display only unique items, to make it a specific column: df['A'].unique()
df.nuinque() # to find uninque numbers, to make it a specific column: df['A'].nunique()
df.shape # gives row and column counts of DataFrame. Example (3,3)
df.size # total number of items in the table
```

### View first few lines or last few lines of data:

```python
df.head() # top 3
df.head(5) # would set a specific amount of rows
df.tail() # bottom 3
```







