class fuzzification_chest_pain:
    def __init__(self):
        pass

    def typical_angina(self, x):
        if x == 1:
            return 1.0
        else:
            return 0.0

    def atypical_angina(self, x):
        if x == 2:
            return 1.0
        else:
            return 0.0

    def non_anginal_pain(self, x):
        if x == 3:
            return 1.0
        else:
            return 0.0

    def asymptomatic(self, x):
        if x == 4:
            return 1.0
        else:
            return 0.0

    def fuzzy_chest_pain(self, x):
        return {'typical_anginal': self.typical_angina(x), 'atypical_anginal': self.atypical_angina(x),
                'non_anginal_pain': self.non_anginal_pain(x), 'asymptomatic': self.asymptomatic(x)}



class fuzzification_cholesterol:
    def __init__(self):
        pass

    def low_cholesterol(self, x):
        if 0 <= x <= 151:
            return 1.0
        elif 151 < x <= 197:
            return (-1.0 / 46) * x + 197 / 46.0
        else:
            return 0.0

    def medium_cholesterol(self, x):
        if 188 <= x <= 215:
            return (1.0 / 27) * x - 188 / 27.0
        elif 215 < x <= 250:
            return (-1.0 / 35) * x + 250 / 35.0
        else:
            return 0.0

    def high_cholesterol(self, x):
        if 217 <= x <= 263:
            return (1.0 / 46) * x - 217 / 46.0
        elif 263 < x <= 307:
            return (-1.0 / 44) * x + 307 / 44.0
        else:
            return 0.0

    def veryHigh_cholesterol(self, x):
        if 0 <= x <= 281:
            return 0.0
        elif 281 < x <= 347:
            return (1.0 / 66) * x - 281 / 66.0
        else:
            return 1.0

    def fuzzy_cholesterol(self, x):
        return {'low': self.low_cholesterol(x), 'medium': self.medium_cholesterol(x),
                'high': self.high_cholesterol(x), 'very_high': self.veryHigh_cholesterol(x)}


class fuzzification_blood_pressure:
    def __init__(self):
        pass

    def low_blood_pressure(self, x):
        if 0 <= x <= 111:
            return 1.0
        elif 111 < x <= 134:
            return (-1.0 / 23) * x + 134 / 23.0
        else:
            return 0.0

    def medium_blood_pressure(self, x):
        if 127 <= x <= 139:
            return (1.0 / 12) * x - 127 / 12.0
        elif 139 < x <= 153:
            return (-1.0 / 14) * x + 153 / 14.0
        else:
            return 0.0

    def high_blood_pressure(self, x):
        if 142 <= x <= 157:
            return (1.0 / 15) * x - 142 / 15.0
        elif 157 < x <= 172:
            return (-1.0 / 15) * x + 172 / 15.0
        else:
            return 0.0

    def veryHigh_blood_pressure(self, x):
        if 0 <= x <= 154:
            return 0.0
        elif 154 < x <= 171:
            return (1.0 / 17) * x - 154 / 17.0
        else:
            return 1.0

    def fuzzy_blood_pressure(self, x):
        return {'low': self.low_blood_pressure(x), 'medium': self.medium_blood_pressure(x),
                'high': self.high_blood_pressure(x), 'very_high': self.veryHigh_blood_pressure(x)}


class fuzzification_ECG:
    def __init__(self):
        pass

    def normal_ECG(self, x):
        if -0.5 <= x <= 0:
            return 1.0
        elif 0 < x <= 0.4:
            return (-1.0 / 0.4) * x + 1.0
        else:
            return 0.0

    def abnormal_ECG(self, x):
        if 0.2 <= x <= 1:
            return (1.0 / 0.8) * x - 0.2 / 0.8
        elif 1 < x <= 1.8:
            return (-1.0 / 0.8) * x + 1.8 / 0.8
        else:
            return 0.0

    def hypertrophy_ECG(self, x):
        if -0.5 <= x <= 1.4:
            return 0.0
        elif 1.4 < x <= 1.9:
            return (1.0 / 0.5) * x - 1.4 / 0.5
        else:
            return 0.0

    def fuzzy_ECG(self, x):
        return {'normal': self.normal_ECG(x), 'abnormal': self.abnormal_ECG(x), 'hypertrophy': self.hypertrophy_ECG(x)}


class fuzzification_sex:
    def __init__(self):
        pass

    def male_sex(self, x):
        if x == 0:
            return 1.0
        else:
            return 0.0

    def female_sex(self, x):
        if x == 1:
            return 1.0
        else:
            return 0.0

    def fuzzy_sex(self, x):
        return {'male': self.male_sex(x), 'female': self.female_sex(x)}


class fuzzification_heart_rate:
    def __init__(self):
        pass

    def low_heart_rate(self, x):
        if 0 <= x <= 100:
            return 1.0
        elif 100 < x <= 141:
            return (-1.0 / 41) * x + 141 / 41.0
        else:
            return 0.0

    def medium_heart_rate(self, x):
        if 111 <= x <= 152:
            return (1.0 / 41) * x - 111 / 41.0
        elif 152 < x <= 194:
            return (-1.0 / 42) * x + 194 / 42.0
        else:
            return 0.0

    def high_heart_rate(self, x):
        if 0 <= x <= 152:
            return 0.0
        elif 152 < x <= 210:
            return (1.0 / 58) * x - 152 / 58.0
        else:
            return 1.0

    def fuzzy_heart_rate(self, x):
        return {'low': self.low_heart_rate(x), 'medium': self.medium_heart_rate(x), 'high': self.high_heart_rate(x)}

class fuzzification_blood_sugar:
    def __init__(self):
        pass

    def veryHigh_blood_sugar(self, x):
        if 120 <= x:
            return 1.0
        if 105 <= x < 120:
            return 0.067 * x - 7
        else:
            return 0.0

    def fuzzy_blood_sugar(self, x):
        return {'true': self.veryHigh_blood_sugar(x), 'false': 1 - self.veryHigh_blood_sugar(x)}


class fuzzification_exercise:
    def __init__(self):
        pass

    def true_exercise(self, x):
        if x == 1:
            return 1.0
        else:
            return 0.0

    def false_exercise(self, x):
        if x == 0:
            return 1.0
        else:
            return 0.0

    def fuzzy_exercise(self, x):
        return {'true': self.true_exercise(x), 'false': self.false_exercise(x)}


class fuzzification_old_peak:
    def __init__(self):
        pass

    def low_old_peak(self, x):
        if 0 <= x <= 1:
            return 1.0
        elif 1 < x <= 2:
            return (-1.0) * x + 2.0
        else:
            return 0.0

    def risk_old_peak(self, x):
        if 1.5 <= x <= 2.8:
            return (1.0 / 1.3) * x - 1.5 / 1.3
        elif 2.8 < x <= 4.2:
            return (-1.0 / 1.4) * x + 4.2 / 1.4
        else:
            return 0.0

    def terrible_old_peak(self, x):
        if 0 <= x <= 2.5:
            return 0.0
        elif 2.5 < x <= 4:
            return (1.0 / 1.5) * x - 2.5 / 1.5
        else:
            return 1.0

    def fuzzy_old_peak(self, x):
        return {'low': self.low_old_peak(x), 'risk': self.risk_old_peak(x), 'terrible': self.terrible_old_peak(x)}


class fuzzification_thallium:
    def __init__(self):
        pass

    def normal_thallium(self, x):
        if x == 3:
            return 1.0
        else:
            return 0.0

    def medium_thallium(self, x):
        if x == 6:
            return 1.0
        else:
            return 0.0

    def high_thallium(self, x):
        if x == 7:
            return 1.0
        else:
            return 0.0

    def fuzzy_thallium(self, x):
        return {'normal': self.normal_thallium(x), 'medium': self.medium_thallium(x), 'high': self.high_thallium(x)}


class fuzzification_age:
    def __init__(self):
        pass

    def young_age(self, x):
        if 0 <= x <= 29:
            return 1.0
        elif 29 < x <= 38:
            return (-1.0 / 9.0) * x + 38.0 / 9.0
        else:
            return 0.0

    def mild_age(self, x):
        if 33 <= x <= 38:
            return (1.0 / 5.0) * x - 33.0 / 5.0
        elif 38 < x <= 45:
            return (-1.0 / 7.0) * x + 45.0 / 7.0
        else:
            return 0.0

    def old_age(self, x):
        if 40 <= x <= 48:
            return (1.0 / 8.0) * x - 40.0 / 8.0
        elif 48 < x <= 58:
            return (-1.0 / 10.0) * x + 58.0 / 10.0
        else:
            return 0.0

    def veryOld_age(self, x):
        if 0 <= x <= 52:
            return 0.0
        elif 52 < x <= 60:
            return (1.0 / 8.0) * x - 52.0 / 8.0
        else:
            return 1.0

    def fuzzy_age(self, x):
        return {'young': self.young_age(x), 'mild': self.mild_age(x), 'old': self.old_age(x),
                'very_old': self.veryOld_age(x)}


class fuzzification_output_sick:
    def __init__(self):
        pass

    def output_sick_healthy(self, x):
        if 0 <= x <= 0.25:
            return 1.0
        elif 0.25 < x <= 1:
            return (-1.0 / 0.75) * x + 1 / 0.75
        else:
            return 0.0

    def output_sick_sick1(self, x):
        if 0 <= x <= 1:
            return x
        elif 1 < x <= 2:
            return (-1.0) * x + 2.0
        else:
            return 0.0

    def output_sick_sick2(self, x):
        if 1 <= x <= 2:
            return x - 1.0
        elif 2 < x <= 3:
            return (-1.0) * x + 3.0
        else:
            return 0.0

    def output_sick_sick3(self, x):
        if 2 <= x <= 3:
            return x - 2.0
        elif 3 < x <= 4:
            return -1.0 * x + 4.0
        else:
            return 0.0

    def output_sick_sick4(self, x):
        if 0 <= x <= 3:
            return 0.0
        elif 3 < x <= 3.75:
            return (1.0 / 0.75) * x - 3.0 / 0.75
        else:
            return 1.0
