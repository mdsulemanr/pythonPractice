def guassian_elemination(a):
    ans=[]
    row=0
    while row < len(a):
        ans.append([]) # iterating each element of given matrix at the same time creating another matrix of equalent order
        col=0
        while col<len(a[row]):
            if row==0:
                ans[0].append(a[0][col]/a[0][0])      #making first row and first col element to unity
            elif row==1:
                ans[1].append(a[1][col]/a[1][0])      #making second row and first col element to unity
                ans[1][col] = ans[1][col] - ans[0][col]  # making second row and first col element to zero
            elif row==2:
                ans[2].append(a[2][col]/a[2][0])      #making third row and first col element to unity
                ans[2][col] = ans[2][col] - ans[0][col]  # making third row and first col element to zero
            else:
                ans[row].append(a[row][col])
            col+=1
        row+=1
    print(ans)

    row=0
    temp=ans[1][1]
    temp1=ans[2][2]
    while row < len(ans):
        col = 0
        while col < len(ans[row]):
            if row == 1:
                ans[1][col] = ans[1][col]/temp      #making second element of second row to unity
            if row == 2:
                ans[2][col] = ans[2][col]/temp1     #making second element of third row to unity
                ans[2][col] = ans[2][col] - ans[1][col]  # making second element of second row to zero
            col += 1
        row += 1
    print(ans)

    row=0
    temp2=ans[2][2]
    while row < len(ans):
        col = 0
        while col < len(ans[row]):
            if row == 2:
                ans[2][col] = ans[2][col]/temp2     #making second element of third row to unity
            col += 1
        row += 1

    print(ans)
    z=ans[2][3]       #putting values in equations
    y=(ans[1][3]-(ans[1][2]*z))/ans[1][1]
    x=(ans[0][3]-(ans[0][1]*y+ans[0][2]*z))/ans[0][0]
    print(x, y, z)



a=[[4, 1, -1, 12],
   [1, 3, 1, 18],
   [2, -1, -2, -3]]
print(guassian_elemination(a))