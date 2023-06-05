import pandas as pd
import numpy as np 
# We'll also import seaborn, a Python graphing library
import seaborn as sns
import warnings # current version of seaborn generates a bunch of warnings that we'll ignore
warnings.filterwarnings("ignore")
import matplotlib.pyplot as plt
from textblob import TextBlob

df = pd.read_csv('tripadvisor_hotel_reviews.csv')
def polarity(x):
    blob = TextBlob(x)
    return blob.sentiment.polarity
df['polarity']= df['Review'].apply(polarity)