# WebScraping
Provide an example on the 'how to' scrap a web site... financial to generate my own report 

## Fast track
```
git clone https://github.com/guillain/WebScraping
cd WebScraping
pip install -r requirements.txt
python program.py
```

## Install
Download from git
`git clone https://github.com/guillain/WebScraping`

Move in the folder
`cd WebScraping`

Install requirements
`pip install -r requirements.txt`

## Excution
Short and with the default parameters
`python program.py`

## Parameters
* -t / --timer: loop frequency, default 5s
* -l / --limit: number of row collected, default 10
* -s / --sfile : output file for the timeserial record
* -r / --rfile : output file for the realtime record

Using the indexes for the parameters
`python program.py -t 60 -l 10 -s timeserial_file.csv -r realtime_file.csv`

Long name as parameters
python program.py --timer=60 --limit=10 --sfile=timeserial_file.csv --rfile=realtime_file.csv

## Output files
The generates files are stored by default in:
`./reports` 
`
### Timeserial
Provide a file this increase with each collect
`./reports/{market}_timeserial_report.csv`
*{market}* is the collected name for the considered sequence

### Realtime
Provide a file with only the last collected data into
`./reports/realtime_report.csv`

## Python version
Validated on the following Python version:
* Python 2.7
* Python 3.6

## Windows users
1/ From Windows Explorer

  a) python installation
	- download the python binary version for Windows (32 or 64 b)
	- install the python binary version (double click on the installer downloaded previously)

  b) app settings
	- download the archive from git (https://github.com/guillain/WebScraping
	- unarchive the zip file
	- go in the folder created by the unarchiving execution

2/ From Windows Command line (the standard one coming from the OS)

  a) package dependencies installation
	- install the necessary package (you're still in the unarchived folder):
	  $ pip install -r requirements.txt
	  
  b) app execution
	- run the python scrypt with the python command
	  $ python program.py
	 