#!/bin/bash

cd $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS

if [ -f .hidden ]; then
	rm .hidden
fi

find ./ -type d -empty >> .hidden
sed -i 's/^..//g' .hidden
