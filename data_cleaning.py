import matplotlib.pyplot as plt
def is_null(train, test):
    print(train.isnull().sum())
    print('------------------')
    print(test.isnull().sum())

def missing_values(train, test):
    fig = plt.figure(figsize=(8, 5))
    ax = fig.add_subplot(111)
    ax = train.boxplot(column='Fare', by=['Embarked', 'Pclass'], ax=ax)
    plt.axhline(y=80, color='green')
    ax.set_title('', y=1.1)
    train[train.Embarked.isnull()][['Fare', 'Pclass', 'Embarked']]

