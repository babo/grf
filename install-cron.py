#!/usr/bin/env python3
import subprocess
import sys
import tempfile
import re

def main():
    if len(sys.argv) == 1:
        print('You need to add a command line argument')
        sys.exit(1)

    pattern = re.compile(r'^(.*)(\$\(.+?\))(.*)$')
    with tempfile.NamedTemporaryFile(delete=False) as cronfile:
        filename = cronfile.name
        with open(sys.argv[1]) as fd:
            for line in fd.readlines():
                line = line.strip()
                while True:
                    m = pattern.match(line)
                    if not m:
                        break
                    cmd = m.group(2)[2:-1]
                    res = subprocess.run(cmd, shell=True, capture_output=True)
                    outp = res.stdout.decode('UTF-8').strip()
                    line = ''.join([m.group(1), outp, m.group(3)])
                cronfile.write(line.encode('UTF-8'))
                cronfile.write(b'\n')
    what = f"crontab {filename} && rm -f {filename}"
    subprocess.run(what, shell=True)

if __name__ == '__main__':
    main()
