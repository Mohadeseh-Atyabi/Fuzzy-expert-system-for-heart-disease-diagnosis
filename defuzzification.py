from fuzzification import fuzzification_output_sick

fuzzification_output_sick = fuzzification_output_sick()


class defuzzification:
    def __init__(self):
        pass

    def defuzzify(self, input):
        steps = 1000
        delta = 4. / steps
        points = [i * delta for i in range(steps + 1)]
        numerator = 0.0
        denominator = 0.0

        for point in points:
            sick1 = fuzzification_output_sick.output_sick_sick1(point)
            sick2 = fuzzification_output_sick.output_sick_sick2(point)
            sick3 = fuzzification_output_sick.output_sick_sick3(point)
            sick4 = fuzzification_output_sick.output_sick_sick4(point)
            healthy = fuzzification_output_sick.output_sick_healthy(point)

            if input['output_sick1'] < sick1:
                sick1 = input['output_sick1']

            if input['output_sick2'] < sick2:
                sick2 = input['output_sick2']

            if input['output_sick3'] < sick3:
                sick3 = input['output_sick3']

            if input['output_sick4'] < sick4:
                sick4 = input['output_sick4']

            if input['output_healthy'] < healthy:
                healthy = input['output_healthy']

            result = max(healthy, sick1, sick2, sick3, sick4)

            numerator += result * point * delta
            denominator += result * delta
        try:
            centerOfMass = round(numerator / denominator, 3)
        except ZeroDivisionError:
            centerOfMass = 0

        result_text = ''
        if centerOfMass < 1.78:
            result_text += ' & ' + 'healthy' if result_text != '' else 'healthy'
        if 1 <= centerOfMass <= 2.51:
            result_text += ' & ' + 'sick1' if result_text != '' else 'sick1'
        if 1.78 <= centerOfMass <= 3.25:
            result_text += ' & ' + 'sick2' if result_text != '' else 'sick2'
        if 1.5 <= centerOfMass <= 4.5:
            result_text += ' & ' + 'sick3' if result_text != '' else 'sick3'
        if 3.25 < centerOfMass:
            result_text += ' & ' + 'sick4' if result_text != '' else 'sick4'

        return result_text + ": " + str(centerOfMass)