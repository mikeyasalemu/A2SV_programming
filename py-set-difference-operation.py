english = input().split()
eng_students = set(input().split())
french = input().split()
fre_students = set(input().split())
result = eng_students - fre_students
print (len(result))
