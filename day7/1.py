d = {
    1: "AEILNORSTU",
    2: "DG",
    3: "BCMP",
    4: "FHVWY",
    5: "K",
    8: "JX",
    10: "QZ"
}
sum = 0
word = input().upper()
for i in word:
    for j in d:
        if i in d[j]:
            sum+=j
            break
print(sum)
