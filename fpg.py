import os
import sys
#Предпочтительны пути без кириллицы и без пробелов

save_path = sys.argv[1].replace('\\','/')
feature_path = sys.argv[2].replace('\\','/')

features = []
try:
    for current, dirs, files in os.walk(feature_path):
        for file in files:
            if file[-8:]==".feature":
                features.append(str(os.path.join(current, file)).replace('\\','/'))
except FileNotFoundError:
    exit("Недостаточно прав для чтения папки "+feature_path)
except Exception as err:
    exit(err)

try:    
    with open(save_path,'w+t', encoding="utf-8-sig") as save_file:
        for path in features:
            scenarios = []
            with open(path,'r', encoding="utf-8-sig") as feature:
                for line in feature:
                    if "Сценарий:" in line.split():
                        scenarios.append(line[line.find("Сценарий:")+9:line.find("Дано ")])
            save_file.write(f"{path[len(feature_path):]} сценарии:")
            save_file.write("\n")
            for scene in scenarios:
                save_file.write(f" >>> {scene}")
                save_file.write("\n")
except PermissionError:
    exit("Недостаточно прав для записи в папку "+save_path)
print("Done!")
