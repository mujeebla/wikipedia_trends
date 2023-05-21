# Putting it all in a function to generate a page given an image, text and heading

# Create Base Image Class

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import matplotlib.patches as patches
import matplotlib.lines as lines
import numpy as np
import matplotlib.image as image
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from datetime import datetime, timedelta
from textwrap import shorten, wrap

plt.rcParams['font.size']=18
plt.rcParams['font.family']="Futura"
plt.rcParams.update({'figure.max_open_warning': 0})

class Base(Figure):

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        
        yesterday = datetime.now() - timedelta(1)
        date_string = yesterday.strftime("%b %d, %Y")

        IMAGE = image.imread("Wikipedia-Emblem.png")
        ab = AnnotationBbox(OffsetImage(IMAGE, zoom=0.035),(0.8, 0.85),xycoords='figure fraction',
            box_alignment = (0,0),pad=0, frameon=False)
        self.add_artist(ab)
        self.add_artist(lines.Line2D([0.05, 0.1], [0.89, 0.89], c="black", linewidth=3))

        self.subplots_adjust(bottom=0.1, top=0.85)
        self.set_size_inches(13.333,7.5)
        self.set_facecolor("#FBFBFB")
        
        caption = f"Wikipedia Trending: {date_string}"
        self.text(0.045, 0.91, caption, fontsize="xx-large", ha="left", va="baseline", fontweight="bold")
        self.text(0.5, 0.015, "By: Mujeeb Lawal", fontsize="x-small", ha="center", va="baseline")

class DocGenerator(Base):
    
    def __init__(self, *args, image_path, text, heading, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.text(0.1, 0.75, heading, fontsize="x-large", ha="left", va="baseline", fontweight="bold")
        
        IMAGE2 = image.imread(image_path)
        ab = AnnotationBbox(OffsetImage(IMAGE2),(0.1, 0.3),xycoords='figure fraction',
            box_alignment = (0,0),pad=0, frameon=False)
        self.add_artist(ab)
        
        self.text(0.4, 0.4, '\n'.join(wrap(text)), fontsize="small", ha="left", va="baseline")
