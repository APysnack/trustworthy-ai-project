from squad import SquadDataset
from experiment import run_experiment
from storage import save_json


dataset = SquadDataset()

examples = dataset.get_range(0, 10)

# runs src/experiment/runner.py
results = run_experiment(examples)

save_json(results)
