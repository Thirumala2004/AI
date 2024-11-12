def solve_nqueens(n):
    def solve(queens, xy_diff, xy_sum, p):
        if p == n:
            result.append(queens)
            return
        for q in range(n):
            if q not in queens and (p - q) not in xy_diff and (p + q) not in xy_sum:
                solve(queens + [q], xy_diff + [p - q], xy_sum + [p + q], p + 1)

    result = []
    solve([], [], [], 0)
    return [['- ' * i + 'Q ' + '- ' * (n - i - 1) for i in sol] for sol in result]

n = int(input("Enter number of queens: "))
solutions = solve_nqueens(n)
print("Solutions:")
for solution in solutions:
    print("* * * * * * *")
    for row in solution:
        print(row)
    print()
