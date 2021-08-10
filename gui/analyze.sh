#!/bin/bash
cd "object-detector"
while IFS='' read -r line || [[ -n "$line" ]]; do
	echo $line
    $line
done < "gui/args.txt"
