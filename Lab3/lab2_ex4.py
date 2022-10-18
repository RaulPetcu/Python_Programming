def xml_builder(tag, content, d):
    value = {i for i in d if d[i] == 'http://python.org'}
    value2 = {i for i in d if d[i] == 'my_link'}
    value3 = {i for i in d if d[i] == 'someid'}
    string = '<' + tag + ' ' + str(value) + '=' + d.get('href') + "/" + str(value2) + '=' + d.get('_class') + ',' + str(
        value3) + '=' + d.get('id') + '>' + content + ' ' + '</' + tag + '>'
    return string

tag = 'a'
content = 'Hello there'
d1 = dict(href='http://python.org', _class='my_link', id='someid')
print(xml_builder(tag, content, d1))