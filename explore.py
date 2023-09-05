import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from scipy.stats import pearsonr, spearmanr

from env import get_db_url
import wrangle as w
import prepare as p
import matplotlib as mpl
mpl.rcParams["axes.formatter.useoffset"] = False
mpl.rcParams["axes.formatter.limits"] = (-1_000_000, 1_000_000)

def plot_categorical_and_continuous_vars(df, x, y, order):
    plt.figure(figsize=(16,9))
    
    sns.catplot(data= df, x= x, y= y, hue='county', order=order)
    plt.title(f'catplot of {x} versus {y}')
    plt.xticks(rotation='vertical')
    plt.xlim() 
    plt.show()
    print('~~~~~~~~~~~~~~~~~~')
    plt.figure(figsize=(16,9))
    sns.barplot(data=df, x= x, y=y, order=order)
    plt.title(f'bargraph of {x} versus {y}')
    plt.xticks(rotation='vertical')
    plt.show()
    print('~~~~~~~~~~~~~~~~~~')
    plt.figure(figsize=(16,9))
    sns.violinplot(data=df, x=x,y=y, hue='county', order=order)
    plt.title(f' {x} versus {y}')
    plt.xticks(rotation='vertical')
    plt.show()
    print('~~~~~~~~~~~~~~~~~~')