def solution(cards1, cards2, goal):
    goal_check = goal.copy()

    for i in goal: 
        if cards1 and cards1[0] == i:
            cards1.pop(0)
            goal_check.pop(0)

        elif cards2 and cards2[0] == i:
            cards2.pop(0)
            goal_check.pop(0)

        else:
            return "No"

    return "Yes"

cards1 = ["i", "drink", "water"]	
cards1 = ["i", "water", "drink"]
cards2 = ["want", "to"]	
goal = ["i", "want", "to", "drink", "water"]
solution(cards1, cards2, goal)