import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

np.random.seed(42)
n_samples = 2000

sqft = np.random.normal(1800, 700, n_samples).clip(400, 6000)
bedrooms = np.random.randint(1, 6, n_samples)
bathrooms = np.random.randint(1, 4, n_samples) + np.random.choice([0, 0.5], n_samples)
age = np.random.uniform(0, 80, n_samples)
distance_to_city = np.random.uniform(0.5, 40, n_samples)
crime_rate = np.random.exponential(3, n_samples).clip(0, 25)
school_rating = np.random.uniform(1, 10, n_samples)

