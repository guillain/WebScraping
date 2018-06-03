# WebScraping
Provide an example on the 'how to' scrap a web site... financial to generate my own report 

# Fast track
```
git clone
cd WebScraping
git install -r requirements.txt
python3 program.py
```

# Install
Download from git
`git clone`

Move into the folder
`cd WebScraping`

Install requirements
`git install -r requirements.txt`

# Excution
Short and with the default parameters
`python3 program.py`

# Parameters
* -t / --timer: loop frequency, default 5s
* -l / --limit: number of row collected, default 10
* -s / --sfile : output file for the timeserial record
* -r / --rfile : output file for the realtime record

Using the indexes for the parameters
`python3 program.py -t 60 -l 10 -s timeserial_file.csv -r realtime_file.csv`

Long name as parameters
python3 program.py --timer=60 --limit=10 --sfile=timeserial_file.csv --rfile=realtime_file.csv

# Output file
## Timeserial
Provide a file this increase with each collect

## Realtime
Provide a file with only the last collected data into

# Python version
Validated on the following Python version:
* Python 2.7
* Python 3.6

