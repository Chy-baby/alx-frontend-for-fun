#!/usr/bin/python3

"""
markdown2html.py: A script to convert Markdown files to HTML.

Usage:
    ./markdown2html.py <input_file.md> <output_file.html>
"""

import sys
import os
import markdown
import re
import hashlib

def convert_markdown_to_html(markdown_file, output_file):
    """
    Convert a Markdown file to HTML.

    Args:
        markdown_file (str): Path to the Markdown input file.
        output_file (str): Path to the HTML output file.
    """
    try:
        with open(markdown_file, 'r') as md_file:
            markdown_text = md_file.read()
            markdown_text = re.sub(r'\[\[(.*?)\]\]', lambda match: hashlib.md5(match.group(1).encode()).hexdigest(), markdown_text)
            markdown_text = re.sub(r'\(\((.*?)\)\)', lambda match: match.group(1).replace('c', '').replace('C', ''), markdown_text)
            html_content = markdown.markdown(
                markdown_text,
                extensions=['markdown.extensions.extra']
            )
            with open(output_file, 'w') as html_file:
                html_file.write(html_content)
    except FileNotFoundError:
        sys.stderr.write(f"Missing {markdown_file}\n")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        sys.exit(1)

    markdown_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.exists(markdown_file):
        sys.stderr.write(f"Missing {markdown_file}\n")
        sys.exit(1)

    convert_markdown_to_html(markdown_file, output_file)
    sys.exit(0)

