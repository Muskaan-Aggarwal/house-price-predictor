# Build the training set and the prediction set
training_set = train[FEATURES + FEATURES_CAT]
prediction_set = train.SalePrice

# Split the train and prediction sets into test train sets
x_train, x_test, y_train, y_test = train_test_split(
    training_set[FEATURES + FEATURES_CAT], prediction_set, test_size=0.2, random_state=42
)

y_train = pd.DataFrame(y_train, columns=[LABEL])
training_set = pd.DataFrame(x_train, columns=FEATURES + FEATURES_CAT).merge(
    y_train, left_index=True, right_index=True
)
y_test = pd.DataFrame(y_test, columns=[LABEL])
testing_set = pd.DataFrame(x_test, columns=FEATURES + FEATURES_CAT).merge(
    y_test, left_index=True, right_index=True
)