def main():
    from . import build
    import sys
    args = sys.argv[1:]
    if not args:
        print("Usage: exebuilder <file> [--quiet]")
        return
    file = args[0]
    flags = args[1:]
    prt = "--quiet" not in flags
    build(file,prt)
if __name__ == "__main__":
    main()