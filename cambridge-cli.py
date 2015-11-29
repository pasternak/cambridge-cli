#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import sys

from urllib.request import urlopen
from bs4 import BeautifulSoup

CAMBRIDGE_ENDPOINT = \
    "http://dictionary.cambridge.org/dictionary/english"


def usage():
    print("Usage: {name} idiom/word".format(name=sys.argv[0]))
    sys.exit(1)


def main(idiom):
    term = re.sub(r"\s", "-", idiom)
    cdict = urlopen("/".join([CAMBRIDGE_ENDPOINT, term]))
    soup = soup = BeautifulSoup(cdict, 'html.parser')

    desc = soup.find(attrs={"name": "description"})['content']
    example = soup.find(attrs={"title": "Example"})

    desc = desc[:-15].split(":")
    print("\n\033[1m{desc}:\033[0m".format(desc=desc[0]))
    print("\t>> {definition}".format(definition=desc[1]))

    try:
        print("\n[-] Example:")
        print("\t{example}\n".format(example=example.get_text()))
    except:
        pass

if __name__ == "__main__":
    if len(sys.argv) < 2:
        usage()
    main(sys.argv[1])
