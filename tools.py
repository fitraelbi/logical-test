import argparse
import sys
import json

parser = argparse.ArgumentParser(
    description=f'example: python {sys.argv[0]} /var/log/error.log -t text')
parser.add_argument('file', help='position file',
                    metavar='file')
parser.add_argument('-t', help='output converter flag')
parser.add_argument('-o', help='save output file')
args = parser.parse_args()

if args.t:
    if args.o:
        if args.t == "json":
            errorLog = open(args.file, "r").read().splitlines()
            outputJson = []
            for items in errorLog:
                items = items.split(" ")
                outputJson.append({
                    'date': items[0],
                    'time': items[1],
                    'status': " ".join(items[2::])
                })
            with open(args.o, 'w') as f:
                f.write(str(json.dumps(outputJson)))
                f.close()
            print(f'file saved to {args.o} with type json')
        if args.t == "text":
            errorLog = open(args.file, "r").read()
            with open(args.o, 'w') as f:
                f.write(errorLog)
                f.close()
            print(f'file saved to {args.o} with type plaintext')
    else:
        if args.t == "json":
            errorLog = open(args.file, "r").read().splitlines()
            outputJson = []
            for items in errorLog:
                items = items.split(" ")
                outputJson.append({
                    'date': items[0],
                    'time': items[1],
                    'status': " ".join(items[2::])
                })
            print(json.dumps(outputJson))
        if args.t == "text":
            errorLog = open(args.file, "r").read()
            print(errorLog)
else:
    if args.o:
        errorLog = open(args.file, "r").read()
        with open(args.o, 'w') as f:
            f.write(errorLog)
            f.close()
        print(f'fle saved to {args.o} with type plaintext')
    else:
        errorLog = open(args.file, "r").read()
        print(errorLog)