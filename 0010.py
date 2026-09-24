def isMatch(s: str, p: str) -> bool:
    ellipse = len(p) >= 2 and p[1] == "*"
    wildcard = len(p) >= 1 and p[0] == "."
    if ellipse:
        if len(s) == 0:
            return isMatch(s, compress(p[2:]))
        possibilities = []
        possibilities.append(isMatch(s, compress(p[2:])))
        if wildcard or s[0] == p[0]:
            possibilities.append(isMatch(s[1:], compress(p[2:])))
            possibilities.append(isMatch(s[1:], p))
        return any(possibilities)
    else:
        if len(s) == 0:
            return len(p) == 0
        if len(p) == 0:
            return False
        if wildcard:
            return isMatch(s[1:], compress(p[1:]))
        if s[0] == p[0]:
            return isMatch(s[1:], p[1:])
        return False

def compress(p: str) -> str: 
    ellipse1 = len(p) >= 2 and p[1] == "*"
    ellipse2 = len(p) >= 4 and p[3] == "*"
    if not (ellipse1 and ellipse2):
        return p
    if p[0] == "." or p[2] == ".":
        return ".*" + p[4:]
    if p[0] == p[2]:
        return p[2:]
    return p

if __name__ == "__main__":
    assert isMatch("aa", "a") is False
    assert isMatch("aa", "a*") is True
    assert isMatch("ab", ".*") is True
    assert isMatch("a", "ab*") is True
    assert isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*b") is True