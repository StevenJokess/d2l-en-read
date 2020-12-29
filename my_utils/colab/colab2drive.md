

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-19 21:09:55
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-29 18:25:10
 * @Description:
 * @TODO::
 * @Reference:https://colab.research.google.com/github/omerbsezer/Fast-Pytorch/blob/master/Learning_Pytorch/TransferLearning.ipynb#scrollTo=jRd8Dg2hQ541
-->
!apt-get install -y -qq software-properties-common python-software-properties module-init-tools
!add-apt-repository -y ppa:alessandro-strada/ppa 2>&1 > /dev/null
!apt-get update -qq 2>&1 > /dev/null
!apt-get -y install -qq google-drive-ocamlfuse fuse
from google.colab import auth
auth.authenticate_user()
from oauth2client.client import GoogleCredentials
creds = GoogleCredentials.get_application_default()
import getpass
!google-drive-ocamlfuse -headless -id={creds.client_id} -secret={creds.client_secret} < /dev/null 2>&1 | grep URL
vcode = getpass.getpass()
!echo {vcode} | google-drive-ocamlfuse -headless -id={creds.client_id} -secret={creds.client_secret}


!mkdir -p drive
!google-drive-ocamlfuse drive
import sys
sys.path.insert(0,'drive/Fast-Pytorch/Learning_Pytorch')
!ls drive


%cd 'drive/'
!ls
!git clone https://github.com/omerbsezer/Fast-Pytorch.git

---

import shutil

shutil.rmtree('/content/Fast-Pytorch', ignore_errors=True)

---

https://colab.research.google.com/drive/1zbt2A74kM10HvcAEgEy3fGgRSNyHZQKj?usp=sharing#scrollTo=RBkP5aBdfFkd

import os
from google_drive_downloader import GoogleDriveDownloader as gdd

# Need to download the Omniglot dataset -- DON'T MODIFY THIS CELL
if not os.path.isdir('./omniglot_resized'):
    gdd.download_file_from_google_drive(file_id='1iaSFXIYC3AB8q9K_M-oVMa4pmB7yKMtI',
                                        dest_path='./omniglot_resized.zip',
                                        unzip=True)

assert os.path.isdir('./omniglot_resized')
