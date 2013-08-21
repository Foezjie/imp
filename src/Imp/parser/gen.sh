#!/bin/bash

LINE=$(grep -n -e "language=Python3;" < Imp.g  | cut -f 1 -d ':')

sed -i "$LINE s/\/\/\(.*\)/\1/g" Imp.g
java -cp ../../../bin/antlr-3.4.1.jar:../../../bin/antlr-runtime-3.4.1.jar:../../../bin/ST-4.0.5.jar org.antlr.Tool Imp.g
sed -i "$LINE s/.*/\/\/&/g" Imp.g
sed -i "s/from antlr3/from Imp.antlr3/g" ImpLexer.py ImpParser.py
