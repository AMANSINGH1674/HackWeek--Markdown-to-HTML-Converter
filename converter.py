import argparse
import sys
import os

try:
    import markdown
except ImportError:
    print("The 'markdown' package is required. Install it with 'pip install markdown'.")
    sys.exit(1)

def convert_markdown_to_html(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as md_file:
        md_content = md_file.read()
    html_content = markdown.markdown(md_content, extensions=['extra', 'codehilite', 'toc'])
    title = os.path.splitext(os.path.basename(input_path))[0]
    full_html = f'''<!DOCTYPE html>\n<html>\n<head>\n    <meta charset="utf-8">\n    <title>{title}</title>\n</head>\n<body>\n{html_content}\n</body>\n</html>'''
    with open(output_path, 'w', encoding='utf-8') as html_file:
        html_file.write(full_html)

def main():
    parser = argparse.ArgumentParser(description='Convert a Markdown file to HTML.')
    parser.add_argument('input', help='Path to the input Markdown (.md) file')
    parser.add_argument('output', help='Path to the output HTML (.html) file')
    args = parser.parse_args()

    convert_markdown_to_html(args.input, args.output)
    print(f"Converted '{args.input}' to '{args.output}' successfully.")

if __name__ == '__main__':
    main() 