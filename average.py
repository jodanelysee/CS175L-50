def main ():
    s1,s2,s3,s4,s5 = inputScores()
    avg = computeAverage(s1,s2,s3,s4,s5)
    letters = determineGrade(s1,s2,s3,s4,s5)
    #determineGrade(s1,s2,s3,s4,s5)
    outputResults(avg)

def inputScores():
    total = 0
    count = 0
    score1 = int(input('Enter test score 1: '))
    total = total + score1
    count = count + 1
    score2 = int(input('Enter test score 2: '))
    total = total +score2
    count = count + 1
    score3 = int(input('Enter test score 3: '))
    total = total + score3
    count = count + 1
    score4 = int(input('Enter test score 4: '))
    total = total + score4
    count = count + 1
    score5 = int(input('Enter test score 5: '))
    print()
    total = total + score5
    count = count + 1
    return score1,score2,score3,score4,score5

def determineGrade(s1,s2,s3,s4,s5):
    STR_S1 = 'Score 1:'
    STR_S2 = 'Score 2:'
    STR_S3 = 'Score 3:'
    STR_S4 = 'Score 4:'
    STR_S5 = 'Score 5:'
    STR_A = 'A'
    STR_B = 'B'
    STR_C = 'C'
    STR_D = 'D'
    STR_F = 'F'
    print('Score\t\tNumeric Grade\t\tLetter Grade')
    print('---------------------------------------------------------------------')
    if s1 >= 100:
        print('Score 1: ',f' {s1:>35}', f'{STR_A:>51}')
    elif s1 >= 90 and s1 < 100:
        print('Score 1: ',f'{s1:>35}', f'{STR_A:>52}')
    elif s1 >= 80 and s1 < 90:
        print('Score 1: ',f'{s1:>35}', f'{STR_B:>52}')
    elif s1 >= 70 and s1 < 80:
        print('Score 1: ',f'{s1:>35}', f'{STR_C:>52}')
    elif s1 >= 60 and s1 < 70:
        print('Score 1: ' ,f'{s1:>35}', f'{STR_D:>52}')
    elif s1 < 10:
        print('Score 1: ',f' {s1:>35}', f'{STR_F:>54}')
    else:
        print('Score 1: ',f'{s1:>35}', f'{STR_F:>52}')
    if s2 >= 100:
        print('Score 2: ',f' {s2:>35}', f'{STR_A:>51}')
    elif s2 >= 90 and s2 < 100:
        print('Score 2: ',f'{s2:>35}', f'{STR_A:>52}')
    elif s2 >= 80 and s2 < 90:
        print('Score 2: ',f'{s2:>35}', f'{STR_B:>52}')
    elif s2 >= 70 and s2 < 80:
        print('Score 2: ',f'{s2:>35}', f'{STR_C:>52}')
    elif s2 >= 60 and s2 < 70:
        print('Score 2: ' ,f'{s2:>35}', f'{STR_D:>52}')
    elif s2 < 10:
        print('Score 2: ',f' {s2:>35}', f'{STR_F:>54}')
    else:
        print('Score 2: ',f'{s2:>35}', f'{STR_F:>52}')
    if s3 >= 100:
        print('Score 3: ',f' {s3:>35}', f'{STR_A:>51}')
    elif s3 >= 90 and s3 < 100:
        print('Score 3: ',f'{s3:>35}', f'{STR_A:>52}')
    elif s3 >= 80 and s3 < 90:
        print('Score 3: ',f'{s3:>35}', f'{STR_B:>52}')
    elif s3 >= 70 and s3 < 80:
        print('Score 3: ',f'{s3:>35}', f'{STR_C:>52}')
    elif s3 >= 60 and s3 < 70:
        print('Score 3: ' ,f'{s3:>35}', f'{STR_D:>52}')
    elif s3 < 10:
        print('Score 3: ',f' {s3:>35}', f'{STR_F:>54}')
    else:
        print('Score 3: ',f'{s4:>35}', f'{STR_F:>52}')
    if s4 >= 100:
        print('Score 4: ',f' {s4:>35}', f'{STR_A:>51}')
    elif s4 >= 90 and s4 < 100:
        print('Score 4: ',f'{s4:>35}', f'{STR_A:>52}')
    elif s4 >= 80 and s4 < 90:
        print('Score 4: ',f'{s4:>35}', f'{STR_B:>52}')
    elif s4 >= 70 and s4 < 80:
        print('Score 4: ',f'{s4:>35}', f'{STR_C:>52}')
    elif s4 >= 60 and s4 < 70:
        print('Score 4: ' ,f'{s4:>35}', f'{STR_D:>52}')
    elif s4 < 10:
        print('Score 4: ',f' {s4:>35}', f'{STR_F:>54}')
    else:
        print('Score 4: ',f'{s4:>35}', f'{STR_F:>52}')
    if s5 >=100:
        print('Score 5: ',f' {s5:>35}', f'{STR_A:>51}')
    elif s5 >= 90 and s5 < 100:
        print('Score 5: ',f'{s5:>35}', f'{STR_A:>52}')
    elif s5 >= 80 and s5 < 90:
        print('Score 5: ',f'{s5:>35}', f'{STR_B:>52}')
    elif s5 >= 70 and s5 < 80:
        print('Score 5: ',f'{s5:>35}', f'{STR_C:>52}')
    elif s5 >= 60 and s5 < 70:
        print('Score 5: ' ,f'{s5:>35}', f'{STR_D:>52}')
    elif s5 < 10:
        print('Score 5: ',f' {s5:>35}', f'{STR_F:>54}')
    else:
        print('Score 5: ',f'{s5:>35}', f'{STR_F:>52}')
        
def computeAverage(s1,s2,s3,s4,s5):
    return (s1+s2+s3+s4+s5)/(5)

def outputResults(avg):
    STR_A1 = 'A'
    STR_B1 = 'B'
    STR_C1 = 'C'
    STR_D1 = 'D'
    STR_F1 = 'F'
    if avg > 90:
        print('Average Score: ',f'{avg:>25}', f'{STR_A1:>49}')
    elif avg >= 80 and avg < 90:
        print('Average Score: ',f'{avg:>25}', f'{STR_B1:>49}')
    elif avg >= 70 and avg < 80:
        print('Average Score: ',f'{avg:>25}', f'{STR_C1:>49}')
    elif avg >= 60 and avg < 70:
        print('Average Score: ',f'{avg:>25}', f'{STR_D1:>49}')
    elif avg < 10:
        print('Average Score: ',f'{avg:>25}', f'{STR_F1:>51}')
    else:
        print('Average Score: ',f'{avg:>25}', f'{STR_F1:>49}')

    #print('average = ',avg)

main()
