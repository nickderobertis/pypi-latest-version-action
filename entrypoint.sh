#!/bin/sh -l

version=$(python get_version.py $INPUT_PACKAGE)
echo ::set-output name=version::$version
