from bs4 import BeautifulSoup
html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>
  <ol>
    <li class="special">This list item is special.</li>
    <li class="special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")
# d = soup.select("[data-example]")
# print(soup.body.div)
# print(soup.find_all(attrs={"data-example":"yes"}))
# print(soup.find_all(class_="special"))

#css
# print(soup.select("#first")[0])
# print(soup.select("[data-example]"))
#select and findall returns a list, find returns one item

#get_text, name, attrs
# print(soup.select(".special")[0].get_text())
# for el in soup.select(".special"):
#     print(el.name)
#     print(el.attrs)

data = soup.body.contents[1].next_sibling.next_sibling
#.find_parent, parent, find_next_sibling() doesnt return empty
print(data)