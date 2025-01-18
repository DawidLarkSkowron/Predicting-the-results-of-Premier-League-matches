import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pickle

# Wczytaj dane
dataset = pd.read_csv(r'C:\Magisterka\Predicting-the-results-of-Premier-League-matches\TEST\final_dataset_2.csv')

# Wybierz odpowiednie cechy i cel (np. wynik meczu)
features = ['HTGS', 'ATGS', 'HTGC', 'ATGC', 'HTP', 'ATP', 'HTFormPts', 'ATFormPts']  # przykład cech
target = 'FTHG'  # wynik meczu dla drużyny gospodarzy (np. liczba bramek strzelonych przez gospodarzy)

# Przygotuj dane wejściowe (X) i wynik (y)
X = dataset[features]
y = dataset[target]

# Podziel dane na zbiór treningowy i testowy
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Stwórz model regresji liniowej
model = LinearRegression()

# Trenuj model
model.fit(X_train, y_train)

# Zapisz model do pliku
with open('model_2.pkl', 'wb') as file:
    pickle.dump(model, file)

print("Model wytrenowany i zapisany.")
