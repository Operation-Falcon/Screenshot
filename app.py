import sys
import argparse
from banner.banner import banner_design
from function import screenshot_url, screenshot_file_url
banner=banner_design()

parser=argparse.ArgumentParser(description=banner, formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('-u', '--url', type=str, help='target url')
parser.add_argument('-f', '--file', help='file containing urls')
args=parser.parse_args()

if len(sys.argv)==3 and sys.argv[2]==args.url:
    screenshot_url(args.url)
elif len(sys.argv)==3 and sys.argv[2]==args.file:
    screenshot_file_url(args.file)