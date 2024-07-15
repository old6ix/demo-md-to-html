import markdown

with open('example.md', 'r', encoding='utf-8') as f:
    md_str = f.read()

html = markdown.markdown(md_str)

with open('output.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f'{type(html) = }')
print(html)
