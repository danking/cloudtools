import subprocess as sp
import sys

if sys.version_info >= (3,7):
    def safe_call(*args):
        sp.run(args, capture_output=True, check=True)
else:
    if sys.version_info >= (3,0):
        def decode(x):
            return x.decode()
    else:
        def decode(x):
            return x
    def safe_call(*args):
        try:
            sp.check_output(args, stderr=sp.STDOUT)
        except sp.CalledProcessError as e:
            print(decode(e.output))
            raise e
