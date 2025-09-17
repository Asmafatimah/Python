fruit_type=input('enter the fruit type').strip().title()
if  fruit_type== 'Oranges':
    print('oranges are 50rs per kilogram')
elif fruit_type=="Apples":
    print('Apples are 120rs per kilogram')
elif fruit_type=="Bananas":
    print('Bananas are 40rs per kilogram')
elif fruit_type=="Cherries":
    print( 'Bananas are 40rs per kilogram')
else:
    print(f"sorry,we are out of {fruit_type}")
    
    
    
