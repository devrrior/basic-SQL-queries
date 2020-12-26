def update_user(data_base):
    
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

    print()

    if many == True:

        number_users = input('How many users you wish update?: ')
        i = 1
        while i <= int(number_users):
            
            name = input('Type the name: ')
            last_name = input('Type the last name: ')
            email = input('Type the email: ')
            id_user = input('Type the ID: ')

            data_update = (name,last_name,email,id_user)
            data_list = list(data)
            data_list.append(data_update)
            data = data_list

            i += 1

    else:
        name = input('Type the name: ')
        last_name = input('Type the last name: ')
        email = input('Type the email: ')
        id_user = input('Type the ID: ')

        data_update = (name,last_name,email,id_user)
        data = data_update


    data_base.update_user(data,many)
    print(f'Update users: {data_base.get_cursor().rowcount}')
