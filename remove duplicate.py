def remove_duplicates(s):
    myset = set()
    result = []
    for ch in s:
        if ch not in myset:
            myset.add(ch)
            result.append(ch)
    return "".join(result)


print(remove_duplicates("programming"))
print(remove_duplicates("aabbccddeeff")) 
