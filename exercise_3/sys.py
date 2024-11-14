import cowsay
import sys

if len(sys.argv) < 2:
    print(sys.argv)
    sys.exit("Too few arguments")

cowsay.cow(f"Hello, {sys.argv[1]}")