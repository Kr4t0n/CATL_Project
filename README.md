
# README #

## Version ##
**1.0**

## Requirements ##
scikit-learn
pydot

## Database Structure ##
Data Source 
***
 Barcode | Property 1 | Property 2 | ... | Result | Class
 ---- | ---- | ---- | ---- | ---- | ----
Decision Tree Result
***
Package | Tree | Index | Feature | Symbol | Threshold | Class
---- | ---- | ---- | ---- | ---- | ---- | ----

## Clustering Part ##

**Please run clustering.py to generate the ensemble clusters.**

The partial help document can be found in terminal.

```
Usage: clustering.py [options]

Options:
  -h, --help            show this help message and exit
  -s SERIAL_NUMBER, --serial_number=SERIAL_NUMBER
                        read data from db using serial_number
  -f FILENAME, --file=FILENAME
                        read data from FILENAME
  -S, --standard        standard the dataset
```

## Classifying Part ##
**Please run classifying.py to generate the result.**
The partial help document can be found in terminal.

```
Usage: classifying.py [options]

Options:
  -h, --help            show this help message and exit
  -t TABLE_NAME, --table=TABLE_NAME
                        read data from db using table_name
  -f FILENAME, --file=FILENAME
                        read data from FILENAME
  -S, --standard        standard the dataset
```

## License ##
MIT

## Support ##
If you are having issues getting this software to work, you can email <kyle.yang1995@gmail.com>

## Authors ##
Yang Zhengkai, Kyle


