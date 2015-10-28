from commander import run, run_group

def parse(line):
    results = map(lambda l: l.split(','),line.split(';'))
    return results

def parse_file(f):
    r = []
    for line in f.readlines():
        parsed = parse(line)
        r.append(run_group(parsed[0],parsed[1]))
    return r

if __name__ == '__main__':
    import sys
    f = open(sys.argv[1],'r')
    print parse_file(f)

