# this code is for Nonlinesar-Optimization-I_Homework1:Q4
S = [
    (15, 40, 40),
    (20, 40, 40),
    (50, 25, 25),
    (40, 25, 25),
    (15, 37.5, 37.5),
    (15, 15, 65),
    (20, 15, 65),
    (50, 15, 35),
    (40, 15, 35),
    (15, 15, 60)
]

students = [
    (100, 90, 80, 70),   
    (85, 85, 85, 85),    
    (70, 80, 90, 100)    
]

def calculate_score(vertex, student):
    H, M, F = vertex
    C_H, C_M, C_F, C_P = student
    P_weight = 100 - H - M - F 
    return H * C_H + M * C_M + F * C_F + P_weight * C_P

for i, student in enumerate(students, 1):
    max_score = -float('inf')
    optimal_vertex = None
    for vertex in S:
        score = calculate_score(vertex, student)
        if score > max_score:
            max_score = score
            optimal_vertex = vertex

    print(f"Student{i}: ")
    print(f"  Max_Score: {max_score}")
    print(f"  Best_Top(H, M, F): {optimal_vertex}\n")
