default empathy = 0
default clarity = 0
default memory_fragments = 0
default truth = 0
default self_awareness = 0
default suspicion = 0

init python:
    def get_ending():
        if (empathy == 3 and clarity == 3 and memory_fragments == 3
            and truth == 1 and self_awareness == 2 and suspicion == 0):
            return "secret"
        if empathy >= 2 and self_awareness >= 1:
            return "return"
        if clarity >= 2 and truth >= 1:
            return "stay"
        return "let_go"
