from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

COLUMNS = col_train_num
FEATURES = col_train_num_bis
LABEL = "SalePrice"
FEATURES_CAT = col_train_cat

engineered_features = []
for continuous_feature in FEATURES:
    engineered_features.append(
        tf.contrib.layers.real_valued_column(continuous_feature)
    )
for categorical_feature in FEATURES_CAT:
    sparse_column = tf.contrib.layers.sparse_column_with_hash_bucket(
        categorical_feature, hash_bucket_size=1000
    )
    engineered_features.append(
        tf.contrib.layers.embedding_column(
            sparse_id_column=sparse_column, dimension=16, combiner="sum"
        )
    )