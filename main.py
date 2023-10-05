from prompts.request_prompt import PROMPT, PROMPT_BIG
from prompts.split_text import split_text_into_fragments
from generate.generation_config import generate_cpu, generate_gpu,parse_text, return_text

DIALOGUE_BATCHES = []
fragments = split_text_into_fragments(PROMPT_BIG, max_fragment_length=4000)
for i, fragment in enumerate(fragments):
    print(f"Фрагмент {i + 1}:\n{fragment}\n")
    DIALOGUE_BATCHES.append(fragment)

merge = []
for i in DIALOGUE_BATCHES:
    prompt = f'''
    Суммаризируй этот диалог::
    {i}

    Summary:
    '''
    generated_text = generate_gpu(prompt)
    batch = return_text(generated_text)
    merge.append(batch)
    
final = ' '.join(merge)
print(final)



# generated_text = generate_gpu(PROMPT)
# parse_text(generated_text)