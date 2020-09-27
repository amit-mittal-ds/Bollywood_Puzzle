
def Game():
    import numpy as np
    import pandas as pd

    
    def display(dis):
        t=7+len(dis)
        print('+'*t)
        print("MOVIE: ",end="")
        for x in dis:
            print(x,end="")
        print()
        print('+'*t)
    
    movies = pd.read_csv("https://raw.githubusercontent.com/amitmittal1005/Bollywood_Puzzle/master/bollywood_full_2000-2019.csv")
    row = np.random.randint(0,500)
    name = movies.iloc[row].values[0].lower()
    name = [x for x in name]

    ans = list()
    for x in name:
        if x in ("aeiou0123456789\:!.,&'") :
            ans.append(x)
        elif x == " ":
            ans.append(" ")
        else:
            ans.append("-")
    display(ans)
    
    count = 5
    used = ""
    while(True):
        
        if name == ans:
            e = "\U0001F60A"*5
            print(f"CONGRATULATIONS! You did it {e}")
            break
        
        if count == 0:
            e = "\U0001F611"*5
            print(f"GAME OVER {e}")
            display(name)
            break
            
        print(f"Alphabets used: {used}")    
        print(f"Wrong Attempts Left: {count}")
        
        check = input("Give Input (single alphabet only): ")
        while(check==''):
            check = input("Give Input: ")
        check = check[0].lower()
        
        if (name.count(check) > 0) and (check.upper() not in used):
            #playsound("Sound.mp3")
            used+=check.upper()+" "
            for i,y in enumerate(name):
                if y == check:
                    ans[i] = check
                
            
        elif check.upper() not in used:
            used+="("+check.upper()+")"+" "
            count -= 1
        
        
        display(ans)
        print()