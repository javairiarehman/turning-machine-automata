def TurningMachineFun(inp):
    print(inp)
    statea = "a"
    stateb = "b"
    statec = "c"
    stateA = "A"
    stateB = "B"
    stateC = "C"
    state = 0
    length = len(inp)
    while True:
        if inp[state] == "a":
            inp=inp[:state] + stateA + inp[state+1:]
            
            print(inp)
            state+=1
            while True:
                if inp[state] == "a":
                    inp=inp[:state] + statea + inp[state+1:]
                elif inp[state] == "B":
                    inp=inp[:state] + stateB + inp[state+1:]
                elif inp[state] == "b":
                    inp=inp[:state] + stateB + inp[state+1:]
                    break
                else:
                    return False
                state+=1
                
            print(inp)
            state+=1
            if inp[state] == "b":
                inp=inp[:state] + stateB + inp[state+1:]
            else:
                return False

            print(inp)
            state+=1
            while True:
                if inp[state] == "b":
                    inp=inp[:state] + stateb + inp[state+1:]
                elif inp[state] == "C":
                    inp=inp[:state] + stateC + inp[state+1:]
                elif inp[state] == "c":
                    inp=inp[:state] + stateC + inp[state+1:]
                    break
                else:
                    return False
                state+=1

            print(inp)
            state+=1
            if inp[state] == "c":
                inp=inp[:state] + stateC + inp[state+1:]
            else:
                return False

            print(inp)
            state+=1
            if inp[state] == "c":
                inp=inp[:state] + stateC + inp[state+1:]
            else:
                return False

            print(inp)
            state-=1
            while True:
                if inp[state] == "C":
                    inp=inp[:state] + stateC + inp[state+1:]
                elif inp[state] == "B":
                    inp=inp[:state] + stateB + inp[state+1:]
                elif inp[state] == "a":
                    inp=inp[:state] + statea + inp[state+1:]
                elif inp[state] == "b":
                    inp=inp[:state] + stateb + inp[state+1:]
                elif inp[state] == "A":
                    inp=inp[:state] + stateA + inp[state+1:]
                    break
                else:
                    return False
                state-=1

            print(inp)
            state+=1
            if inp[state] == "B":
                while True:
                    state+=1
                    if state == length:
                        return True
                    elif inp[state] == "B":
                        inp=inp[:state] + stateB + inp[state+1:]
                    elif inp[state] == "C":
                        inp=inp[:state] + stateC + inp[state+1:]
                    else:
                        return False
        else:
            return False


inp = "aaabbbbbbccccccccc"
out = TurningMachineFun(inp)
if out == False:
    print("False returned")
else:
    print("True returned")
