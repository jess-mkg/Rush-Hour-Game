from tools import structure_boards
from tools import Tools
from tools import visual_board
from tools import welcome
import time



def get_solutions(lines):
    sols = []
    phrase = 'Sol:'
    end = '.' 
    lineNum = 0        
    for line in lines:                              #reads each line
        if phrase in line:                          #if 'Sol:' appears in a line the algo will preform some steps to append the solution to a list
            sol = line
            loopCount = 1
            while end not in sol:
                nex = lines[lineNum + loopCount]
                new = sol + nex
                sol = new
                loopCount +=1
            arrsol = sol.split()
            del arrsol[0]
            del arrsol[(len(arrsol)-1)]
            sols.append(arrsol)
        lineNum += 1
    return sols

def print_res(res):
    if res[2] == "SOLVED":
        print("Algorithm: " + res[0])
        print("Card Number: " + str(res[1]))
        print("Status: " + res[2])
        visual_board(res[3])
        print(res[4])
        visual_board(res[5])
        print(res[6])
        print("Depth: " + str(res[7]))
        print("Nodes: " + str(res[8]))
        print("Different in Sol Lenth: " + str(res[9]))
        print("Time: " + str(res[10]))
        print("Accuracy: " + str(res[11]))
        print("\n")
    
    elif res[2] == "FAILED":
        print("Algorithm: " + res[0])
        print("Card Number: " + str(res[1]))
        print("Status: " + res[2])
        visual_board(res[3])
        print(res[4])
        
        print("Depth: " + str(res[7]))
        print("Nodes: " + str(res[8]))
        print("Time: " + str(res[10]))
        print("\n")


if __name__ == "__main__":

    file = open('rh.txt', 'r')
    lines = file.readlines()
    boards = lines[4:44]
    b_sols = get_solutions(lines)
    s_boards = structure_boards(boards)
    op, start, end = welcome()
    res = 0
    f = False

    if start == 0 and end == 40:
        f = True
        filename = input("please give a file name with the .txt: ")
        file = open(filename, 'w')
        print("loading ... ")


    s = time.time()
    for i in range(start, end):
        
        t = Tools()
        if op == "BFS":
            res = t.BFS(i, s_boards, b_sols)     #Breath First Search
        if op == "ID":
            res = t.ID(i, s_boards, b_sols, limit = 1)   #depth limited DFS
        if op == "A1":
            res = t.H1AStar(i, s_boards, b_sols)
        if op == "A2":
            res = t.H2AStar(i, s_boards, b_sols)
        if op == "HC": 
            res = t.HCStart(i, s_boards, b_sols)
        if op == "SA":
            res = t.SAStart(i, s_boards, b_sols)
        
        if not f:
                print_res(res)

        if f: 
            for i in range (0, len(res)):
                if i == 7:
                    file.write("Depth: " + (str(res[7])) + "\n")
                if i == 8:
                    file.write("Nodes: " + (str(res[8])) + "\n")
                if i == 9:
                    file.write("Difference: " + (str(res[9])) + "\n")
                if i == 10:
                    file.write("Time: " + (str(res[10])) + "\n")
                if i == 11:
                    file.write("Accuracy: " + (str(res[11])) + "\n")
                else:   
                    file.write(str(res[i]) + "\n")
            file.write("\n")
    e = time.time()
    
    if f:
        file.close()
        print("Done!")
    
    print("Total Time: " + (str(e-s)))

