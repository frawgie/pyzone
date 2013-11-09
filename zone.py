#!/usr/bin/env python2.7
import argparse

SITES = ["www.reddit.com", 
    "news.ycombinator.com", 
    "www.medium.com"]

def main():
    args = parse_args()
    if args.on:
        block_sites()
    elif args.off:
        unblock_sites()

def block_sites():
    with open("/etc/hosts", "a") as hosts:
        for site in SITES:
            hosts.write("127.0.0.1 %s" % site)

def unblock_sites():
    stripped_hosts = []
    with open("/etc/hosts", "r+") as hosts:
        for line in hosts.readlines():
            if not filter(lambda site: site in line, SITES):
                stripped_hosts.append(line)
        hosts.writelines(stripped_hosts)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-on", action="store_true")
    parser.add_argument("-off", action="store_true")
    return parser.parse_args()

if __name__ == '__main__':
    main()
