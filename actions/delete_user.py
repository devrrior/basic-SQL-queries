def delete_user(data_base):

    data = ()
    many = None
    validation = False

    while validation == False:

        option = input('Do you wish delete more than one user? (yes/no): ')

        if option == 'yes' or option == 'no' or option == 'YES' or option == 'NO' or option == 'Yes' or option == 'No':
            validation = True

            if option == 'yes':
                many = True
            else:
                many = False

            print('Your answer is valid!')

        else:
            print('Your answer is invalid!')


    if many == True:

        number_users = input('How many users you wish delete?: ')
        i = 1
        while i <= int(number_users):
            
            id_select = input(f'{i}. Type the ID: ')
            data_list = list(data)
            data_list.append(id_select)
            data = data_list

            i += 1

        data = tuple(data)

    else:
        id_select = input('Type de ID of user: ')
        data = (id_select,)

    data_base.delete_user(data,many)
    print(f'Deleted users: {data_base.get_cursor().rowcount}')
