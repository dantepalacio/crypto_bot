from prompts.request_prompt import PROMPT_BIG
from prompts.dialogue_text import BIG
from prompts.split_text import split_text_into_fragments
from generate.generation_config import generate_cpu, generate_gpu,parse_text, return_text

file_path = '/workspace/llama2/cli_llama2/real_text.txt'


with open(file_path, 'r', encoding='utf-8') as file:
    file_contents = file.read()


DIALOGUE_BATCHES = []
fragments = split_text_into_fragments(file_contents, max_fragment_length=5000)
for i, fragment in enumerate(fragments):
    print(f"Фрагмент {i + 1}:\n{fragment}\n")
    DIALOGUE_BATCHES.append(fragment)

merge = []
for i in DIALOGUE_BATCHES:
    prompt = f'''
    Ниже представлен фрагмент из одного общего текста совещания, твоя задача сделать суммаризацию предоставленного отрезка.

    Распиши как можно подробнее, о чем был разговор.

    Сохрани в своем ответе все важные числа, даты, имена, проблемы, идеи, решения  из входного текста:

    {i}

    Суммаризация:
    '''
    generated_text = generate_gpu(prompt)
    batch = return_text(generated_text)
    merge.append(batch)

final = ' '.join(merge)
print('ЫВПЫГВРПГНЫВПГНШЫПВГНПЦГНУПГНЦУ', final)



PROMPT_1 = f'''
Это куски из одного общего текста, которые уже были суммаризированны. Ты должен превратить этот текст в читабельный формат, сохрани все важные числа, даты, имена, идеи, проблемы в своем ответе.

Не придумывай лишнего, опирайся лишь на входной текст.

Распиши как можно подробнее, о чем был разговор, с чего начали, к чему пришли. Распиши все идеи, проблемы, решения.

Давай думать шаг за шагом

{final}

Общий и складный текст:
 '''

generated_text = generate_gpu(PROMPT_1)
parse_text(generated_text)
