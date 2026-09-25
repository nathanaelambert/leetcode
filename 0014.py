def longestCommonPrefix(strs: list[str]) -> str:
    prefix = ""
    for i in range(min([len(s) for s in strs])):
        c = strs[0][i]
        if all(s[i] == c for s in strs):
            prefix += c
        else:
            break
    return prefix

if __name__ == "__main__":
    assert longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
    assert longestCommonPrefix(["dog", "racecar", "car"]) == ""
    assert longestCommonPrefix(["cir", "car"]) == "c"

