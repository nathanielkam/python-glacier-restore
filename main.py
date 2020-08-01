from tkinter import *
from tkinter import messagebox
import boto3
import webbrowser

# Initialize
fields = ('AWS Access Key', 'AWS Secret Key','S3 Bucket', 'Folder to Restore (Format: folder1/folder2/)', 'Bucket Region (Example: us-east-1)',)
s3_client = ''

# Enable Hyperlinking
def hyperlink(url):
    webbrowser.open_new(url)

# Create an S3 Client Session
def create_client(entries):
   client = boto3.client(
      's3', 
      aws_access_key_id=entries['AWS Access Key'].get(), 
      aws_secret_access_key=entries['AWS Secret Key'].get(),
      region_name=entries['Bucket Region (Example: us-east-1)'].get()
   )
   return client

# Can User List files and Glacier Restore Them
def validate_access(entries):
   # If Failure
   messagebox.showerror("Access Forbidden", "You do not have access to restore those files.")

def restore_glacier_contents(entries, type):

   client = create_client(entries)    

   # bucket = entries['AWS Secret Key'].get()
   bucket = entries['S3 Bucket'].get()
   prefix = entries['Folder to Restore (Format: folder1/folder2/)'].get()
   # prefix = entries['Folder to Restore (Format: folder1/folder2/'].get()

   # Try to get S3 list
   try:
      s3_result = client.list_objects_v2(
         Bucket=bucket,
         Prefix=prefix
      )
   except:
      messagebox.showerror("Error", "You are unable to list these files.")
      exit()

   if 'Contents' not in s3_result:
      return []

   file_list = []

   restore_request = {
      'OutputLocation': {
         'S3': {
               'BucketName': 'destination-bucket',
               'Prefix': 'destination-prefix',
         }
      }
   }

   # Get list of Contents
   for file in s3_result['Contents']:
      # Only Log Glacier Files
      if file['StorageClass'] == 'GLACIER':
         response = client.restore_object(Bucket=bucket, Key=file['Key'],RestoreRequest={'Days': 14,'Tier': type})
         file_list.append(file['Key'])

   # Get list of Contents when More than 1000 Items
   while s3_result['IsTruncated']:
      continuation_key = s3_result['NextContinuationToken']
      s3_result = s3_conn.list_objects_v2(Bucket=bucket, Prefix=prefix, Delimiter="/", ContinuationToken=continuation_key)
      for file in s3_result['Contents']:
            # Only Log Glacier Files
         if file['StorageClass'] == 'GLACIER':
            response = client.restore_object(Bucket=bucket, Key=file['Key'],RestoreRequest={'Days': 14,'Tier': type})
            file_list.append(file['Key'])

   # Return File List
   return file_list

def glacier_restore(entries, type):

   if type=="Bulk":
      files = restore_glacier_contents(entries, type)
      #print(files)
      # If Bulk Success
      messagebox.showinfo("Bulk Request Success!", "Bulk Restore Request Successful! Your files will be restored in 5-12 hours.")

   elif type=="Standard":
      files = restore_glacier_contents(entries, type)
      #print(files)
      # If Standard Success
      messagebox.showinfo("Standard Request Success!", "Standard Restore Request Successful! Your files will be restored in 3-5 hours.")

   else:
      # If Failure
      messagebox.showerror("Error", "There was an issue requesting restore of files, please contact your S3 administrator.")

def makeform(root, fields):
       
   # Initialize Entries
   entries = {}
   
   for field in fields:
      row = Frame(root)

      # Add Field Title
      lab = Label(row, width=50, text=field+": ", anchor='w')

      # Add Field Entry
      if field=="AWS Secret Key":
         # AWS Secret Key is sensitive data and should be obscured
         ent = Entry(row, width=61, show="*")

      else:  
         ent = Entry(row, width=61)

      # Add Styling
      row.pack(side = TOP, fill = X, padx = 5 , pady = 5)
      lab.pack(side = LEFT)
      ent.pack(side = LEFT, expand = YES, fill = X)
      
      # Save to Entries
      entries[field] = ent
   return entries

if __name__ == '__main__':
       
   # Init TK
   root = Tk()

   # Init the Form
   ents = makeform(root, fields)

   # Set Window Title
   root.title("AWS Glacier Restore to S3")

   # Add Quit Button
   b3 = Button(root, text = 'Quit', command = root.quit)
   b3.pack(side = RIGHT, padx = 5, pady = 5)

   # Add Bulk Retrieval Button
   b1 = Button(root, text = 'Bulk Retrieval (5-12 Hours)',
   command=(lambda e = ents: glacier_restore(e, "Bulk")))
   b1.pack(side = RIGHT, padx = 5, pady = 5)

   # Add Standard Retrieval Button
   b2 = Button(root, text='Standard Retrieval (3-5 Hours)',
   command=(lambda e = ents: glacier_restore(e, "Standard")))
   b2.pack(side = RIGHT, padx = 5, pady = 5)

   # Add Hyperlink to AWS Region Documentation
   link1 = Label(root, text="Documentation: AWS Region Codes", fg="blue", cursor="hand2")
   link1.pack(side = LEFT, fill = X, padx = 5 , pady = 5)
   link1.bind("<Button-1>", lambda e: hyperlink("https://docs.aws.amazon.com/general/latest/gr/rande.html"))

   # Run
   root.mainloop()