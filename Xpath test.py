from lxml import etree
import io

f = io.StringIO('<foo><bar></bar></foo>')
tree = etree.parse(f)

r = tree.xpath('/foo/bar')
r[0].tag

r = tree.xpath('bar')
r[0].tag

root = tree.getroot()
r = root.xpath('bar')
r[0].tag

bar = root[0]
r= bar.xpath('/foo/bar')
r[0].tag

tree = bar.getroottree()
r = tree.xpath('/foo/bar')
r[0].tag

print(root.xpath(expr, name = "bar")[0].tag)

expr = "//*[local-name() = $name]"
print(root.xpath(expr, name = "foo")[0].tag)

print(root.xpath("$text",text = "Hello World!"))

root = etree.XML("<root><a>TEXT</a></root>")
find_text = etree.XPath("//text()")
text = find_text(root)[0]
print(text)

find_text = etree.XPath("//text()",smart_strings = False)
text = find_text(root)[0]
print(text)

hasattr(text,'getparent')

a = etree.Element("a")
b = etree.SubElement(a,"b")
c = etree.SubElement(a,"c")
d1 = etree.SubElement(c,"d")
d2 = etree.SubElement(c,"d")
tree = etree.ElementTree(c)

print(tree.getpath(d2))

tree.xpath(tree.getpath(d2)) == [d2]

root = etree.XML("<root><a><b/></a><b/></root>")
find = etree.XPath("//b")
print(find(root)[0].tag)

count_elements = etree.XPath("count(//*[local-name() = $name])")

print(count_elements(root, name = "a"))

print(count_elements(root, name = "b"))

root = etree.XML("<root xmlns='NS'><a><b/></a><b/></root>")
find = etree.XPath("//n:b", namespaces={'n':'NS'})
print(find(root)[0].tag)

regexpNS = "http://exslt.org/regular-expressions"
find = etree.XPath("//*[re:test(., '^abc$','i')]",namespaces={'re':regexpNS})
root = etree.XML("<root><a>aB</a><b>aBc</b></root>")
print(find(root)[0].text)

root = etree.XML("<root xmlns='ns'><a><b/></a><b/></root>")
find = etree.XPath("//p:b",namespaces={'p':'ns'})
print(find(root)[0].tag)

find = etree.ETXPath("//{ns}b")
print(find(root)[0].tag)