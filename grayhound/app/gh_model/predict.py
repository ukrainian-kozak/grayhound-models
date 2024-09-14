import os
import joblib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from datetime import datetime, timedelta
from grayhound.app.main.logger import GHLogger

logger = GHLogger("predict")

def load_model(dist):
    return joblib.load(os.path.join(os.getcwd(), "..", "..", "data", "models", "random_forest_class", f'model_{dist}.pkl'))

def load_imputer(dist):
    return joblib.load(os.path.join(os.getcwd(), "..", "..", "data", "imputers", f'imputer_{dist}.pkl'))

def load_encoder(dist):
    return joblib.load(os.path.join(os.getcwd(), "..", "..", "data", "encoders", f'encoder_{dist}.pkl'))


from datetime import datetime


def save_race_results_to_pdf(race_results, name: str) -> None:
    print('received: ', race_results)
    dir_path = os.path.join(os.getcwd(), "..", "..", "data", "results")
    filename = os.path.join(dir_path, name)

    with PdfPages(filename) as pdf:
        # Для каждого уникального времени гонки собираем данные
        grouped_results = {}

        for idx, (row, predictions) in enumerate(zip(race_results[0].itertuples(index=False), race_results[1])):
            # Преобразуем строку с датой и временем в объект datetime
            try:
                race_time = datetime.strptime(row.race_date_time, '%Y-%m-%d %H:%M')
            except ValueError as e:
                print(f"Error parsing date: {e}")
                race_time = row.race_date_time  # В случае ошибки используем строковое представление

            race_distance = row.raceDistance
            dog_name = row.name

            # Собираем вероятности для каждого места
            probabilities = np.round(predictions, 2)

            # Если гонка уже есть, добавляем результаты, иначе создаем новую запись
            if race_time not in grouped_results:
                grouped_results[race_time] = {'race_distance': race_distance, 'dogs': []}

            grouped_results[race_time]['dogs'].append({
                'Dog Name': dog_name,
                '1st place': probabilities[0],
                '2nd place': probabilities[1],
                '3rd place': probabilities[2],
                '4th place': probabilities[3],
                '5th place': probabilities[4],
                '6th place': probabilities[5]
            })

        # Теперь для каждой гонки создаем таблицу
        for race_time, race_info in grouped_results.items():
            race_distance = race_info['race_distance']
            dogs = race_info['dogs']

            # Создаем DataFrame для всей гонки
            df = pd.DataFrame(dogs)

            fig, ax = plt.subplots(figsize=(10, len(dogs) * 0.5 + 2))  # Зависимость высоты от количества строк
            ax.axis('tight')
            ax.axis('off')
            ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')
            ax.set_title(f"Race on {race_time}, Distance: {race_distance}m")

            pdf.savefig(fig, bbox_inches='tight')
            plt.close(fig)


def make_predictions(dfs):
    logger.debug(f"FUNCTION predict: received dfs with type: {type(dfs)}\n")


    for dist, df in dfs.items():
        if int(dist) > 270:
            continue

        print(dist)

        encoder = load_encoder(dist)
        inputer = load_imputer(dist)
        model = load_model(dist)

        columns_cat = ['raceClass', 'race_grade_1', 'race_grade_2', 'race_grade_3', 'race_grade_4', 'race_grade_5']
        df_cat = df[columns_cat]
        print(df_cat)
        df_encoded = encoder.transform(df_cat)
        df_encoded_df = pd.DataFrame(df_encoded, columns=columns_cat)
        df[columns_cat] = df_encoded_df

        df_nrr = df[['name', 'raceDistance', 'race_date_time']]
        df = df.drop(['name', 'raceDistance', 'race_date_time'], axis=1)

        X = inputer.transform(df)
        predictions = model.predict_proba(X)

        race_results = (df_nrr, predictions)

        date = datetime.today() + timedelta(days=1)
        date = date.strftime('%Y-%m-%d')
        name = f"predictions_{dist}_{date}.pdf"

        save_race_results_to_pdf(race_results, name)
