import os
import sys
#Предпочтительны пути без кириллицы и без пробелов
save_path= "C:/Users/user/Documents/file.txt" #Убедитсь что использованны знаки '/' для между директориями и файлами, предпочтителен полный путь

save_path = sys.argv[1].replace('\\','/')
feature_path = sys.argv[2].replace('\\','/')

if not(os.access(save_path, os.W_OK)):exit("Недостаточно прав для записи в папку", save_path)
if not(os.access(feature_path, os.R_OK)):exit("Недостаточно прав для чтения папки", feature_path)

features = []
try:
    for current, dirs, files in os.walk(feature_path):
        for file in files:
            if file[-8:]==".feature":
                features.append(str(os.path.join(current, file)).replace('\\','/'))
except Exception as err:
    exit(err)
    
with open(save_path,'w+t', encoding="utf-8-sig") as save_file:
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
print("Done!")
