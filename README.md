# Shift Record Automation

The scenario in that project is the tally that is holding records of officers' shift entrances and these names of officers are 
stored in digital as a list that seperated by commas. The watch commander, who is responsible about update shift scores, must do 
it manuelly. 

That automation console program takes officer name or a list of names as input and assigns them a 1-point increase score in the 
related Google Sheet. . 

![alt text](https://cdn.discordapp.com/attachments/1096569339886456883/1167486413583953980/Adsz.png)

## Getting Started

You can follow the steps below to run and develop the project on your local machine.

### Gereksinimler

You will need the following software and tools for the project:

- Python 3.8 or newer
- Git (Optional. You can download the project as RAR)

### Insallation By Git

Clone the project directory to your local machine and install the dependencies.

1. Clone the project directory:
```shell
git clone https://github.com/Cagala/Shift-SheetPY.git
```
2. Navigate to the Project directory:
```shell
cd Shift-SheetPY
```
3. Configure project settings ("If you use a Sheet template like in this project, you can configure it here):

- You must use your creds.json that related with your Sheet. [Here how to create credentials](https://pygsheets.readthedocs.io/en/stable/authorization.html)

- You should delete path config in config.ini. Otherwise program will occur at the first initilazition.



## Usage
You can use the project by following these steps:

#### Windows
If your python version is 3.11.3, you can use the program by .bat file.

If your python version is newer or older, you can put your python.exe file to Assets folder
and change the older one.

**But**: The included python.exe could be invisible. You should make sure your folder options shows
invisible folders.

#### Without .bat
1.Open the console and navigate to the project's root directory (system/).
2.Start the console application by using the following command:
```shell
python sheet.py
```
If doesn't work, try that:
```shell
python3 sheet.py
```
3.Use the console application menu to add worker information, increase their scores, or list them.
