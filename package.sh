#!/bin/bash

version=$(grep '"version":' manifest.json | cut -d: -f2 | cut -d\" -f2)

rm -rf SHA256SUMS package
mkdir package
cp *.py manifest.json LICENSE README.md package/
cp -r css images js pkg views package/
cd package
find . -type f -exec sha256sum {} \; >> SHA256SUMS
cd ..

tar czf "voir-ma-photo-${version}.tgz" package
