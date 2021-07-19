import os
import dropbox 
from dropbox.files import WriteMode
class TransferData:
    def __init__(self,accesstoken):
        self.accesstoken=accesstoken
    def uploadfiles(self,filefrom,fileto):
        dbx=dropbox.Dropbox(self.accesstoken)
        for root,dirs,files in os.walk(filefrom):
            for filename in files:
                localpath=os.path.join(root,filename)
                relativepath=os.path.relpath(localpath,filefrom)
                dropboxpath=os.path.join(fileto,relativepath)
                with open(localpath,"rb")as f:
                    dbx.files_upload(f.read(),dropboxpath,mode=WriteMode("overwrite"))
def main():
    accesstoken="sl.A05i3_OJ2-vrtZUXLiBtHFCO9FwJrAwnqijdVaYuwVdHR8bxO-r0Q0IY4JzsPA1qRQMDC3u_zom9nErK8piFOWJFgS1CyPJvYhPDRDgxz7Sy6vlkbPIM1RW8KG_MKzihyUCb_xE"
    transferdata=TransferData(accesstoken)
    filefrom=str(input("Enter The Folder Path :"))
    fileto=input("Enter The Path To Upload To Dropbox")
    transferdata.uploadfiles(filefrom,fileto)
    print("File Has Been Moved")
main()