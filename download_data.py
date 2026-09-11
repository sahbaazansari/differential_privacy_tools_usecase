from pathlib import Path
from urllib.request import urlretrieve

url_file = 'https://raw.githubusercontent.com/opendifferentialprivacy/dp-test-datasets/master/data/PUMS_california_demographics/data.csv'
local_file = Path('PUMS_large.csv')

if local_file.exists():
	print(f'{local_file} already exists; skipping download.')
else:
	urlretrieve(url_file, local_file)
	print(f'Downloaded {local_file}.')