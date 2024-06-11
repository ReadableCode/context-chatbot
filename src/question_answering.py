# %%
# Running Imports #

import nltk.corpus
import torch
from transformers import pipeline

# %%
# Variables and Setup #

nltk.download("genesis")

# load text
context = nltk.corpus.genesis.raw("english-kjv.txt")

# Check if GPU is available and use it
device = 0 if torch.cuda.is_available() else -1
print(f"Using device: {[torch.cuda.get_device_name(device)]}")
print(f"Using {['GPU' if device == 0 else 'CPU']}")

# load question answering model
model = pipeline(model="deepset/roberta-base-squad2", device=device)


# %%
# Main #

if __name__ == "__main__":
    # receive user input continuously
    while True:
        # collect input
        user_input = input("\nYour question:")

        if user_input == "exit":
            break
        else:
            # enter input into model
            output = model(question=user_input, context=context)

            print(
                # print likelihood
                round(output["score"], 2),
                # print separator
                "|",
                # print answer
                output["answer"],
            )

# %%
