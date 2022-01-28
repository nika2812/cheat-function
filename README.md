### cheat() function
This is task 9 from Python assignment containing my cheat() function

### General information
This cheat() function takes argument "task", specifying which exercise of previous Python assignment the user wants to cheat on. 
Function tells the correct solutions for exercices Q1.2P.9, Q3.2P.1, Q3.2P.4 and Q1.2P.7. If user tries to get the solution for some other task, the output is: 
"I don't know the answer"


### Usage
You write cheat() function and choose among following exercises: Q1.2P.9, Q3.2P.1, Q3.2P.4 and Q1.2P.7.
For those four exercises you can get the correct code as an output

```
cheat("Q3.2P.4")

#output:
        import seaborn as sns 
        import matplotlib.pyplot as plt
        plt.subplot(1, 2, 1)
        heatmap = sns.heatmap(data.corr())
        plt.subplot(1, 2, 2)
        kdeplot = sns.kdeplot(x=data.alcohol, y=data.color_intensity)
        plt.tight_layout()
        
   ```
