from utils import unzip_with_7z

zip_file_path = 'congrats.7z' # keep as is
dest_path = '.' # keep as is

find_me = '' # 2 letters are missing!
secret_password = find_me + 'bcmpda' 


def decod():
   for i in range(97,123):
      for j in range(97,123):
         global find_me
         global secret_password
         find_me=chr(i)+chr(j)
         secret_password=find_me+'bcmpda'
         if unzip_with_7z(zip_file_path,dest_path,secret_password):
           return ('File unzipped successfully')

print (decod())
