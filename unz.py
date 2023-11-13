import zipfile
with zipfile.ZipFile('qubot.zip', 'r') as zip_ref:
    zip_ref.extractall()

# Output:
# This will extract all files from 'file.zip'
