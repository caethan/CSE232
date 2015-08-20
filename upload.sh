#!/bin/bash

#Actually upload the course files to the website!

cd webpage
rsync -r * cse232@acm.wustl.edu
cd ../
