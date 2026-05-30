import os
#Предпочтительны пути без кириллицы и без пробелов
save_path= "C:/Users/user/Documents/file.txt" #Убедитсь что использованны знаки '/' для между директориями и файлами, предпочтителен полный путь
save_file = open(save_path,'w+t', encoding="utf-8-sig")
save_file.close()

feature_path = str(input("Путь для features>>"))
feature_path = feature_path.replace('\\','/')

features = []
try:
    for current, dirs, files in os.walk(feature_path):
        for file in files:
            if file[-8:]==".feature":
                features.append(str(os.path.join(current, file)).replace('\\','/'))
except Exception as err:
    print(err)
save_file = open(save_path,'w+t', encoding="utf-8-sig")
for path in features:
    scenarios = []
    with open(path,'r', encoding="utf-8-sig") as feature:
        for line in feature:
            if "Сценарий:" in line.split():
                scenarios.append(line[line.find("Сценарий:")+9:])
    save_file.write(f"{path[len(feature_path):]} сценарии:")
    save_file.write("\n")
    for scene in scenarios:
        save_file.write(f" >>> {scene}")
    save_file.write("\n")
save_file.close()

