from logic import *

def main():
    p = Atom("Está chovendo")
    q = Atom("A rua está molhendo")
    p.value = True
    q.value = False
    p_and_q = THEN(p, q)
    not_p_and_q = NOT(p_and_q)
    print(repr(p_and_q))
    print(p_and_q.value)
    print(repr(not_p_and_q))

if __name__ == "__main__":
    main()