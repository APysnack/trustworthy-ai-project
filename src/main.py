from datasets import load_dataset

dataset = load_dataset("rajpurkar/squad", split="train")

print(dataset)
print(dataset[0])