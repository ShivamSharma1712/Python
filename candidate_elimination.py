import pandas as pd
import csv


file_path = "candidate.csv"

with open(file_path, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Sky", "Temperature", "Humidity", "Wind", "Water", "Forecast", "PlayTennis"])
    writer.writerow(["Sunny", "Warm", "Normal", "Strong", "Warm", "Same", "Yes"])
    writer.writerow(["Sunny", "Warm", "High", "Strong", "Warm", "Same", "Yes"])
    writer.writerow(["Rainy", "Cold", "High", "Strong", "Warm", "Change", "No"])
    writer.writerow(["Sunny", "Warm", "High", "Strong", "Cool", "Change", "Yes"])


with open(file_path, "r") as file:
    f = csv.reader(file)
    data_list = list(f)
    for row in data_list:
        print(row)


data = pd.read_csv(file_path)

data.columns = data.columns.str.strip()
data = data.applymap(lambda x: x.strip() if isinstance(x, str) else x)


features = data.iloc[:, :-1]  
target = data.iloc[:, -1]  

def find_s_algorithm(features, target):
    
    hypothesis = None
    
    for i in range(len(features)):
        if target[i] == "Yes":  
            if hypothesis is None:
                hypothesis = features.iloc[i].values.copy()  # Set initial hypothesis
            else:
                for j in range(len(hypothesis)):
                    if features.iloc[i, j] != hypothesis[j]:
                        hypothesis[j] = "?"  
    return hypothesis  


final_hypothesis = find_s_algorithm(features, target)
print("Final Hypothesis:", final_hypothesis)