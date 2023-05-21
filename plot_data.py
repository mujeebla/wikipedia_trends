import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
# import matplotlib.lines as lines
# from datetime import datetime, timedelta

# import matplotlib.image as image
# from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from textwrap import shorten

from presentation import Base

def plot_line_chart(df):
    fig = plt.figure(FigureClass=Base)
    ax = fig.add_subplot()
    fig.subplots_adjust(bottom=0.1, top=0.85)
    articles = df.article.unique()
    
    colors = ['#311B7E', '#6B4CD9', '#3DB2FF', '#31D490', '#FF4F61']
    df1 = df[df.article==articles[0]]
    
    for article, color in zip(articles, colors):
        sub_df = df[df.article==article]
        name = shorten(article.replace("_"," "), width=15, placeholder="...")
        ax.plot_date(sub_df.timestamp, sub_df.views, linestyle='solid', color=color, linewidth=2)
        ax.text(sub_df.timestamp.values[-1], sub_df.views.values[-1], f'{name}', color=color, ha='left')
    
    ax.xaxis.set_major_formatter(mdates.ConciseDateFormatter(ax.xaxis.get_major_locator()))
    ax.grid(True, 'major', 'y', ls='--', lw=.5, c='k', alpha=.3)
    
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['left'].set_visible(False)
    
    ax.set_ylabel('Views')
    return fig
