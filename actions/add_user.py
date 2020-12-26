def add_user(data_base):

    data = ()
    many = None
    validation = False
    while validation == False:

        option = input('Do you wish add more than one user? (yes/no): ')

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
        number_users = int(input('How many users you wish add?: '))

        i = 1
        while i <= number_users:

            print(f'User {i}\n')
            name = input('Type the name: ')
            last_name = input('Type the last name: ')
            email = input('Type the email: ')
            print('\n')

            new_data = (name,last_name,email)

            data_list = list(data)
            data_list.append(new_data)
            data = data_list

            i += 1


    else:
        
            name = input('Type the name: ')
            last_name = input('Type the last name: ')
            email = input('Type the email: ')

            data = (name,last_name,email)




    data_base.add_user(data,many)
    print(f'Added users: {data_base.get_cursor().rowcount}')
