import pickle
import codecs
import binascii

output_file = open("pw.bin", "wb")

print('Converting hUcitUm59Gdwu6y6fHLXEURR9AQ6jHsf')
data = "hUcitUm59Gdwu6y6fHLXEURR9AQ6jHsf".encode('utf-8')
enc = data.hex()
print('to ' + enc)
print('And writing it to a binary file')
 
pickle.dump(enc, output_file)
output_file.close()