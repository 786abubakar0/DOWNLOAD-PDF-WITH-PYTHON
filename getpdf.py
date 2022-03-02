import requests
import sys

arguments = sys.argv[1:]
if(len(arguments)!=2):
    print("Invalid arguments!!")
    print("Correct command: python getpdf.py {Url of pdf} {Directory with name to save}")
    print('Example: python getpdf.py "http://www.africau.edu/images/default/sample.pdf" "C:/Users/Mohammad Abubakar/Desktop/pdf/sample.pdf"')
    sys.exit()
else:
    URL = arguments[0]
    LOCATION_TO_SAVE_FILE = arguments[1]
    try:
        pdf_content = requests.get(URL, stream=True).content
        pdf_name = URL.split("/")[-1]

        file = open(LOCATION_TO_SAVE_FILE, "wb")
        file.write(pdf_content)
        file.close()

        print("File is Created successfully!!")
        print("Check this directory: " + LOCATION_TO_SAVE_FILE)
    except Exception as e:
        print("Some error occurred!")