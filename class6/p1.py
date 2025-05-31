from google.colab import drive
drive.mount('/content/drive')

# Once the drive is mounted, you can access files like this:
file_path = '/content/drive/My Drive/New CV.docx'  # Replace with the actual path to your file

# Open the file in read binary mode ('rb') to handle binary data
with open(file_path, 'rb') as file:  # Change 'r' to 'rb'
    content = file.read()

!pip install python-docx
import docx

doc = docx.Document(file_path)
full_text = []
for para in doc.paragraphs:
    full_text.append(para.text)
print('\n'.join(full_text))

