# importing the requests module
import requests

def Download(durl):
    print('Downloading started')
    #url = 'https://golang.org/dl/go1.17.3.windows-amd64.zip'
    print(durl)
    # Downloading the file by sending the request to the URL
    req = requests.get(durl)
     
    # Split URL to get the file name
    filename = durl.split('/')[-1]
    print(durl.split("/"))

    """
    # Writing the file to the local file system
    with open(filename,'wb') as output_file:
        output_file.write(req.content)
    print('Downloading Completed')
    """

url = "https://golang.org/dl/go1.17.3.windows-amd64.zip"

def DWLD(uuu):
    print(uuu.split("/")[-1])


DWLD(url)
