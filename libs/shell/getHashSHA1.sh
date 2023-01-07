#!/usr/bin/bash

echo -n $(sha1sum $1 | cut -d " " -f1)
