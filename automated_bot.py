#!/usr/bin/python3.10

import argparse
import service

CONFIG_FILE_PATH = "config.ini"

parser = argparse.ArgumentParser(description='Automated Bot Script')
parser.add_argument('-f', '--config-file', type=str, help='Path of the config file.')

args = parser.parse_args()


if args.config_file:
    CONFIG_FILE_PATH = args.config_file

k = service.run_bot(CONFIG_FILE_PATH)
print("Automated bot created all users, posts.")
