#!/bin/bash

echo "Ciao dal mio script" 
ls -l ./ > nuovissimoFile.txt

if grep -q root /etc/passwd; then
 echo la parola root si trova nel file passwd
else
 echo la parola non è nel file
fi
