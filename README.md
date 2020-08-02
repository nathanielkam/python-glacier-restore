# python-glacier-restore
A simple Python Script / Tkinter GUI App using the boto3 SDK to Easily Restore Glacier Files to Amazon S3. All glacier restores are charged but this app only uses bulk and standard retrieval methods so you will not incur increased expedited credit charges. 

## Requirements:
To run from python files, you will need python 3. To run the standlone executable binary just double click the one you need in dist. 

### Instructions to Run the Binary Executable (recommended):
1. Go to the dist folder
2. If you are on windows run the .exe version
3. If you are on mac run the app version

### Instructions to Run the Code:

1. Create a virtual enviornment to install libraries related to **venv**
    - Run `python -m venv venv`
    - Linux / MacOSX: Run `source venv/bin/activate`
    - Windows: Run `venv\env\Scripts\activate.bat`
2. Run `pip install -r requirements.txt`
3. Run `python main.py` 

### How to use this app to restore Glacier Files to S3
![Example Image Placeholder](https://octodex.github.com/images/yaktocat.png)
1. Enter your access key in the form of 
2. Enter your secret key in the form of 
3. Enter the bucket name in the form of 
4. Enter the folder name in the form of 
5. Enter the bucket region in the form of 
6. Select which tier you want bulk or standard 
7. Wait a few minutees (program currently restores file by file) 
8. A success popup will trigger when restore request is complete (once the request is complete it will still take X hours to access your files based on the restore tier you selected). 
