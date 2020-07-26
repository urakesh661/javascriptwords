# jswords

This script is for creating wordlist from javascript files.The script takes a file having js urls as input.
Java script is beautified using jsbeautifier.The script fetches all the words having length greater than 2.It also ignores all the words which
only contains digits.
Also words which are to be ignored can be specified in the script and they won't be returned in the output.

Syntax :  python jswords.py -f /home/rakesh/Desktop/testfile.txt
