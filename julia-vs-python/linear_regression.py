import pandas as pd
from sklearn.preprocessing import OneHotEncoder

insurance_df = pd.read_csv('medium-articles/julia-vs-python/data/insurance.csv')
insurance_df.info()
print('\nSeparating categorical and numerical...\n')
categorical_variable_cols = ['sex', 'smoker', 'region']
categorical_df = insurance_df[categorical_variable_cols]
wip_insurance_df = insurance_df.drop(categorical_variable_cols, axis=1)

print('Getting ready for OHE...\n')
onehot_encoder = OneHotEncoder(sparse=False)
categorical_array = onehot_encoder.fit_transform(categorical_df)

print('Outputting the encoded data...\n')

X = insurance_df.drop(['charges'], axis=1)
y = insurance_df['charges']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=500)