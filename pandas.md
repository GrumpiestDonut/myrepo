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

### create a basic DataFrame:

```python
df = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]], columns=["A","B","C")
```

### view first few lines or last few lines of data:

```python
df.head() # top 3

df.tail() # bottom 3
```
