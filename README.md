# In this project I want to explore some ways to load a csv files

## 1. Using native Python APIs (or functions)
In files I explore the use of dictionary and list structures with native Python API (csv).

## 2. Processing 1B rows and aggregate with Python (src/duckdb/duckdb_csv.py e src/pandas/pandas_csv.py)
Inspired by [The One Billion Row Challenge](https://github.com/gunnarmorling/1brc), originally proposed for Java.

![imagem_01](./images/1brc.png)

### Procedimento
- Clonar o repositorio do projeto [load_file](https://github.com/Silmara-Basso/load_file.git)
- Rodar o código utilizando Pyenv, Poetry e VSCode
- Instalar as dependencias


### Sumary

#### Pandas

Starting file processing.
Processing:  10%|██████████▍                                                                                             | 1/10 [00:00<00:00, 78.30it/s]
                                             station      min      max     mean
0  # Adapted from https://simplemaps.com/data/wor...      NaN      NaN      NaN
1  # Licensed under Creative Commons Attribution ...      NaN      NaN      NaN
2                                           A Coruña  43.3667  43.3667  43.3667
3                                           A Yun Pa  13.3939  13.3939  13.3939
4                                           Aabenraa  55.0444  55.0444  55.0444
Processing took: 0.65 sec

#### DuckDB

┌───────────────────────────────────────────────────────────────────────────────────────────────┬─────────────────┬──────────────────┬─────────────────┐
│                                            station                                            │ min_temperature │ mean_temperature │ max_temperature │
│                                            varchar                                            │  decimal(3,1)   │   decimal(3,1)   │  decimal(3,1)   │
├───────────────────────────────────────────────────────────────────────────────────────────────┼─────────────────┼──────────────────┼─────────────────┤
│ # Adapted from https://simplemaps.com/data/world-cities                                       │            NULL │             NULL │            NULL │
│ # Licensed under Creative Commons Attribution 4.0 (https://creativecommons.org/licenses/by/…  │            NULL │             NULL │            NULL │
│ A Coruña                                                                                      │            43.4 │             43.4 │            43.4 │
│ A Yun Pa                                                                                      │            13.4 │             13.4 │            13.4 │
│ Aabenraa                                                                                      │            55.0 │             55.0 │            55.0 │
│ Aachen                                                                                        │            50.8 │             50.8 │            50.8 │
│ Aadorf                                                                                        │            47.5 │             47.5 │            47.5 │
│ Aalborg                                                                                       │            57.1 │             57.1 │            57.1 │
│ Aalen                                                                                         │            48.8 │             48.8 │            48.8 │
│ Aaley                                                                                         │            33.8 │             33.8 │            33.8 │
│   ·                                                                                           │              ·  │               ·  │              ·  │
│   ·                                                                                           │              ·  │               ·  │              ·  │
│   ·                                                                                           │              ·  │               ·  │              ·  │
│ Dodge City                                                                                    │            37.8 │             37.8 │            37.8 │
│ Dodji-Bata                                                                                    │             6.7 │              6.7 │             6.7 │
│ Dodola                                                                                        │             7.0 │              7.0 │             7.0 │
│ Dodoma                                                                                        │            -6.2 │             -6.2 │            -6.2 │
│ Dodvad                                                                                        │            15.8 │             15.8 │            15.8 │
│ Dodworth                                                                                      │            53.5 │             53.5 │            53.5 │
│ Doesburg                                                                                      │            52.0 │             52.0 │            52.0 │
│ Doetinchem                                                                                    │            52.0 │             52.0 │            52.0 │
│ Dogbo                                                                                         │             6.8 │              6.8 │             6.8 │
│ Dogāchi                                                                                       │            24.6 │             24.6 │            24.6 │
├───────────────────────────────────────────────────────────────────────────────────────────────┴─────────────────┴──────────────────┴─────────────────┤
│ ? rows (>9999 rows, 20 shown)                                                                                                              4 columns │
└──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

Duckdb Took: 0.02 sec