from clasa_de_intrebari import Question, run_test

question_prompts = [
    "Ce mananca un caine?\n(a) oase\n (b) cirese\n(c) ciocolata\n\n",
    "Cu ce poti zbura?\n(a) caruta\n (b) masina\n(c) avion\n\n",
    "Unde se afla Bucuresti?\n(a) Ungaria\n(b) Anglia\n(c) Romania\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "c")
]

run_test(questions)
