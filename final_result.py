import fuzzification
import inference
import defuzzification


class ProvideResult(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ProvideResult, cls).__new__(cls)
        return cls.instance

    @staticmethod
    def get_final_result(input_dict: dict) -> str:
        print(input_dict.keys())
        fuzzification_chest_pain = fuzzification.fuzzification_chest_pain()
        fuzzy_chest_pain = fuzzification_chest_pain.fuzzy_chest_pain(int(input_dict['chest_pain']))

        fuzzification_bloodPressure = fuzzification.fuzzification_blood_pressure()
        fuzzy_blood_pressure = fuzzification_bloodPressure.fuzzy_blood_pressure(int(input_dict['blood_pressure']))

        fuzzification_cholestrol = fuzzification.fuzzification_cholesterol()
        fuzzy_cholesterol = fuzzification_cholestrol.fuzzy_cholesterol(int(input_dict['cholestrol']))

        fuzzification_blood_sugar = fuzzification.fuzzification_blood_sugar()
        fuzzy_blood_sugar = fuzzification_blood_sugar.fuzzy_blood_sugar(int(input_dict['blood_sugar']))

        fuzzification_ECG = fuzzification.fuzzification_ECG()
        fuzzy_ECG = fuzzification_ECG.fuzzy_ECG(float(input_dict['ecg']))

        fuzzification_heart_rate = fuzzification.fuzzification_heart_rate()
        fuzzy_heart_rate = fuzzification_heart_rate.fuzzy_heart_rate(int(input_dict['heart_rate']))

        fuzzification_exercise = fuzzification.fuzzification_exercise()
        fuzzy_exercise = fuzzification_exercise.fuzzy_exercise(int(input_dict['exercise']))

        fuzzification_old_peak = fuzzification.fuzzification_old_peak()
        fuzzy_old_peak = fuzzification_old_peak.fuzzy_old_peak(float(input_dict['old_peak']))

        fuzzification_thallium = fuzzification.fuzzification_thallium()
        fuzzy_thallium = fuzzification_thallium.fuzzy_thallium(int(input_dict['thallium_scan']))

        fuzzification_sex = fuzzification.fuzzification_sex()
        fuzzy_sex = fuzzification_sex.fuzzy_sex(int(input_dict['sex']))

        fuzzification_age = fuzzification.fuzzification_age()
        fuzzy_age = fuzzification_age.fuzzy_age(int(input_dict['age']))

        inference_logic = inference.inference()
        fuzzy_sick = inference_logic.inference(fuzzy_chest_pain, fuzzy_blood_pressure, fuzzy_cholesterol,
                                               fuzzy_blood_sugar, fuzzy_ECG, fuzzy_heart_rate, fuzzy_exercise, fuzzy_old_peak, fuzzy_thallium, fuzzy_sex, fuzzy_age)
        print(fuzzy_sick)

        defuzzification_logic = defuzzification.defuzzification()
        return defuzzification_logic.defuzzify(fuzzy_sick)