# module demo

haha = 6

def instant_drama():
    return "So it has come to this."   # https://xkcd.com/1022/

def our_difference(who, where):
    return "{} never go back to {}".format(who, where)


# https://docs.python.org/3/tutorial/modules.html#executing-modules-as-scripts
if __name__ == "__main__":
    print('This is run when you execute this script directly (python3 carpetstore.py), not run if you import it (import carpetstore).')
