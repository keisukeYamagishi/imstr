# coding:utf-8
import numpy as np
import cv2
import sys

def convert_hexColor(r,b,g):
    hex_color = '#' + Hex_s(r) + Hex_s(b) + Hex_s(g)
    return  hex_color

def start_html():
    return '<!DOCTYPE html>\n<html>\n\t<head>\n\t\t<meta charset="utf-8">\n\t\t<title></title>\n\t</head>\n\t<body>'

def end_html():
    return '</pre>\n\t</body>\n\t</html>'

def span_html(r,g,b):
    return '<span style="color:' + convert_hexColor(r,g,b) + '; ">#</span>'

def writeToFile():
    write_html = open('./index.html','w')
    write_html.write(html)
    write_html.close()

def Hex_s(hex_s):
    hexNumber = hex(hex_s)
    strings = format(hexNumber)
    split_str = strings.split('x')
    split = split_str[1]
    return split

def EmurateColor(w, h):
    b = img[wid_num,hei_num,0]
    g = img[wid_num,hei_num,1]
    r = img[wid_num,hei_num,2]
    return (r,g,b)

html = start_html()

img = cv2.imread('./fuckIage.png', cv2.IMREAD_COLOR)

if img is None:
    print ('Failuer loaded image')
    sys.exit(1)

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
            color  = EmurateColor(wid_num,hei_num)
            html = html + span_html(color[0],color[1],color[2])

html = html + end_html()
writeToFile()

print ('Complete')
