
class validated:

    def paramsnoemtpy(self, valores):
        responses = False
        for P1 in valores:
            if P1 == "":
                responses = True
                return responses

        return responses