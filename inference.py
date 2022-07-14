class inference:
    def __init__(self):
        pass

    def inference(self, chest_pain, blood_pressure, cholesterol, blood_sugar, ECG, heart_rate, exercise,
                  old_peak, thallium, sex, age):
        output_sick1 = []
        output_sick2 = []
        output_sick3 = []
        output_sick4 = []
        output_healthy = []

        output_sick4.append(min(age['very_old'], chest_pain['atypical_anginal']))           # Rule 1
        output_sick4.append(min(heart_rate['high'], age['old']))                            # Rule 2
        output_sick3.append(min(sex['male'], heart_rate['medium']))                         # Rule 3
        output_sick2.append(min(sex['female'], heart_rate['medium']))                       # Rule 4
        output_sick3.append(min(chest_pain['non_anginal_pain'], blood_pressure['high']))    # Rule 5
        output_sick2.append(min(chest_pain['typical_anginal'], heart_rate['medium']))       # Rule 6
        output_sick3.append(min(blood_sugar['true'], age['mild']))                          # Rule 7
        output_sick2.append(min(blood_sugar['false'], blood_pressure['very_high']))         # Rule 8
        output_sick1.append(max(chest_pain['asymptomatic'], age['very_old']))               # Rule 9
        output_sick1.append(max(blood_pressure['high'], heart_rate['low']))                 # Rule 10
        output_healthy.append(chest_pain['typical_anginal'])                                # Rule 11
        output_sick1.append(chest_pain['atypical_anginal'])                                 # Rule 12
        output_sick2.append(chest_pain['non_anginal_pain'])                                 # Rule 13
        output_sick3.append(chest_pain['asymptomatic'])                                     # Rule 14
        output_sick4.append(chest_pain['asymptomatic'])                                     # Rule 15
        output_sick1.append(sex['female'])                                                  # Rule 16
        output_sick2.append(sex['male'])                                                    # Rule 17
        output_healthy.append(blood_pressure['low'])                                        # Rule 18
        output_sick1.append(blood_pressure['medium'])                                       # Rule 19
        output_sick2.append(blood_pressure['high'])                                         # Rule 20
        output_sick3.append(blood_pressure['high'])                                         # Rule 21
        output_sick4.append(blood_pressure['very_high'])                                    # Rule 22
        output_healthy.append(cholesterol['low'])                                           # Rule 23
        output_sick1.append(cholesterol['medium'])                                          # Rule 24
        output_sick2.append(cholesterol['high'])                                            # Rule 25
        output_sick3.append(cholesterol['high'])                                            # Rule 26
        output_sick4.append(cholesterol['very_high'])                                       # Rule 27
        output_sick2.append(blood_sugar['true'])                                            # Rule 28
        output_healthy.append(ECG['normal'])                                                # Rule 29
        output_sick1.append(ECG['normal'])                                                  # Rule 30
        output_sick2.append(ECG['abnormal'])                                                # Rule 31
        output_sick3.append(ECG['hypertrophy'])                                             # Rule 32
        output_sick4.append(ECG['hypertrophy'])                                             # Rule 33
        output_healthy.append(heart_rate['low'])                                            # Rule 34
        output_sick1.append(heart_rate['medium'])                                           # Rule 35
        output_sick2.append(heart_rate['medium'])                                           # Rule 36
        output_sick3.append(heart_rate['high'])                                             # Rule 37
        output_sick4.append(heart_rate['high'])                                             # Rule 38
        output_sick2.append(exercise['true'])                                               # Rule 39
        output_healthy.append(old_peak['low'])                                              # Rule 40
        output_sick1.append(old_peak['low'])                                                # Rule 41
        output_sick2.append(old_peak['terrible'])                                           # Rule 42
        output_sick3.append(old_peak['terrible'])                                           # Rule 43
        output_sick4.append(old_peak['risk'])                                               # Rule 44
        output_healthy.append(thallium['normal'])                                           # Rule 45
        output_sick1.append(thallium['normal'])                                             # Rule 46
        output_sick2.append(thallium['medium'])                                             # Rule 47
        output_sick3.append(thallium['high'])                                               # Rule 48
        output_sick4.append(thallium['high'])                                               # Rule 49
        output_healthy.append(age['young'])                                                 # Rule 50
        output_sick1.append(age['mild'])                                                    # Rule 51
        output_sick2.append(age['old'])                                                     # Rule 52
        output_sick3.append(age['old'])                                                     # Rule 53
        output_sick4.append(age['very_old'])                                                # Rule 54

        return {'output_sick1': max(output_sick1), 'output_sick2': max(output_sick2),
                'output_sick3': max(output_sick3), 'output_sick4': max(output_sick4),
                'output_healthy': max(output_healthy)}
