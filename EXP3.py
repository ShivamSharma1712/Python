import matplotlib.pylab as plt
import pandas as pd;


filename = r"C:\Users\hp\OneDrive\Documents\PYTHON\auto.csv"
headers=["symboling","normalized-losses","make","fuel-type","aspiration","num-of-doors","body-style","drive-wheels",
         "engine-location","wheel-base","length","width","height","curb-weight","engine-type","num-of-cylinders",
         "engine-size","fuel-system","compression-ratio","horsepower","peak-rpm","city-mpg","highway-mpg","price_1"]


df = pd.read_csv(filename, names='headers')