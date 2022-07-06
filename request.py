
import requests

url = 'http://localhost:5000/predict_api'
output1 = requests.post(url,json={'cloud': 4000, 'furniture': 40000, 'equipment': 140000, 'software': 4000, 'salary_hr':2000,'length': 400, 'study_material_cost': 1500, 'rent': 90000, 'electricity': 16000, 'maintainance': 1500,'marketing': 2000, 'certification': 1, 'placement': 1})

print(output1.json())
