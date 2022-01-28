#Assignment Python week 3
#Nikolina Vuksic
#13886975
#This is my cheat() function for Q9

def cheat(task):
    if task == "Q1.2P.9":
        my_solution_1= """
        insect_sprays = pd.read_csv('InsectSprays.csv').to_dict()
        insect_sprays.keys()
        """
        print(my_solution_1)
    elif task == "Q3.2P.1":
        my_solution_2 = """
        import matplotlib.pyplot as plt
        import numpy as np
        my_sim_data = np.random.normal(loc=50, scale=20, size=1000)
        plt.figure()
        plt.boxplot(my_sim_data)
        import seaborn as sns
        plt.figure()
        sns.violinplot(data=my_sim_data, color='violet')
        sns.stripplot(data=my_sim_data, color='black')
        """
        print(my_solution_2)
    elif task == "Q3.2P.4":
        my_solution_3 = """
        import seaborn as sns 
        import matplotlib.pyplot as plt
        plt.subplot(1, 2, 1)
        heatmap = sns.heatmap(data.corr())
        plt.subplot(1, 2, 2)
        kdeplot = sns.kdeplot(x=data.alcohol, y=data.color_intensity)
        plt.tight_layout()
        """
        print(my_solution_3)
    elif task == "Q1.2P.7":
        print("This function does not work in a script because \n"
              "it is not a Python function" )
    else:
        print("I don't know the answer")

cheat("Q3.2P.4")
cheat("Q1.2P.1")
cheat("Q1.2P.7")