def bool_question(question : str, valid_responses : list) -> bool:
    response = None
    answer = input(question)
    while response is None:
        try:
            if answer in valid_responses:
                if answer == valid_responses[0]:
                    response = True
                else:
                    response = False
            else:
                raise ValueError(f"Your response '{answer}' isn't one of the valid options")
        except ValueError as e:
            print(str(e))
            answer = input(question)
    return response