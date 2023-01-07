#!/usr/bin/bash

echo -n $(sha256sum $1 | cut -d " " -f1)