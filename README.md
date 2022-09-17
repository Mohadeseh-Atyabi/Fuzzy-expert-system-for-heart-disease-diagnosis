# Fuzzy-expert-system-for-heart-disease-diagnosis
In this project, our goal is to design a fuzzy expert system to detect whether a person has heart disease. 

## Inputs
The inputs to this problem include the following:

- Blood pressure:
![image](https://user-images.githubusercontent.com/72689599/179025325-0aa9ce04-0b41-4391-88ba-286407666736.png)

- Age:
![image](https://user-images.githubusercontent.com/72689599/179025502-cca407cf-71b8-40de-a013-2f68e19f17f0.png)

- Cholesterol:
![image](https://user-images.githubusercontent.com/72689599/179025615-a118eb0e-a41a-4547-af03-4e20d1ac7922.png)

- Old peak:
![image](https://user-images.githubusercontent.com/72689599/179025722-5c579838-3b2b-4cc6-b403-68543a661e2b.png)

- Blood sugar:
![image](https://user-images.githubusercontent.com/72689599/179025802-f907a0c7-7a70-48b8-b1e8-14c758ffcc39.png)

- ECG: It is a non-invasive test that can detect abnormalities such as arrhythmia, evidence of coronary heart disease, left ventricular hypertrophy and bundle branch blocks.
![image](https://user-images.githubusercontent.com/72689599/179026010-d81db57f-5bfb-4295-81d7-8eb259fa4e17.png)

- Maximum heart rate: This input shows the maximum heart rate of a person during 24 hours.
![image](https://user-images.githubusercontent.com/72689599/179026049-76114fca-7582-4aed-a1e3-3645f9b8fb45.png)

- Sports activity: This input is a crisp input and has only two values zero or one. If it is zero, it means that sports activity is not suitable for the person, and if it is one, it means that there is no obstacle for the person.
- Thallium: This entry specifies the amount of thallium (a chemical element) in a person's body. This input is also a crisp input and takes only three values 3, 6 and 7. If the value of thallium is 3, it is normal, if it is 6, it is average, and if it is 7, it is high.
- Gender: This input is also a crisp input and has only two values zero and one. If it is zero, it means that the patient is male, and if it is one, it means that the patient is female.
- Chest pain: This entry specifies the amount of chest pain. This input is a crisp input and has only four values, one, two, three, or four. If the value is one, it indicates the type of typical angina, if the value is two, it indicates the type of atypical angina, and if the value is three, it indicates anginal pain. non, and if its value is four, it means asymptomatic.
- The output diagram that determines the degree of heart disease is also shown in the figure below:
![image](https://user-images.githubusercontent.com/72689599/179026668-924e609c-687c-4c30-9cc6-6968ef927005.png)

Finally, the output determines whether or not a person has heart disease, which is explained in more detail below.

## Fuzzification
To solve the problem with the help of fuzzy logic, it is necessary to convert our values from absolute to fuzzy (imprecise, relative). This stage is called Fuzzification. For this purpose, fuzzy sets should be defined and according to the membership function, the membership of each value to the set should be calculated. For this purpose, we use the membership functions of the required sets that we have defined in the input. For inputs such as sports activity, gender, and thallium, as explained above, since they only have crisp values, the chart is not given, but they should be included in the project.

## Inference
In the next step, it is necessary to check the obtained fuzzy values in the existing rules to solve the problem. This stage is called Inference. For example, consider the following rules:
```
If (age is old) and (blood pressure is very high) then (result is sick(s4))
If (cholesterol is low) and (blood pressure is low) then (result is health)
If (blood pressure is high) and (max heart rate is medium) then (result is sick (s2))
```

As you know, in fuzzy logic, there are different methods for calculating community and sharing operators. Here we use the maximum and minimum method. As a result, AND=min and OR=max. With the help of the above statements, the following expressions are obtained:
```
Membership(sick(s4)) = min(0.6, 0.7) = 0.6
Membership(healthy) = min(0.6, 0) = 0
Membership(sick(s2)) = min(0.7, 0.5) = 0.5
```

This stage obtains the output which is the same as different disease degrees with different belonging values.

## Defuzzification
The last step is called Defuzzification. At this stage, we return to the world of absolute values with the help of repeated deductions to obtain the answer in the form of absolute values. There are also different methods for dephasing, one of the most important and widely used of which is the center of mass method. Please note that in some cases, more than 2 rules may be activated and may belong to several sets of values. In these cases, we must combine the obtained answers. For this, we OR all the answers together, or in other words, we get the Max output of all the rules. After combining the answers of all the rules, we get the center of mass of the resulting figure.
To calculate the center of mass, we use the following formula:

![image](https://user-images.githubusercontent.com/72689599/179029542-556480e1-1266-422c-b8b2-d7d9d570715f.png)

## How to run the project
To install the requirements and used libraries, first enter the main directory and then install the requirements using the command below.
```
pip install -r requirements.txt
```
In the [app.py](app.py) file, the server is running on port 8448 and you should not change this file. Also, in the [final_result.py](final_result.py) file, in the get_final_result method, a dictionary of the parameters in the problem is given to you in its input, and you must use this dictionary. Also, at the end, you must return the final result (health status), which must be of string type, in the get_final_result method.


