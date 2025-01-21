
import pandas as pd

data = {
    'id': [1,2,3,4,5],
    'sex': ['male', 'female','female','male','female'],
    'math': [80, 74, 89, 90, 97],
    'read': [60, 90, 96, 89, 92]
}
print(data)

grades = pd.DataFrame(data)

print(grades)

grades

grades.id
grades.read(sum)
data['id']
data['read']
