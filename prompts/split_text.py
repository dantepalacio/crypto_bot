import re


def split_text_into_fragments(text, max_fragment_length):
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)

    fragments = []
    current_fragment = ""

    for sentence in sentences:
        if len(current_fragment) + len(sentence) <= max_fragment_length:
            current_fragment += sentence + " "
        else:
            if current_fragment:
                fragments.append(current_fragment.strip())
                current_fragment = ""


            for i in range(len(sentence)):
                if len(current_fragment) + i <= max_fragment_length:
                    current_fragment += sentence[i]
                else:
                    break

    if current_fragment:
        fragments.append(current_fragment.strip())

    return fragments

