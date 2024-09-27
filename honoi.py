def TowerofHonoi(n,source,destination,auxiliary):
    if n==1:
        print("move disk 1 from source ",source," to destination ",destination)
        return
    TowerofHonoi(n-1,source,auxiliary,destination)
    print("move disk",n,"from source ",source," to destination ",destination)
    TowerofHonoi(n-1,auxiliary,destination,source)
n=3
TowerofHonoi(n,'A','B','C')