#!/usr/bin/env python

from art.splqueryutils.sessions import get_user_sessions, UserEncoder
from art.splqueryutils.jsondata import put_json_files, BYTES_IN_MB
from collections import defaultdict

import re

def main():
    commands = defaultdict(int)
    for users in  get_user_sessions(limit=800*BYTES_IN_MB, remove_autorecurring=False):
        for user in users:
            for query in user.queries:
                q = query.text.strip()
                q = replace_quotes(q)
                stages = q.split('|')
                for stage in stages:
                    stage = stage.strip()
                    parts = stage.split()
                    if len(parts) > 0:
                        command = parts[0].lower()
                        if command[0] == command[-1] == '`':
                            command = 'macro'
                        commands[command] += 1        
    commands = sorted(commands.items(), key=lambda x: x[1], reverse=True)
    for (cmd, cnt) in commands:
        print cmd, cnt

def replace_quotes(s):
    matches = re.findall(r'"[^"]*"', s)
    for m in matches:
        s = s.replace(m, "~")
    matches = re.findall(r"'[^']*'", s)
    for m in matches:
        s = s.replace(m, "~")
    matches = re.findall(r"`[^`]*`", s)
    for m in matches:
        s = s.replace(m, "`-`")
    return s

if __name__ == "__main__":
    main()
