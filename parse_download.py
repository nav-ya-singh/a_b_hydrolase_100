import argparse
import requests

parser = argparse.ArgumentParser()
parser.add_argument("filename", type=argparse.FileType('r'))
args = parser.parse_args()
lines_list = []
for line in args.filename:
    stripped_line = line.strip()
    lines_list.append(stripped_line)

print("start download")
for pdb_id in lines_list:
    url = "https://files.rcsb.org/download/" + pdb_id + ".cif.gz"
    r = requests.get(url)
    filename = url.split('/')[-1]
    with open(filename, 'wb') as cif_file:
        cif_file.write(r.content)
print('download complete')
