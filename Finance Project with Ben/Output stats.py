def decrypt(word):
    alphabet_num = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12, "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26}
    num_alphabet = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H", 9: "I", 10: "J", 11: "K", 12: "L", 13: "M", 14: "N", 15: "O", 16: "P", 17: "Q", 18: "R", 19: "S", 20: "T", 21: "U", 22: "V", 23: "W", 24: "X", 25: "Y", 26: "Z"}    
    kachig = 11
    encodedList = []
    for i in range(len(word)):
        n = alphabet_num.get(word[i])
        n -= kachig
        if kachig == 11:
            kachig = 1
        elif kachig == 1:
            kachig = 3
        elif kachig == 3:
            kachig = 8
        elif kachig == 8:
            kachig = 9
        elif kachig == 9:
            kachig = 7
        elif kachig == 7:
            kachig = 12
        elif kachig == 12:
            kachig = 22
        elif kachig == 22:
            kachig = 4
        elif kachig == 4:
            kachig = 19
        elif kachig == 19:
            kachig = 10
        elif kachig == 10:
            kachig = 2
        elif kachig == 2:
            kachig = 24
        elif kachig == 24:
            kachig = 15
        elif kachig == 15:
            kachig = 5
        elif kachig == 5:
            kachig = 16
        elif kachig == 16:
            kachig = 21
        elif kachig == 21:
            kachig = 6
        elif kachig == 6:
            kachig = 13
        elif kachig == 13:
            kachig = 23
        elif kachig == 23:
            kachig = 14
        elif kachig == 14:
            kachig = 17
        elif kachig == 17:
            kachig = 18
        elif kachig == 18:
            kachig = 20
        elif kachig == 20:
            kachig = 11 
        letter = num_alphabet.get(n, "NO")
        if letter == "NO":
            n = n + 26
            letter = num_alphabet.get(n, "Oops")
        encodedList.append(letter)
    sentence1 = ""
    for i in range(len(word)):
        sentence1 += encodedList[i]
    return sentence1
    

file = open('Name, County, and Salary.txt','r')
everything = file.read().splitlines()
file.close()
everything.pop(0)
names = []
salarys = []
counties = []
salaryandcounty = []
for i in range(len(everything)):
    if (i + 2) % 2 == 0:
        names.append(decrypt(everything[i]))
    else:
        salaryandcounty.append(everything[i])
for i in range(len(salaryandcounty)):
    salaryandcounty[i] = salaryandcounty[i].split()
    salarys.append(salaryandcounty[i][1])
    salarys[i] = (float(salarys[i]) / 8) * 2
    counties.append(decrypt(salaryandcounty[i][0]))

warwickshire_salaries = []
oxfordshire_salaries = []
surrey_salaries = []
shropshire_salaries = []
northumberland_salaries = []
cumbria_salaries = []
lancashire_salaries = []
tyneandwear_salaries = []
westsussex_salaries = []
durham_salaries = []
yorkshire_salaries = []
mersey_salaries = []
eastsussex_salaries = []
greatermanchester_salaries = []
lincolnshire_salaries = []
norfolk_salaries = []
buckinghamshire_salaries = []
bedfordshire_salaries = []
cityoflondon_salaries = []
cheshire_salaries = []
derbyshire_salaries = []
nottinghamshire_salaries = []
leicestershire_salaries = []
staffordshire_salaries = []
westmidlands_salaries = []
bristol_salaries = []
greaterlondon_salaries = []
rutland_salaries = []
suffolk_salaries = []
essex_salaries = []
worcestershire_salaries = []
cambridgeshire_salaries = []
gloucestershire_salaries = []
northamptonshire_salaries = []
hertfordshire_salaries = []
sommerset_salaries = []
devon_salaries = []
cornwall_salaries = []
isleofwight_salaries = []
dorset_salaries = []
wiltshire_salaries = []
kent_salaries = []
hampshire_salaries = []
berkshire_salaries = []
for i in range(len(counties)):
    if counties[i] == "WARWICKSHIRE":
        warwickshire_salaries.append(salarys[i])
        warwickshire_mean = sum(warwickshire_salaries) / len(warwickshire_salaries)
        print("Warwickshires salarys are:" ,warwickshire_salaries)
    elif counties[i] == "SHROPSHIRE":
        shropshire_salaries.append(salarys[i])
        shropshire_mean = sum(shropshire_salaries) / len(shropshire_salaries)
        print("Shropshires salarys are:" ,shropshire_salaries)
    elif counties[i] == "NORTHUMBERLAND":
        northumberland_salaries.append(salarys[i])
        northumberland_mean = sum(northumberland_salaries) / len(northumberland_salaries)
        print("Northumberlands salarys are:" ,northumberland_salaries)
    elif counties[i] == "CUMBRIA":
        cumbria_salaries.append(salarys[i])
        cumbria_mean = sum(cumbria_salaries) / len(cumbria_salaries)
        print("Cumbrias salarys are:" ,cumbria_salaries)
    elif counties[i] == "LANCASHIRE":
        lancashire_salaries.append(salarys[i])
        lancashire_mean = sum(lancashire_salaries) / len(lancashire_salaries)
        print("Lancashires salarys are:" ,lancashire_salaries)
    elif counties[i] == "TYNEANDWEAR":
        tyneandwear_salaries.append(salarys[i])
        tyneandwear_mean = sum(tyneandwear_salaries) / len(tyneandwear_salaries)
        print("Tyne and Wear salarys are:" ,tyneandwear_salaries)
    elif counties[i] == "DURHAM":
        durham_salaries.append(salarys[i])
        durham_mean = sum(durham_salaries) / len(durham_salaries)
        print("Durham salarys are:" ,durham_salaries)
    elif counties[i] == "YORKSHIRE":
        yorkshire_salaries.append(salarys[i])
        yorkshire_mean = sum(yorkshire_salaries) / len(yorkshire_salaries)
        print("Yorkshires salarys are:" ,yorkshire_salaries)
    elif counties[i] == "MERSEY":
        mersey_salaries.append(salarys[i])
        mersey_mean = sum(mersey_salaries) / len(mersey_salaries)
        print("Merseys salarys are:" ,mersey_salaries)
    elif counties[i] == "GREATERMANCHESTER":
        greatermanchester_salaries.append(salarys[i])
        greatermanchester_mean = sum(greatermanchester_salaries) / len(greatermanchester_salaries)
        print("Greater Manchester salarys are:" ,greatermanchester_salaries)
    elif counties[i] == "LINCOLNSHIRE":
        lincolnshire_salaries.append(salarys[i])
        lincolnshire_mean = sum(lincolnshire_salaries) / len(lincolnshire_salaries)
        print("Lincolnshires salarys are:" ,lincolnshire_salaries)
    elif counties[i] == "CHESHIRE":
        cheshire_salaries.append(salarys[i])
        cheshire_mean = sum(cheshire_salaries) / len(cheshire_salaries)
        print("Cheshires salarys are:" ,cheshire_salaries)
    elif counties[i] == "DERBYSHIRE":
        derbyshire_salaries.append(salarys[i])
        derbyshire_mean = sum(derbyshire_salaries) / len(derbyshire_salaries)
        print("Derbyshires salarys are:" ,derbyshire_salaries)
    elif counties[i] == "NOTTINGHAMSHIRE":
        nottinghamshire_salaries.append(salarys[i])
        nottinghamshire_mean = sum(nottinghamshire_salaries) / len(nottinghamshire_salaries)
        print("Nottinghamshires salarys are:" ,nottinghamshire_salaries)
    elif counties[i] == "STAFFORDSHIRE":
        staffordshire_salaries.append(salarys[i])
        staffordshire_mean = sum(staffordshire_salaries) / len(staffordshire_salaries)
        print("Staffordshires salarys are:" ,staffordshire_salaries)
    elif counties[i] == "WESTMIDLANDS":
        westmidlands_salaries.append(salarys[i])
        westmidlands_mean = sum(westmidlands_salaries) / len(westmidlands_salaries)
        print("West Midlands salarys are:" ,westmidlands_salaries)
    elif counties[i] == "LEICESTERSHIRE":
        leicestershire_salaries.append(salarys[i])
        leicestershire_mean = sum(leicestershire_salaries) / len(leicestershire_salaries)
        print("Leicestershires salarys are:" ,leicestershire_salaries)
    elif counties[i] == "RUTLAND":
        rutland_salaries.append(salarys[i])
        rutland_mean = sum(rutland_salaries) / len(rutland_salaries)
        print("Rutland salarys are:" ,rutland_salaries)
    elif counties[i] == "NORTHAMPTONSHIRE":
        northamptonshire_salaries.append(salarys[i])
        northamptonshire_mean = sum(northamptonshire_salaries) / len(northamptonshire_salaries)
        print("Northamptonshires salarys are:" ,northamptonshire_salaries)
    elif counties[i] == "CAMBRIDGESHIRE":
        cambridgeshire_salaries.append(salarys[i])
        cambridgeshire_mean = sum(cambridgeshire_salaries) / len(cambridgeshire_salaries)
        print("Cambridgeshires salarys are:" ,cambridgeshire_salaries)
    elif counties[i] == "NORFOLK":
        norfolk_salaries.append(salarys[i])
        norfolk_mean = sum(norfolk_salaries) / len(norfolk_salaries)
        print("Norfolks salarys are:" ,norfolk_salaries)
    elif counties[i] == "SUFFOLK":
        suffolk_salaries.append(salarys[i])
        suffolk_mean = sum(suffolk_salaries) / len(suffolk_salaries)
        print("Sufforks salarys are:" ,suffolks_salaries)
    elif counties[i] == "ESSEX":
        essex_salaries.append(salarys[i])
        essex_mean = sum(essex_salaries) / len(essex_salaries)
        print("Essexs salarys are:" ,essex_salaries)
    elif counties[i] == "HERTFORDSHIRE":
        hertfordshire_salaries.append(salarys[i])
        hertfordshire_mean = sum(hertfordshire_salaries) / len(hertfordshire_salaries)
        print("Hertfordshires salarys are:" ,hertfordshire_salaries)
    elif counties[i] == "BEDFORDSHIRE":
        bedfordshire_salaries.append(salarys[i])
        bedfordshire_mean = sum(bedfordshire_salaries) / len(bedfordshire_salaries)
        print("Bedfordshires salarys are:" ,bedfordshire_salaries)
    elif counties[i] == "BUCKINGHAMSHIRE":
        buckinghamshire_salaries.append(salarys[i])
        buckinghamshire_mean = sum(buckinghamshire_salaries) / len(buckinghamshire_salaries)
        print("Buckinghamshires salarys are:" ,buckinghamshire_salaries)
    elif counties[i] == "OXFORDSHIRE":
        oxfordshire_salaries.append(salarys[i])
        oxfordshire_mean = sum(oxfordshire_salaries) / len(oxfordshire_salaries)
        print("Oxfordshires salarys are:" ,oxfordshire_salaries)
    elif counties[i] == "GLOUCESTERSHIRE":
        gloucestershire_salaries.append(salarys[i])
        gloucestershire_mean = sum(gloucestershire_salaries) / len(gloucestershire_salaries)
        print("Gloucestershires salarys are:" ,gloucestershire_salaries)
    elif counties[i] == "WORCESTERSHIRE":
        worcestershire_salaries.append(salarys[i])
        worcestershire_mean = sum(worcestershire_salaries) / len(worcestershire_salaries)
        print("Worcestershires salarys are:" ,worcestershire_salaries)
    elif counties[i] == "HEREFORDSHIRE":
        herefordshire_salaries.append(salarys[i])
        herefordshire_mean = sum(herefordshire_salaries) / len(herefordshire_salaries)
        print("Herefordshires salarys are:" ,herefordshire_salaries)
    elif counties[i] == "BRISTOL":
        bristol_salaries.append(salarys[i])
        bristol_mean = sum(bristol_salaries) / len(bristol_salaries)
        print("Bristols salarys are:" ,bristol_salaries)
    elif counties[i] == "SOMMERSET":
        sommerset_salaries.append(salarys[i])
        sommerset_mean = sum(sommerset_salaries) / len(sommerset_salaries)
        print("Sommersets salarys are:" ,sommerset_salaries)
    elif counties[i] == "DEVON":
        devon_salaries.append(salarys[i])
        devon_mean = sum(devon_salaries) / len(devon_salaries)
        print("Devons salarys are:" ,devon_salaries)
    elif counties[i] == "CORNWALL":
        cornwall_salaries.append(salarys[i])
        cornwall_mean = sum(cornwall_salaries) / len(cornwall_salaries)
        print("Cornwalls salarys are:" ,cornwall_salaries)
    elif counties[i] == "DORSET":
        dorset_salaries.append(salarys[i])
        dorset_mean = sum(dorset_salaries) / len(dorset_salaries)
        print("Dorsets salarys are:" ,dorset_salaries)
    elif counties[i] == "WILTSHIRE":
        wiltshire_salaries.append(salarys[i])
        wiltshire_mean = sum(wiltshire_salaries) / len(wiltshire_salaries)
        print("Wiltshires salarys are:" ,wiltshire_salaries)
    elif counties[i] == "HAMPSHIRE":
        hampshire_salaries.append(salarys[i])
        hampshire_mean = sum(hampshire_salaries) / len(hampshire_salaries)
        print("Hampshires salarys are:" ,hampshire_salaries)
    elif counties[i] == "ISLEOFWIGHT":
        isleofwight_salaries.append(salarys[i])
        isleofwight_mean = sum(isleofwight_salaries) / len(isleofwight_salaries)
        print("Isle of Wights salarys are:" ,isleofwight_salaries)
    elif counties[i] == "BERKSHIRE":
        berkshire_salaries.append(salarys[i])
        berkshire_mean = sum(berkshire_salaries) / len(berkshire_salaries)
        print("Berkshires salarys are:" ,berkshire_salaries)
    elif counties[i] == "SURREY":
        surrey_salaries.append(salarys[i])
        surrey_mean = sum(surrey_salaries) / len(surrey_salaries)
        print("Surreys salarys are:" ,surrey_salaries)
    elif counties[i] == "GREATERLONDON":
        greaterlondon_salaries.append(salarys[i])
        greaterlondon_mean = sum(greaterlondon_salaries) / len(greaterlondon_salaries)
        print("Greater Londons salarys are:" ,greaterlondon_salaries)
    elif counties[i] == "CITYOFLONDON":
        cityoflondon_salaries.append(salarys[i])
        cityoflondon_mean = sum(cityoflondon_salaries) / len(cityoflodon_salaries)
        print("City of Londons salarys are:" ,cityoflondon_salaries)
    elif counties[i] == "WESTSUSSEX":
        westsussex_salaries.append(salarys[i])
        westsussex_mean = sum(westsussex_salaries) / len(westsussex_salaries)
        print("West Sussexs salarys are:" ,westsussex_salaries)
    elif counties[i] == "EASTSUSSEX":
        eastsussex_salaries.append(salarys[i])
        eastsussex_mean = sum(eastsussex_salaries) / len(eastsussex_salaries)
        print("East Sussexs salarys are:" ,eastsussex_salaries)
    elif counties[i] == "KENT":
        kent_salaries.append(salarys[i])
        kent_mean = sum(kent_salaries) / len(kent_salaries)
        print("Kents salarys are:" ,kent_salaries)
    else:
        print("Invalid County")
        other_salaries = []
        other_salaries.append(salarys[i])
    
