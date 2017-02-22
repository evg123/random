"""
Classes and data structures for storing a web
"""

import turtle
import math

def draw_square(turt, top, bot, left, right):
    turt.penup()
    turt.color(WebNode.NODE_COLOR)
    turt.goto(top, left)
    turt.pendown()
    turt.setpos(top, right)
    turt.setpos(bot, right)
    turt.setpos(bot, left)
    turt.setpos(top, left)

def draw_line(turt, x1, y1, x2, y2, color):
    turt.penup()
    turt.color(color)
    turt.goto(x1, y1)
    turt.pendown()
    turt.setpos(x2, y2)

def draw_text(turt, text, xpos, ypos):
    turt.penup()
    turt.color(WebNode.TEXT_COLOR)
    turt.goto(xpos, ypos)
    turt.pendown()
    turt.write(text, False, align="center")

class Web(object):
    
    def __init__(self):
        self.node_list = []
    
    def size(self):
        return len(self.node_list)
    
    # organize the web and set the positions of the webnodes
    def arrange(self, width, height):
        # arrange the nodes in a circle
        
        # center the circle in the canvas
        cx = cy = 0
        
        # calculate radius but don't fill the entire screen
        radius = min(width / 2, height / 2) * .8
        
        incr = (2 * math.pi) / self.size()
        cur_angle = 0
        
        for node in self.node_list:
            node.x = cx + radius * math.cos(cur_angle)
            node.y = cy + radius * math.sin(cur_angle)
            cur_angle += incr


    # draw the web using the current positions of the webnodes
    def draw(self, width, height):
        turt = turtle.Turtle()
        turtle.setup(width, height)
        turtle.speed(0)
        
        for node in self.node_list:
            # draw the requirements lines
            for other in node.req_list:
                draw_line(turt, node.x, node.y, other.x, other.y, WebNode.REQ_COLOR)
            
            # draw the optional lines
            for other in node.opt_list:
                draw_line(turt, node.x, node.y, other.x, other.y, WebNode.OPT_COLOR)
            
            # draw the node itself
            draw_square(turt, node.top(), node.bot(), node.left(), node.right())
            draw_text(turt, node.content, node.x, node.y)
        
        turtle.Screen().exitonclick()
    
class WebNode(object):
    
    NODE_COLOR = "black"
    REQ_COLOR = "blue"
    OPT_COLOR = "green"
    TEXT_COLOR = "black"
    
    DEFAULT_WIDTH = 50
    DEFAULT_HEIGHT = 50
    
    def __init__(self, content):
        self.content = content
        self.req_list = [] # these nodes are required before getting to this one
        self.opt_list = [] # these are optional nodes can lead to this one
        
        # position to display this node at
        # coords are of the center of the square
        self.x = 0
        self.y = 0
        self.z = 0
        
        self.width = WebNode.DEFAULT_WIDTH
        self.height = WebNode.DEFAULT_HEIGHT
    
    def top(self):
        return self.y - (self.height / 2)
    def bot(self):
        return self.y + (self.height / 2)
    def left(self):
        return self.x - (self.width / 2)
    def right(self):
        return self.x + (self.width / 2)
    
