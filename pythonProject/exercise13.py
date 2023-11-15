list1=[1,1,1]
list2=[1,1,1]
list3=[1,1,1]
final_list=[list1, list2, list3]
print(final_list)
row_position=int(input("enter the row position:"))
row_position -= 1
print(row_position)
column_position=int(input("enter the column position:"))
column_position -= 1
print(column_position)
final_list[row_position][column_position]="x"
print(f"{list1}\n{list2}\n{list3}")
