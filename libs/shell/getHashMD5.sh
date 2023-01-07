#!/usr/bin/bash

echo -n $(md5sum $1 | cut -d " " -f1)
