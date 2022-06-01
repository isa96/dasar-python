# ** Syntax keyword_argument_list
def create_html(tag, text, **attribute):
    html = f"<{tag}"
    for key, value in attribute.items():
        html = html + f" {key}='{value}'"
    
    html = html + f">{text}</{tag}>"
    return html

html = create_html("p", "hai", style="paragraf")
print(html)
html = create_html("a", "link", href="www.aaa.com", style="link")
print(html)
html = create_html("div", "Div", style="bbb")
print(html)