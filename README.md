wordcount_matrix
================

Python tool to generate word count matrices

Example use: python wordcount_matrix.py -d ~/Downloads/wordpress -f .php -o wordpress.csv

Specify an optional directory path, an optional file mask (no wildcards
at this time), and an optional output file (otherwise pipe to stdout).

The first row is a comma-separated list of words in alphanumeric order.
Successive rows represent word counts for each of the remaining files.
