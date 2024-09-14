import joblib
import numpy as np
import pandas as pd
from sklearn.isotonic import IsotonicRegression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import  GradientBoostingClassifier
from sklearn.preprocessing import MinMaxScaler

from grayhound.app.main.file_functions import is_csv_file_empty, get_file_path


def train(start_date_train, end_date_train, dist, track, params):
    print('train function')
    file_path = get_file_path(start_date_train, end_date_train, dist, track, params, mode='t')
    df_train = pd.read_csv(file_path)

    scaler = MinMaxScaler()

    scaled_features = scaler.fit_transform(df_train[params])
    y = df_train['Winner'].values.ravel()

    if np.isnan(scaled_features).any():
        print("Warning: x_features contains NaN values!")
    if np.isnan(y).any():
        print("Warning: y contains NaN values!")

    x_train, x_valid, y_train, y_valid = train_test_split(scaled_features, y, test_size=0.2, random_state=42)

    model = GradientBoostingClassifier(n_estimators=1000, max_features='sqrt', min_samples_split=2)
    model.fit(x_train, y_train)

    proba_valid = model.predict_proba(x_valid)[:, 1]

    iso_reg = IsotonicRegression(y_min=0, y_max=1, out_of_bounds='clip').fit(proba_valid, y_valid)

    joblib.dump(model, get_file_path(start_date_train, end_date_train, dist, track, params, mode='m'))
    joblib.dump(iso_reg, get_file_path(start_date_train, end_date_train, dist, track, params, mode='iso'))
    


def predict(start_date_pred=None, end_date_pred=None, start_date_train=None, end_date_train=None, dist_train=None, track_train=None, dist_pred=None, track_pred=None, params=None):
    print('predict function')

    file_path = get_file_path(start_date_pred, end_date_pred, dist_pred, track_pred, params, mode='p')

    if is_csv_file_empty(file_path):
        return {}

    model = joblib.load(get_file_path(start_date_train, end_date_train, dist_train, track_train, params, mode='m'))
    iso_reg = joblib.load(get_file_path(start_date_train, end_date_train, dist_train, track_train, params, mode='iso'))

    df_pred = pd.read_csv(file_path)

    scaler = MinMaxScaler()

    scaled_features_pred = scaler.fit_transform(df_pred[params])

    proba_test = model.predict_proba(scaled_features_pred)[:, 1]
    proba_test_isoreg = iso_reg.predict(proba_test)

    probabilities = np.round(proba_test_isoreg, 3)

    df_pred['probabilities'] = probabilities

    grouped = df_pred.groupby('Race_ID')

    results_y = [group['Finished'].tolist() for _, group in grouped]
    predictions = [group['probabilities'].tolist() for _, group in grouped]

    results_x = []
    for _, group in grouped:
        group = group.sort_values('probabilities', ascending=False)
        real_pos = np.arange(1, len(group) + 1)
        results_x.append(real_pos.tolist())

    return results_x, results_y, predictions
