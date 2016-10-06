# coding=utf-8

INPUT_FILE = None   # Use stdin as default input
OUTPUT_FILE = None  # Use stdout as default output
FILE_MAX_SIZE = 1024 * 1024  # 1 MB
STRIP = True
PRE = False  # Add pre tags?
PROMO = False  # Should I add a promo text at the end of stripped files?
PROMO_TEXT = '- NFO Stripped by pyStripper -'
NEWLINE = '\r\n'  # Character to be used as line break in the final output
