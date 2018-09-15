# WebScraping
Provide an example on the 'how to' scrap a web site... to generate your own reports and alerts.
Default configuration is for:
* alerting
* files record
Output options are:
* CSV files:
  * one file by name
  * one global file
* Graph with realtime refresh on:
  * Prices
  * Volumes

Up to you to adapt to your need and fork it ;-)

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

## Execution
Short and with the default parameters

`python program.py`

## Parameters: 
[classes/standard.py](classes/standard.py)

* -h // --help 
*       --debug 
* -d / --dir= <output dir> / define the output folder
* -f / --file= <filename> / define the files suffix
* -t / --timer= <loop timer> / define the collector loop timer
* -l / --limit= <row limit> / define the limit to use during the market collection
* -n / --collect_name= <name> / define the name for this collection
* -u / --collect_url= <url to collect> / define the url to reach to collect the info
* -G / -- / graph the collection
* -A / -- / display the alert (values of variation)
* -D / -- / graph the alert
* -R / -- / display the report info
* -P / -- / display the scraping info
* -M / -- / display the market info
* -F / -- / display the file info
* -S / -- / save the scraping output in file  (compilation, one CSV file by collected entry)
* -O / -- / CSV files loader (history)
              
Using the indexes for the parameters

`python program.py -t 60 -l 10 -s timeserial_file.csv -r realtime_file.csv`

Long name as parameters

`python program.py --timer=60 --limit=10 --order=Prix --sfile=timeserial_file.csv --rfile=realtime_file.csv`

## Output files
The generates files are stored by default in:

`./reports` 

### Timeserial
Provide a file this increase with each collect

`./reports/{market}_timeserial_report.csv`

*{market}* is the collected name for the considered sequence

### Realtime
Provide a file with all collected data 

`./reports/Global-realtime_report.csv`

## Python version
Validated on the following Python versions:
* Python 2.7.13
* Python 3.6.5

## Windows users
1/ From Windows Explorer

a) python installation
- download the python binary version for Windows (python 2.7 or 3.6, 32 or 64 b) (preference for python3.6 64b)
- install the python binary version (double click on the installer downloaded previously)

b) app settings  
- download the archive from git (https://github.com/guillain/WebScraping)
- unarchive the zip file
- go in the folder created by the unarchiving execution

2/ From Windows Command line (the standard one coming from the OS)

a) move in the downloaded folder

`cd c:\Users\guillain\Desktop` 

b) package dependencies installation
- install the necessary package (you're still in the unarchived folder):

`pip install -r requirements.txt`

c) app execution
- run the python scrypt with the python command

`python program.py`

d) stop the execution
- press Ctrl + C


## Traces
```
C:\WINDOWS\system32>cd c:\Users\guillain\Desktop

c:\Users\guillain\Desktop>git clone https://github.com/guillain/WebScraping.git
Cloning into 'WebScraping'...
remote: Counting objects: 16, done.
remote: Compressing objects: 100% (12/12), done.
remote: Total 16 (delta 5), reused 11 (delta 3), pack-reused 0
Unpacking objects: 100% (16/16), done.

c:\Users\guillain\Desktop>cd WebScraping

c:\Users\guillain\Desktop\WebScraping>pip3 install -r requirements.txt
Collecting bs4 (from -r requirements.txt (line 1))
  Using cached https://files.pythonhosted.org/packages/10/ed/7e8b97591f6f456174139ec089c769f89a94a1a4025fe967691de971f314/bs4-0.0.1.tar.gz
Requirement already satisfied: requests in c:\program files\python36\lib\site-packages (from -r requirements.txt (line 2)) (2.18.4)
Collecting matplotlib (from -r requirements.txt (line 3))
  Using cached https://files.pythonhosted.org/packages/bf/b9/485032835e979ee11d514bb3b9b0543a928b8b96c099c178aeab1d2ba861/matplotlib-2.2.2-cp36-cp36m-win_amd64.whl
Requirement already satisfied: numpy in c:\program files\python36\lib\site-packages (from -r requirements.txt (line 4)) (1.13.1)
Requirement already satisfied: beautifulsoup4 in c:\program files\python36\lib\site-packages (from bs4->-r requirements.txt (line 1)) (4.6.0)
Requirement already satisfied: idna<2.7,>=2.5 in c:\program files\python36\lib\site-packages (from requests->-r requirements.txt (line 2)) (2.6)
Requirement already satisfied: chardet<3.1.0,>=3.0.2 in c:\program files\python36\lib\site-packages (from requests->-r requirements.txt (line 2)) (3.0.4)
Requirement already satisfied: urllib3<1.23,>=1.21.1 in c:\program files\python36\lib\site-packages (from requests->-r requirements.txt (line 2)) (1.22)
Requirement already satisfied: certifi>=2017.4.17 in c:\program files\python36\lib\site-packages (from requests->-r requirements.txt (line 2)) (2018.1.18)
Requirement already satisfied: six>=1.10 in c:\users\guillain\appdata\roaming\python\python36\site-packages (from matplotlib->-r requirements.txt (line 3)) (1.11.0)
Requirement already satisfied: pytz in c:\program files\python36\lib\site-packages (from matplotlib->-r requirements.txt (line 3)) (2017.2)
Collecting kiwisolver>=1.0.1 (from matplotlib->-r requirements.txt (line 3))
  Using cached https://files.pythonhosted.org/packages/44/72/16630c3392eba03788ad87949390516bbc488e8e118047a3b824631d21a6/kiwisolver-1.0.1-cp36-none-win_amd64.whl
Collecting cycler>=0.10 (from matplotlib->-r requirements.txt (line 3))
  Using cached https://files.pythonhosted.org/packages/f7/d2/e07d3ebb2bd7af696440ce7e754c59dd546ffe1bbe732c8ab68b9c834e61/cycler-0.10.0-py2.py3-none-any.whl
Collecting pyparsing!=2.0.4,!=2.1.2,!=2.1.6,>=2.0.1 (from matplotlib->-r requirements.txt (line 3))
  Using cached https://files.pythonhosted.org/packages/6a/8a/718fd7d3458f9fab8e67186b00abdd345b639976bc7fb3ae722e1b026a50/pyparsing-2.2.0-py2.py3-none-any.whl
Requirement already satisfied: python-dateutil>=2.1 in c:\program files\python36\lib\site-packages (from matplotlib->-r requirements.txt (line 3)) (2.6.1)
Requirement already satisfied: setuptools in c:\program files\python36\lib\site-packages (from kiwisolver>=1.0.1->matplotlib->-r requirements.txt (line 3)) (39.0.1)
Installing collected packages: bs4, kiwisolver, cycler, pyparsing, matplotlib
  Running setup.py install for bs4 ... done
Successfully installed bs4-0.0.1 cycler-0.10.0 kiwisolver-1.0.1 matplotlib-2.2.2 pyparsing-2.2.0

c:\Users\guillain\Desktop\WebScraping>python3 program.py
-----------------------------------
            coinmarketcap APP
-----------------------------------

2018-06-09 20:35:29      BTCBitcoin      BTC     129911709615    7604.13         3841430000
2018-06-09 20:35:29      ETHEthereum     ETH     60170519168     601.88          1526200000
2018-06-09 20:35:29      XRPRipple       XRP     26113479561     0.665408        180638000
2018-06-09 20:35:29      BCHBitcoin Cash         BCH     19060423244     1109.82         411555000
2018-06-09 20:35:29      EOSEOS          EOS     12756419176     14.23   1179130000
2018-06-09 20:35:29      LTCLitecoin     LTC     6765336630      118.88          243424000
2018-06-09 20:35:29      XLMStellar      XLM     5281080960      0.283879        46140400
2018-06-09 20:35:29      ADACardano      ADA     5278829343      0.203603        51252400
2018-06-09 20:35:29      MIOTAIOTA       MIOTA   4626639337      1.66    68522600
2018-06-09 20:35:29      TRXTRON         TRX     3786078710      0.057585        170011000
2018-06-09 20:35:29      NEONEO          NEO     3381683500      52.03   72378000
2018-06-09 20:35:45      BTCBitcoin      BTC     129911709615    7604.13         3841430000
2018-06-09 20:35:45      ETHEthereum     ETH     60170519168     601.88          1526200000
2018-06-09 20:35:45      XRPRipple       XRP     26113479561     0.665408        180638000
2018-06-09 20:35:45      BCHBitcoin Cash         BCH     19060423244     1109.82         411555000
2018-06-09 20:35:45      EOSEOS          EOS     12756419176     14.23   1179130000
2018-06-09 20:35:45      LTCLitecoin     LTC     6765336630      118.88          243424000
2018-06-09 20:35:45      XLMStellar      XLM     5281080960      0.283879        46140400
2018-06-09 20:35:45      ADACardano      ADA     5278829343      0.203603        51252400
2018-06-09 20:35:45      MIOTAIOTA       MIOTA   4626639337      1.66    68522600
2018-06-09 20:35:45      TRXTRON         TRX     3786078710      0.057585        170011000
2018-06-09 20:35:45      NEONEO          NEO     3381683500      52.03   72378000
Manual break by user

c:\Users\guillain\Desktop\WebScraping>dir reports
 Volume in drive C is Windows

 Directory of c:\Users\guillain\Desktop\WebScraping\reports

09/06/2018  20:35    <DIR>          .
09/06/2018  20:35    <DIR>          ..
09/06/2018  20:35               122 ADACardano-timeserial_report.csv
09/06/2018  20:35               124 BCHBitcoin Cash-timeserial_report.csv
09/06/2018  20:35               128 BTCBitcoin-timeserial_report.csv
09/06/2018  20:35               122 EOSEOS-timeserial_report.csv
09/06/2018  20:35               124 ETHEthereum-timeserial_report.csv
09/06/2018  20:35               120 LTCLitecoin-timeserial_report.csv
09/06/2018  20:35               118 MIOTAIOTA-timeserial_report.csv
09/06/2018  20:35               116 NEONEO-timeserial_report.csv
09/06/2018  20:35               491 realtime_report.csv
09/06/2018  20:35               124 TRXTRON-timeserial_report.csv
09/06/2018  20:35               122 XLMStellar-timeserial_report.csv
09/06/2018  20:35               126 XRPRipple-timeserial_report.csv
              12 File(s)          1 837 bytes
               2 Dir(s)  66 778 128 384 bytes free

c:\Users\guillain\Desktop\WebScraping>
```