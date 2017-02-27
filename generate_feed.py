#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import path

title = 'Vi syns vid fnasket!'
description = 'En podcast med godtyckliga referenser till Gävle'
link = 'http://www.visynsvidfnasket.se'
title_image_link = 'FlaskWebProject1/static/images/title.jpg'

def create_feed():
    out = ''
    

feed_path = 'FlaskWebProject1/static/xml/feed.xml'

if not path.isfile(feed_path):
    create_feed()