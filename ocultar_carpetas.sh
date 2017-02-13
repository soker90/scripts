#!/bin/bash

if [ -f .hidden ]; then
	rm .hidden
fi

find ./ -type d -empty >> .hidden
sed -i 's/^..//g' .hidden
