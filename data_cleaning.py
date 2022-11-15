def is_null(train, test):
    print(train.isnull().sum())
    print('------------------')
    print(test.isnull().sum())