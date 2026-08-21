import pandas as pd
from sklearn.impute import KNNImputer

def free_fix(df: pd.DataFrame):

    amenities = ['RoomService', 'FoodCourt', 'ShoppingMall', 'Spa', 'VRDeck']
    
    for col in amenities:
        condition = (df['CryoSleep'] == True) & (df[col].isna())
        df.loc[condition, col] = 0
        
    return df


def add_is_missing_indicator(df: pd.DataFrame)->pd.DataFrame:

    cols_with_missing = df.columns[df.isna().any()].tolist()
    for col in cols_with_missing:
        df[f'{col}_is_missing'] =  df[col].isna().astype(int)

    return df 


def fill_by_group(df: pd.DataFrame)-> pd.DataFrame:

    df['Group'] = df['PassengerId'].str.split('_').str[0]
    df['Surname'] = df['Name'].str.split(' ').str[-1]

    shared_features = ['HomePlanet', 'Cabin', 'Destination']

    for feature in shared_features:
        known = df.dropna(subset=[feature])
        group_lookup = known.set_index('Group')[feature].to_dict()
        df[feature] = df[feature].fillna(df['Group'].map(group_lookup))

    return df


def fill_mode(df: pd.DataFrame)-> pd.DataFrame:


    categorical_cols = ['HomePlanet', 'Destination', 'VIP', 'CryoSleep']
    
    for col in categorical_cols:
        most_common_value = df[col].mode()[0]
        df[col] = df[col].fillna(most_common_value)
        
    return df


def impute_numeric_knn(df: pd.DataFrame)-> pd.DataFrame:

    numeric_cols = ['Age', 'RoomService', 'FoodCourt', 'ShoppingMall', 'Spa', 'VRDeck']
    knn = KNNImputer(n_neighbors=5)
    imputed_data = knn.fit_transform(df[numeric_cols])
    df[numeric_cols] = imputed_data
    
    return df


def fill_leftovers(df: pd.DataFrame)-> pd.DataFrame:
    
    df['Name'] = df['Name'].fillna('Unknown')
    df['Surname'] = df['Surname'].fillna('Unknown')
    df['Cabin'] = df['Cabin'].fillna('U/9999/U')
    
    return df


def split_cabin(df: pd.DataFrame)-> pd.DataFrame:
    
    df[['Deck', 'Num', 'Side']] = df['Cabin'].str.split('/', expand=True)
    df['Num'] = df['Num'].astype(float)
    
    return df


def format_and_drop(df: pd.DataFrame)-> pd.DataFrame:

    df['CryoSleep'] = df['CryoSleep'].astype(int)
    df['VIP'] = df['VIP'].astype(int)
    
    if 'Transported' in df.columns:
        df['Transported'] = df['Transported'].astype(int)

    cols_to_drop = ['PassengerId', 'Name', 'Surname', 'Group', 'Cabin']
    df = df.drop(columns=[col for col in cols_to_drop if col in df.columns])
    
    return df


def encode_categories(df: pd.DataFrame)-> pd.DataFrame:

    categorical_cols = ['HomePlanet', 'Destination', 'Deck', 'Side']
    
    # pd.get_dummies automatically creates the 1s and 0s columns 
    df = pd.get_dummies(df, columns=categorical_cols)
    
    return df