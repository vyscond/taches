import os
import shlex
import subprocess

class Shell (object):

    def __init__(self, env):
        self.env = os.environ.copy()
        self.env.update(env)


class Unicodes:
    cross_mark = '\u274C'
    flag = '\u2691'
    check_mark = '\u2713'
    heavy_check_mark = '\u2714'


def failure(msg):
    print("\033[91m\u2691\033[0m {msg}".format(msg=msg))


def success(msg):
    print("\033[92m\u2691\033[0m {msg}".format(msg=msg))


def run(cmd, alias=None, silent=True, env=None):
    cmd = shlex.split(cmd)
    alias = alias or cmd[0]
    env = env or os.environ.copy()
    stdout = subprocess.DEVNULL if silent else None
    ret = subprocess.call(cmd, stdout=stdout, env=env)
    if ret:
        failure('[{}] failed'.format(alias))
    else:
        success('[{}] succeed'.format(alias))
    return ret

def batch(cmds):
    for cmd in cmds:
        run(cmd)
