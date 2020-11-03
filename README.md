# Download Data and convert it into either numpy array or pandas

## How to use ?

1. Download `data_handler.py`
1. Install numpy environment where you want to download the data
1. Import the class
```python
from data_handler import data_handler
```
1. Make an object
```python
dh = data_handler()
```
1. Download the data into a numpy array
```python
data = dh.download_to_np(folder_name = 'data')
```
1. Simply download the data into a folder
```python
dh.download(folder_name = 'data')
```
