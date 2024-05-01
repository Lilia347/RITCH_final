import subprocess
from subprocess import Popen, PIPE, STDOUT
from contextlib import contextmanager
import threading
from datetime import datetime

def timeout( p ):
    if p.poll() is None:
        p.kill()


def get_output(filename, info_in_test):
    cmd = f"Python {filename}"
    info_in_test = list(map(str, info_in_test))
    st = datetime.now()
    proc = Popen(cmd.split(' '), stdout=PIPE, stderr=PIPE, stdin=PIPE, text=True)
    try:
        (output, error) = proc.communicate(input="\n".join(info_in_test), timeout=3)
    except:
        output, error = "", "TLTLTLTLT"
    result = str(output).strip("'")
    if "\\n" in result:
        result = str(result).split("\\n")
    else:
        result = str(result).split("\n")
    if not error:
        return result[:-1]
    else:
        return str(error)


def into_file(name, text):
    with open(name, "w") as d:
        d.write(text)
    return name


def tests_operator(code, filename2, tests_file):
    filename1 = into_file("testing.py", code)
    all_tests = []
    with open(tests_file) as ts:
        ts = ts.read().split("!!!")
        for i in ts:
            all_tests.append(i.strip("\n").split("\n"))
    good = True

    for i in all_tests:
        aaa = get_output(filename1, i)
        bbb = get_output(filename2, i)
        print(aaa, bbb, i)
        if aaa != bbb:
            good = False
            break
    return int(good)
