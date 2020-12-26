from database.database import DataBase

from actions.add_user import add_user
from actions.delete_user import delete_user
from actions.update_user import update_user

data_base = DataBase()
switch = 0
while switch != 5:
    print(
        """
********************************** WELCOME **********************************

1. Print user/users
2. Add user/users
3. Delete user/users
4. Update user/users
5. Salir
        """
    )

    switch = int(input('Opción (1-5): '))
    print('\n')

    # Print
    if switch == 1:
        data_base.print_user()
    
    # Add
    if switch == 2:
        add_user(data_base)

    # Delete
    if switch == 3:
        delete_user(data_base)

    # Update
    if switch == 4:
        update_user(data_base)
