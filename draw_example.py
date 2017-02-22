#!/bin/env python

from web import *

web = Web()
for num in range(15):
    node = WebNode("example " + str(num))
    if num % 3:
        node.req_list.append(web.node_list[-1])
    if num > 4:
        node.opt_list.append(web.node_list[-4])
    web.node_list.append(node)

width = 1600
height = 900
web.arrange(width, height)
web.draw(width, height)

for node in web.node_list:
    print "{0}, {1}".format(node.x, node.y)
    print "{0}, {1}".format(node.left(), node.top())