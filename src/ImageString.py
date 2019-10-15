#!/usr/local/bin/python
# coding:utf-8
import cv2
import numpy as np
import sys
import os
from String import String

class ImageString:

    def __init__(self, imagePath, option):
        self.imagePath = imagePath
        self.option = option

    def convert_hexColor(self,r,b,g):
        hex_color = '#' + self.hex_s(r) + self.hex_s(b) + self.hex_s(g)
        return  hex_color

    def start_html(self):
        return '<!DOCTYPE html>\n<html>\n\t<head>\n\t\t<meta charset="utf-8">\n\t\t<title></title>\n\t</head>\n\t<body>'

    def end_html(self):
        return '</pre>\n\t</body>\n\t</html>'

    def span_html(self,r,g,b):
        return '<span style="color:' + self.convert_hexColor(r,g,b) + '; ">#</span>'

    def writeToFile(self,html):
        write_html = open(String(self.option.htmlName).formatStr(),'w')
        write_html.write(html)
        write_html.close()

    def hex_s(self,hex_s):
        hexNumber = hex(hex_s)
        strings = format(hexNumber)
        split_str = strings.split('x')
        split = split_str[1]
        return split

    def emurateColor(self,wid_num, hei_num,image):
        self.b = image[wid_num,hei_num,0]
        self.g = image[wid_num,hei_num,1]
        self.r = image[wid_num,hei_num,2]
        return (self.r,self.g,self.b)

    def createHtml(self):

        html = self.start_html()

        if self.option.OUTPUT_PATH == 0:
            print ('create path: => ' + String(self.option.htmlName).formatStr())

        img = cv2.imread(self.imagePath , cv2.IMREAD_COLOR)
        if img is None:
            print ('Failuer loaded image')
            return

        hei, wid = img.shape[:2]

        for wid_num in range(0,hei):
            if wid_num == 0:
                html = html + '<pre style="font: 10px/5px monospace;">'
            else:
                html = html + '<br>'

            for hei_num in range(0, wid):
                if img[wid_num,hei_num,0] is None:
                    print ("none obj")
                else:
                    color  = self.emurateColor(wid_num,hei_num,img)
                    html = html + self.span_html(color[0],color[1],color[2])

        html = html + self.end_html()
        self.writeToFile(html)

        print ('Complete\n🍺 ')
