import re
import argparse
from urllib.request import Request, urlopen
from jsbeautifier import beautify

pattern_regexp = re.compile(r'[a-zA-Z0-9_\-\.]+')

ignore_words = {"function",
                "for"
                }


def fetchWords(jsdata):
    data_dup = pattern_regexp.findall(beautify(jsdata))
    remove_ignored_words = [' '.join(words for words in place.split() if words not in ignore_words)
                            for place in data_dup
                            ]
    verified_list = []
    for string in remove_ignored_words:
        if string.isnumeric():
            continue
        if string != "" and len(string) >= 2 and string.isalnum() and string.isascii():
            verified_list.append(string)

    unique_words = list(dict.fromkeys(verified_list))
    print(unique_words)


parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", help="File containing js urls", type=str, required=True)
args = parser.parse_args()
js_file = str(args.file)

file = open(js_file, 'r')
file_urls = file.readlines()
for url in file_urls:
    js_url = Request(url,
                     headers={'User-Agent': 'Mozilla/5.0'})
    data = urlopen(js_url).read().decode("utf-8")

    fetchWords(data)
