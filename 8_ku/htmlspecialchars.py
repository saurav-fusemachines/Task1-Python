def html_special_chars(data):
    data = data.replace("&","&amp;")
    data = data.replace("<","&lt;")
    data = data.replace(">","&gt;")
    data = data.replace('"',"&quot;")
    return data
    

print(html_special_chars("<h2>Hello World</h2>"))
print(html_special_chars("Hello, how would you & I fare?"))
print(html_special_chars('How was "The Matrix"?  Did you like it?'))