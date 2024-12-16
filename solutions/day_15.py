from util.input import get_input_as_string

if __name__ == "__main__":
    input_data = get_input_as_string("inputs/day_15.txt")
    (F1,F2) = input_data.split("\n\n")
    C = [{">":1,"^":-1j,"<":-1,"v":1j}[c] for c in F2.replace("\n", "")]
    def push(i, c, doit):  
        if M[i+c] == "#": val = False
        elif M[i+c] == ".": val = True
        elif c.imag==0 or M[i+c] == "O": val = push(i+c, c, doit)
        elif M[i+c] == "[": val = push(i+c, c, doit) and push(i+1+c, c, doit)
        elif M[i+c] == "]": val = push(i+c, c, doit) and push(i-1+c, c, doit)
        if doit: M[i+c], M[i] = M[i], M[i+c]
        return val

    for part in (0, 1):
        M = {c+1j*r:v for r,l in enumerate(F1.split('\n')) for c,v in enumerate(l.strip())}
        r = next(k for k,v in M.items() if v=="@")
        for c in C:
            if push(r, c, False):
                push(r, c, True)
                r += c

        print(int(sum(k.real + 100*k.imag for k,v in M.items() if v in "[O")))
        F1 = F1.replace("#","##").replace("O", "[]").replace(".", "..").replace("@", "@.")