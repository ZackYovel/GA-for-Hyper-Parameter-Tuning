import json
import numpy as np

"""
Format of ecosystem is:
{
  'last_generation': int,
  'times': [float,...],
  'improvements': [float,...],
  'average_total_improve': [float,...],
  'runtime_running_avg': float,
  'total_runtime': float,
  'need_drift': [False,...],
  'drifted_last_generation': [False,...],
  'best_mae': [float,...],
  'std': [float,...],
  'avg_mae_survivors': [{
    'generation': int,
    'values': [None] * n_territories,
  }],
  'territories': [
    [{hp:{}, mae=None},...],
    .
    .
    .
  ]
}
"""

ecosystem = None

with open('ecosystem.json') as f:
    ecosystem = json.load(f)

best_ter = ecosystem['territories'][0]
for ter in ecosystem['territories']:
    if ter[0]['mae'] < best_ter[0]['mae']:
        best_ter = ter

params = {}
for ind in best_ter:
  for key, val in ind['hp'].items():
    if key == 'n_estimators' and val > 1500:
      print(val)
    if key in params:
      params[key].append(val)
    else:
      params[key] = [val]

for key, val in params.items():
  print("*" * 10, key, "*" * 10)
  mean = np.mean(val)
  std = np.std(val)
  minimum = np.min(val)
  maximum = np.max(val)
  print("Mean:", mean)
  print("STD:", std)
  print("Range:", mean - std, mean + std, mean + std - (mean - std))
  print("Minimum:", minimum, "Maximum:", maximum)
  print("Best:", best_ter[0]['hp'][key])