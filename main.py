import csv
import argparse

ap=argparse.ArgumentParser()

ap.add_argument('-r', help='file path of the reading file')
ap.add_argument('-w', help='file path of file that is being written or created')

args, unknown=ap.parse_known_args()

# Opens and closes file with encoding 'utf-8' to decode all characters in file

if args.r is not None and args.w is not None:
    f = open(args.w, "w")
    with open(args.r, mode='r', encoding='utf-8')as file:
        csvReader=csv.reader(file, delimiter=",")
        for row in csvReader:
            # row[6] is the User Group column
            if row[6]=='Students':
                # row[0] is the Email column
                f.write(row[0]+'\n')
                print(row[0])
    f.close()
else:
    ap.print_help()