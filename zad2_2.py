import sys
import os

for i in sys.argv[1:]:
    try:
        print os.environ[i]
    except KeyError, err:
        print >> sys.stderr, "Zmienna", i, "nie istnieje"


