#!/bin/sh -l

cd /

version=$(python get_version.py $INPUT_PACKAGE)

if [ $? -ne 0 ]; then
    echo "Error getting package version from PyPI" >&2;

    exit 1;
fi

echo ::set-output name=version::$version
