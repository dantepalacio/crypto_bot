import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from dotenv import load_dotenv
import os


from optimization.bnb_config import create_bnb_config

# load_dotenv()
# HF_TOKEN = os.environ.get('HF_TOKEN')

# MODEL_NAME = "OpenBuddy/openbuddy-llama2-13b-v8.1-fp16"


# def load_model():
#     model = AutoModelForCausalLM.from_pretrained(
#         MODEL_NAME,
#         # quantization_config=bnb_config,
#         # load_in_4bit=True,
#         torch_dtype=torch.float16,
#         device_map="auto", 
#         use_auth_token = HF_TOKEN,
#         offload_folder="offload",
#     )
#     print('Модель скачалась')
#     tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, use_auth_token=HF_TOKEN)

#     tokenizer.pad_token = tokenizer.eos_token
#     print('Токенизатор скачался')

#     return model, tokenizer






# bnb_config = create_bnb_config()
# model, tokenizer = load_model(model_name)


# _ = tokenizer.save_pretrained('models/tokenizer')
# _ = model.save_pretrained('models/model')



load_dotenv()
HF_TOKEN = os.environ.get('HF_TOKEN')

MODEL_NAME = "OpenBuddy/openbuddy-llama2-13b-v8.1-fp16"


def load_model():
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME,
        # quantization_config=bnb_config,
        load_in_4bit=True,
        torch_dtype=torch.float16,
        device_map="cuda", 
        use_auth_token = HF_TOKEN,
        offload_folder="offload",
    )
    print('Модель скачалась')
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, use_auth_token=HF_TOKEN)

    tokenizer.pad_token = tokenizer.eos_token
    print('Токенизатор скачался')

    return model, tokenizer






bnb_config = create_bnb_config()
# model, tokenizer = load_model(model_name)


# _ = tokenizer.save_pretrained('models/tokenizer')
# _ = model.save_pretrained('models/model')
