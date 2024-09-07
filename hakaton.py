employers = {
    "Курпешко": {
        "Посада": "Data analyst",
        "KE": 11,
        "проекти": ["Mail list clasterisation",]
    },
    "Миша":{
        "Посада": "програмист",
        "KE": 8,
        "проекти": ["гугл сайти","Мини игри"]
    },
    "Кирил":{
        "Посада": "тестер",
        "KE": 9,
        "проекти": ["проверка програл","помощь програмисту"]
    }
}

print(employers)
print("Наші працівники")
for e in employers.keys():
    print("-",e)

for e in employers.keys():
    print("-",employers[e]["Посада"])
