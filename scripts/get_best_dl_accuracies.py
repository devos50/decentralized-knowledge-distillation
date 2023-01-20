"""
Read dl_accuracies.csv and determine the round that produced the model with the high accuracies.
"""
from statistics import mean

NUM_PEERS = 200

accs_per_round = {}
with open("../data/dl_accuracies.csv") as in_file:
    parsed_header = False
    for line in in_file.readlines():
        if not parsed_header:
            parsed_header = True
            continue

        parts = line.strip().split(",")
        round_nr = int(parts[4])
        acc, loss = float(parts[5]), float(parts[6])
        if round_nr not in accs_per_round:
            accs_per_round[round_nr] = []
        accs_per_round[round_nr].append((acc, loss))

round_highest_accs = 0
highest_avg_acc = 0
for round_nr in accs_per_round.keys():
    avg_acc = mean([info[0] for info in accs_per_round[round_nr]])
    if avg_acc > highest_avg_acc:
        highest_avg_acc = avg_acc
        round_highest_accs = round_nr

#print("Round with highest average accuracy: %d (%f)" % (round_highest_accs, highest_avg_acc))

for acc, loss in accs_per_round[round_highest_accs]:
    print("cifar10,DL,0,%d,100,0.002,%f,%f" % (NUM_PEERS, acc, loss))