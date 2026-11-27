import math

seqs = ["AGTCTA", "GTCAAG", "TCTAGC", "ACATCC", "GTCAAT"]
letters = "ACGT"
n = len(seqs)
L = len(seqs[0])

pfm = {b: [sum(s[i] == b for s in seqs) for i in range(L)] for b in letters}
pwm = {b: [c / n for c in pfm[b]] for b in letters}
ps = 0.01
llm = {b: [math.log(((c + ps) / (n + 4 * ps)) / 0.25) for c in pfm[b]] for b in letters}

def show(name, m):
    print(name)
    print("   " + "".join(f"{i:>8}" for i in range(1, L + 1)))
    for b in letters:
        print(f"{b:<3}" + "".join(f"{v:>8.2f}" if isinstance(v, float) else f"{v:>8}" for v in m[b]))
    print()


show("PFM", pfm)
show("PWM", pwm)
show("LLM", llm)

S = "ACTGCTGACA"
for k in range(len(S) - L + 1):
    w = S[k:k + L]
    print(f"Sw{k + 1} = {w} = {sum(llm[b][i] for i, b in enumerate(w)):.2f}")
