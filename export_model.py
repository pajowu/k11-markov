from models import MODELS

MAX_LEN = 10

model = MODELS["lindenstrasse"]
chain = model["model"].chain
begin_choices = chain.begin_choices

BEGIN = "___BEGIN__"
END = "___END__"

# input_set = set(model['names'])

def all_next(state, depth):
    if depth >= MAX_LEN:
        return state
    for next_word in chain.model[state]:
        if next_word == END:
            yield state
        else:
            new_state = state[1:] + (next_word,)
            if new_state == state:
                yield state
            else:
                for rest in all_next(new_state, depth+1):
                    yield (state[0],) + rest

new_sentences = set()
for begin_choice in begin_choices:
    state = ((BEGIN,) * (chain.state_size - 1)) + (begin_choice,)
    sentences = list(all_next(state, 0))
    if sentences and len(sentences[0]) > 1:
        for sentence in sentences:
            sentence = sentence[1:]
            if model['model'].test_sentence_output(sentence, 1, 100): # Check that this is a new sentence
                new_sentences.add(" ".join(sentence))
                if len(new_sentences) == 100:
                    break
