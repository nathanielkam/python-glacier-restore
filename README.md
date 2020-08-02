# python-glacier-restore
A simple Python Script / Tkinter GUI App using the boto3 SDK to Easily Restore Glacier Files to Amazon S3. All glacier restores are charged but this app only uses bulk and standard retrieval methods so you will not incur increased expedited credit charges. 

## Requirements:
No requirements needed to run the app from the dist folder, just double click and it will start. To run from python files, you will need python 3. To run the standlone executable binary just double click the one you need in dist. 

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
![Glacier Restore Example](https://nathanielkam.com/wp-content/uploads/2020/08/Example.png)
1. Enter your access key with no special characters or spaces
2. Enter your secret key with no special characters or spaces
3. Enter the bucket name with no special characters or spaces
4. Enter the folder name with **NO LEADING SLASH** but make sure it **ends with a SLASH** - see photo 
5. Enter the bucket region with no special characters or spaces see [AWS region codes!](https://docs.aws.amazon.com/general/latest/gr/rande.html)
6. Select which tier you want **bulk** or **standard** 
7. Wait a few minutees (program currently restores file by file) 
8. A success popup will trigger when restore request is complete (once the request is complete it will still take X hours to access your files based on the restore tier you selected). 

### Rebuilding Executable if you make changes
1. From the repo root (where main.py is)
2. MacOSX - sudo pyinstaller --onefile --add-binary='/System/Library/Frameworks/Tk.framework/Tk':'tk' --add-binary='/System/Library/Frameworks/Tcl.framework/Tcl':'tcl' main.py -n glacier-restore-to-s3 --windowed --noconfirm --clean
3. Windows - pyinstaller main.py -n  glacier-restore-to-s3 --windowed --noconfirm --clean
