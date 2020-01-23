#!/usr/bin/env python
import gtk
print (gtk.Clipboard().wait_for_contents('text/html')).data
