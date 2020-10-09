#!/usr/bin/env python3
from datetime import date
from glob import glob
from argparse import ArgumentParser
try:
    import yamale
    from yamale.yamale_error import YamaleError
except ImportError:
    print("You have to install yamale.\npip install -r requirements.txt")
    exit(-1)

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("filename", type=str, help="Filename/Glob of rules to test against the schema.")
    parser.add_argument("--schema", "-s", type=str, default="schema.yml", help="Schema to use. (Default=schema.yml)")
    args = parser.parse_args()
    schema = yamale.make_schema(args.schema)
    filelist = glob(args.filename)
    for file in filelist:
        data = yamale.make_data(file)
        try:
            yamale.validate(schema, data)
            print(f"✔️  - {file}")
        except YamaleError as ye:
            print(f"❌ - {file}")
            print(ye)
