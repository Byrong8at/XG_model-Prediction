import matplotlib.pyplot as plt
import seaborn as sns

def matrice(data):
    numerical_columns = data.select_dtypes(include=['float64', 'int64']).columns
    plt.figure(figsize=(12, 8))
    sns.heatmap(data[numerical_columns].corr(), annot=True, cmap='coolwarm')
    plt.title('Correlation Heatmap')
    plt.show()

def hist(data):
    data.hist(bins=50, figsize=(20, 20))
    plt.show()

def distribution(data, name):
    sns.countplot(x=name, data=data, palette=['steelblue','orange'])
    plt.title('Distribution de la Variable Cible ')
    plt.show()