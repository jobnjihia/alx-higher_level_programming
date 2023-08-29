#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        execu_saf = fct(*args)
        return execu_saf
    except Exception as error:
        import sys
        print("Exception: {}".format(error), file=sys.stderr)
        return None
