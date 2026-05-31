#!/usr/bin/env python3
# User should be able to call the script with `cat weekly_youtube_ids | clean_ids.py`` 
# and the result should be output at the console of the cleaned ids.

#basic configuration for the built-in logging module
import logging
logging.basicConfig(level=logging.WARNING, filename="pipeline_audit.log")

#Given a file with youtube ids named youtube_ids
import sys
#When I cat youtube_ids into clean_ids.py
#(to execute in terminal you will write `cat youtube_ids | clean_ids.py`)
#Then I should only see valid youtube ids at the command line
import re
for line in sys.stdin:
    youtube_id = line.strip()
    if re.fullmatch(r"[A-Za-z0-9_-]{11}", youtube_id):
        print(youtube_id)
    else:
        logging.warning(f"Invalid ID: {youtube_id}")
        #exactly 11 characters as per definition of a valid youtube id
        #character set uses a modified Base64 encoding consisting of the following 64 possibilities: 
        #uppercase and lowercase letters (A-Z & a-z)
        #numbers (0-9) and hyphen (-) and underscore (_)
#And there should be a log file named pipeline_audit.log created indicating any errors
import os 
assert os.path.exists("pipeline_audit.log")
    #file is not given to me yet so I don't know which ones are invalid to be logged


#Given the file test_ids with the contents
#     abcd
#     CctJNYYCPo0
#     1234
#When I cat the file at clean_ids.py
#Then I should only see CctJNYYCPo0 at the command line
#And the log should indicate abcd and 1234 were not valid ids

#Given the script clean_ids.py
#When I call it directly with 'python3 clean_ids.py'
#Then the command line should wait for input
#    And when I type 1234 I should see no echo
#    And when I type CctJNYYCPo0, I should see it echoed
#    And when I use CTL-C I should return to the command line``