#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

latexmk --pdflua --outdir=./out --auxdir=/tmp/latex/ main.tex
