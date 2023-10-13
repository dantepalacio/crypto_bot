from prompts.request_prompt import PROMPT_BIG
from prompts.dialogue_text import BIG
from prompts.split_text import split_text_into_fragments
from generate.generation_config import generate_gpu,parse_text, return_text

# file_path = '/workspace/llama2/cli_llama2/real_text.txt'


# with open(file_path, 'r', encoding='utf-8') as file:
#     file_contents = file.read()


DIALOGUE_BATCHES = []
fragments = split_text_into_fragments(BIG, max_fragment_length=5000)
for i, fragment in enumerate(fragments):
    DIALOGUE_BATCHES.append(fragment)



merge = []
for i in DIALOGUE_BATCHES:
    PROMPT = f'''
    '''
    generated_text = generate_gpu(PROMPT)
    batch = return_text(generated_text)
    merge.append(batch)


final = ' '.join(merge)
print(final)
print('_________________________________________________________')



PROMPT_1 = f'''

 '''

generated_text = generate_gpu(PROMPT_1)
parse_text(generated_text)
