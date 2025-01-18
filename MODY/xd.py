import pandas as pd

# Wczytaj oba pliki
file_1920 = pd.read_csv(r'C:\Magisterka\Predicting-the-results-of-Premier-League-matches\MODY\season-1819.csv')  # Podaj ścieżkę do swojego pliku
file_2019_20 = pd.read_csv(r'C:\Magisterka\Predicting-the-results-of-Premier-League-matches\MODY\2018-19.csv')  # Podaj ścieżkę do swojego pliku

missing_columns = [col for col in file_2019_20.columns if col not in file_1920.columns]

# Dodaj brakujące kolumny do file_1920 z wartościami NaN (lub innymi wartościami domyślnymi, jeśli chcesz)
for col in missing_columns:
    file_1920[col] = pd.NA  # Możesz użyć np. `None` lub innej wartości domyślnej

# Przekształcenie file_1920, aby miało tę samą kolejność kolumn, co file_2019_20
file_1920 = file_1920[file_2019_20.columns]

# Zapisz wynikowy plik
file_1920.to_csv('season_1920_with_2019_20_columns.csv', index=False)

print("Zmodyfikowany plik zapisany jako 'season_1920_with_2019_20_columns.csv'")