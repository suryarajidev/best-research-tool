import csv
filepath = "output.csv"
labels = ["Question: ", "1: ", "2: ", "3: ", "4: ", "5: ", "6: "]
def main():
  name = input("What's your name?    ")
  file_name = "answers_" + name + ".csv"
  print(file_name)
  print("")
  with open(file_name, "w", newline = "", encoding = "utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Question", "Clarity", "Completeness", "Accuracy", "Brevity"])
    prompts = readCsv(filepath)
    for index, line in enumerate(prompts):
      if index == 0:
        continue
      for j in range(0, 7):
        print(labels[j], line[j])
        print("")
      row =[]
      row.append(line[0])
      print("\n")
      print("Which of the answers is the best for: ")
      row.append(ask_user("clarity"))
      row.append(ask_user("completeness"))
      row.append(ask_user("accuracy"))
      row.append(ask_user("brevity"))
      writer.writerow(row)
      print("\n")
      



def readCsv(filepath):
  allrows = []
  with open(filepath, encoding = "utf-8") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
      allrows.append(row)
    
  return allrows

def ask_user(category):
  valid = ["1", "2", "3", "4", "5", "6"]
  explanations = {
    "brevity": "Brevity is how short and concise an answer is.",
    "clarity": "Clarity is how clear and easy to understand an answer is.",
    "completeness": "Completeness is how much of the question an answer responds to.",
    "accuracy": "Accuracy is how accurate information is and how relevant it is to the question."
  }
  while True:
    answer = input(f"{category}:  ")
    if not answer in valid:
      print(explanations[category])
    else:
      # print("Your answer has been recorded.")
      print("")
      break
  return answer

main()