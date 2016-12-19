import argparse
from datetime import date

parser = argparse.ArgumentParser(description='Add a date to a journal entry.')
parser.add_argument('journal', type=str, help='Journal file to evaluate.')
args = parser.parse_args()

with open(args.journal, 'ab+') as f:
    k = b''
    while k != b'#':
        f.seek(-2, 1)
        k = f.read(1)
    last_date = f.readline().decode("utf-8").strip()
    today = date.today().strftime("%m/%d/%Y")

    if today != last_date:
        date_line = '\n# {today}\n\n'.format(today=today)
        f.write(str.encode(date_line))

