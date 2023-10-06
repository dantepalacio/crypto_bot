import json
import textwrap
import torch

from prompts.system_prompt import B_INST, SYSTEM_PROMPT, E_INST
from models.load_model import load_model


model, tokenizer = load_model()


def get_prompt(instruction):
    '''
    Function is called to merge all of prompts
    :instruction: request prompt
    '''

    prompt_template =  B_INST + SYSTEM_PROMPT + instruction + E_INST
    return prompt_template

def cut_off_text(text, prompt):
    '''
    Function is called to remove the end-of-sequence tokens from output
    :text: model's output
    :prompt: eos token
    '''

    cutoff_phrase = prompt
    index = text.find(cutoff_phrase)
    if index != -1:
        return text[:index]
    else:
        return text

def remove_substring(string, substring):
    '''
    Function is called to remove the request prompt from the final output
    :string: model's output
    :substring: request prompt
    '''

    return string.replace(substring, "")

def generate_gpu(text):
    '''
    the function is responsible for generating the raw model response
    :text: request prompt
    '''

    prompt = get_prompt(text)
    with torch.autocast('cuda', dtype=torch.float16):
        inputs = tokenizer(prompt, return_tensors="pt").to('cuda')
        outputs = model.generate(**inputs,
                                 max_length = 3000,
                                 eos_token_id = tokenizer.eos_token_id,
                                 pad_token_id = tokenizer.eos_token_id,
                                 temperature = 0.2,
                                 min_length = 256,
                                 )
        final_outputs = tokenizer.batch_decode(outputs, skip_special_tokens=True, num_beans=1)[0]
        final_outputs = cut_off_text(final_outputs, '</s>')
        final_outputs = remove_substring(final_outputs, prompt)

    return final_outputs


def generate_cpu(text):
    print('generate_cpu')
    '''
    the function is responsible for generating the raw model response
    :text: request prompt
    '''

    prompt = get_prompt(text)
    with torch.autocast('cpu', dtype=torch.bfloat16):
        print('началась генерация')
        inputs = tokenizer(prompt, return_tensors="pt", return_token_type_ids=False)
        outputs = model.generate(**inputs,
                                max_new_tokens = 2048,
                                eos_token_id = tokenizer.eos_token_id,
                                pad_token_id = tokenizer.eos_token_id,
                                temperature = 0.5,
                                min_new_tokens = 256
                                )
        print('Генерация закончилась')
        final_outputs = tokenizer.batch_decode(outputs, skip_special_tokens=True, num_beans=1)[0]
        final_outputs = cut_off_text(final_outputs, '</s>')
        final_outputs = remove_substring(final_outputs, prompt)

    return final_outputs


def parse_text(text):
        print('Текст обрабатывается')
        '''
        parse_text procedure is needed to print the final text
        :param text: generated text by model
        '''

        wrapped_text = textwrap.fill(text, width=100)
        print(wrapped_text +'\n\n')
        # return assistant_text


def return_text(text):
        wrapped_text = textwrap.fill(text, width=100)
        assistant_text = wrapped_text +'\n\n'
        return assistant_text
