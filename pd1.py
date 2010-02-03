import sys, glob, re, getopt, os, fnmatch

def usage():
    print """Usage:
        %s [option] expression [directory]

        OPTIONS

            -r
                recursive search

            -h, --help
                this text

            -c, --content
                find in files
        """ % sys.argv[0]

def main():
    try:
        opts, args = getopt.gnu_getopt(sys.argv[1:], 'hcr', ['help', 'content'])
    except getopt.GetoptError, err:
        print str(err)
        print __doc__
        return 1

    recursive = False
    content = False
    for o, a in opts:
        if o in ('-h', '--help'):
            usage()
            return 1
        if o in ('-c', '--content'):
            content = True
        if o == '-r':
            recursive = True

    def znaleziono_wzorzec_w_pliku(file):
        wynik = False
        try:
            plik = open(file, 'r')
            try:
                regex = fnmatch.translate(args[0])
                for line in plik:
                    if re.match(regex, line):
                        wynik = True
                        break
            finally:
                plik.close()
        except IOError, err:
            print >> sys.stderr, str(err)
        return wynik

    def recursive_path(cwd=os.getcwd()):
        listdir = os.listdir(cwd)
        dirs = [ d for d in listdir if os.path.isdir(cwd + '/' + d) ]
        regex = fnmatch.translate(args[0])
        for l in listdir:
            if re.match(regex, l):
                print os.path.abspath(cwd + '/' + l)
        for d in dirs:
            recursive_path(cwd + '/' + d)

    def recursive_content(cwd=os.getcwd()):
        listdir = os.listdir(cwd)
        dirs = [ d for d in listdir if os.path.isdir(cwd + '/' + d) ]
        files = [ f for f in listdir if os.path.isfile(cwd + '/' + f) ]
        for file in files:
            if znaleziono_wzorzec_w_pliku(os.path.abspath(cwd + '/' + file)):
                print os.path.abspath(cwd + '/' + file)
        for dir in dirs:
            recursive_content(cwd + '/' + dir)

    def dopasuj():
        if recursive:
            if content: #DONE
                recursive_content()
            else: #DONE
                recursive_path()
        else:
            if content: # DONE
                cwd = os.getcwd()
                listdir = os.listdir(cwd)
                files = [ file for file in listdir if os.path.isfile(file) ]
                pasujace = []
                for file in files:
                    if znaleziono_wzorzec_w_pliku(os.path.abspath(file)):
                        pasujace.append(file)

                if pasujace:
                    for p in pasujace:
                        print os.path.abspath(p)
                else:
                    print >> sys.stderr, "niczego nie znaleziono"

            else: #DONE
                pasujace = glob.glob(args[0])
                if pasujace:
                    for p in pasujace:
                        print os.path.abspath(p)
                else:
                    print >> sys.stderr, "niczego nie znaleziono"

    if len(args) == 1:
        dopasuj()
    elif len(args) == 2:
        # zmien katalog i wykonaj to co wyzej
        os.chdir(args[1])
        dopasuj()
    else:
        print >> sys.stderr, "za duzo argumentow"
        usage()
        return 1
    return 0

if __name__ == '__main__':
    sys.exit(main())
