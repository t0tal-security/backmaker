#!/usr/bin/bash

echo -n $(sha512sum $1 | cut -d " " -f1)
   