def find_arrays_with_digit(arrays, digit):
    result_arrays = []

    for array in arrays:
        if digit in array:
            result_arrays.append(array)

    return result_arrays


def extract_digits(arrays, digit_to_exclude):
    digits = set()

    for array in arrays:
        for num in array:
            if num != digit_to_exclude:
                digits.add(num)

    return digits


def find_arrays_with_digits(arrays, digits):
    result_arrays = []

    for array in arrays:
        for num in array:
            if num in digits:
                result_arrays.append(array)

    return result_arrays


# Исходный массив
arrays = [[16, 17], [17, 18], [14, 15], [14, 16], [18, ''], [15, ''], [1, 14], [1, 19], [1, 2], [1, 28], [1, 30], [1, 31], [19, ''], [2, 29], [28, ''], [30, ''], [31, ''], [26, 1], [29, '']]

# Шаг 1: Находим все массивы, содержащие цифру 14
step1_result = find_arrays_with_digit(arrays, 14)
print("Массивы с цифрой 14:")
for array in step1_result:
    print(array)

# Шаг 2: Извлекаем цифры из полученных массивов, исключая 14
step2_digits = extract_digits(step1_result, 14)
print("\nЦифры, за исключением 14:")
for digit in step2_digits:
    print(digit)

# Шаг 3: Находим массивы, содержащие цифры из предыдущего шага
step3_result = find_arrays_with_digits(arrays, step2_digits)
print("\nМассивы с цифрами из предыдущего шага:")
for array in step3_result:
    print(array)



        # while step <= depth:
        # while step <= 6:
        #     for j in range(0, len(massive_for_path)):
    # tmp_start_id = start_id
    # for i in range(0, len(massive_for_path)):
    #     if tmp_start_id in massive_for_path[i]:
    #         if tmp_start_id != massive_for_path[i][0]:
    #             tmp = massive_for_path[i][0]
    #             massive_for_path[i][0] = tmp_start_id
    #             massive_for_path[i][1] = tmp
    #         massive.append(massive_for_path[i])
    #         # print(massive_for_path[i])
    # print(massive)
    # # step = 2
    # for i in range(0, len(massive)):
    #     if tmp_start_id in massive_for_path[i]:
    #         if tmp_start_id != massive_for_path[i][0]:
    #             print(massive_for_path[i][1])
    #         else:
    #             print(massive_for_path[i][0])
    #     while step <= depth:
    #         # for j in range( )
    #         step += 1
    #     step = 2
    # while step <= depth:
    #     for i in range(0, len(massive)):
            
    #         step += 1

    # for i in range(0, len(massive_for_path)):
    #     print(massive_for_path[i])
    #     if tmp_start_id in massive_for_path[i]:
    #         if tmp_start_id != massive_for_path[i][0]:
    #             tmp_start_id = massive_for_path[i][1]
    #         else:
    #             tmp_start_id = massive_for_path[i][0]

        # print(tmp_start_id)
        # if tmp_start_id in massive_for_path[i]:
        #     if tmp_start_id != massive_for_path[i][0]:
                
    # for i in range(len(massive_for_path)):
    #     print(i)
        # print(massive_norm[i])
    # while step <= depth:
    #     for i in range(0, len(allfriend)):
    #         if allfriend[i]['step'] == step:
    #             pass
    #             # massive_for_path.append()
    #             # print(allfriend[i])
    #     step += 1
    # for i in massive_norm:
        # print(massive_norm)
    # tmp_previous_id = start_id
    # tmp_step_len = 1
    # step = 1
    # while step <= depth:
    #     for i in range(0, len(allfriend)):
    #         if allfriend[i]['step'] == step and step == 1:
    #             tmp = [tmp_previous_id, allfriend[i]['previous_id']]
    #             massive_for_path.append(tmp)
    #         if allfriend[i]['step'] == step and step > 1:
    #             for j in range(0, len(massive_for_path)):
    #                 if allfriend[i]['previous_id'] in allfriend[j]['people_friend']:
    #                     print(f"{allfriend[i]['previous_id']} in {allfriend[j]['people_friend']}, i: {i}, j: {j}")
    #                     print(allfriend[i]['previous_id'])
    #                     print(allfriend[j]['people_friend'])
    #                     for find_tmp_j in range(0, len(massive_for_path)):
    #                         if massive_for_path[find_tmp_j][len(massive_for_path[find_tmp_j])-1] == allfriend[j]['previous_id']:
    #                             tmp_j = find_tmp_j
    #                     append_path(massive_for_path, tmp_j, allfriend[i]['previous_id'])
    #                     # print(j)
    #     step += 1
    # print(massive_for_path)



    # allfriend_norm = []
    # for i in range(0, len(allfriend)):
    #     if allfriend[i][step]
        # print(allfriend[i])
    # step = 1
    # while step <= depth:
    #     for create_path in range(1, len(allfriend)):
    #         if allfriend['friend'][create_path]['step'] == step:
    #             print(allfriend['friend'][create_path])

    #     step += 1

    # step = 1
    # while step <= depth:
    #     for create_path in range(0, len(yourfriend_UPDOWN['friend'])):
    #         if yourfriend_UPDOWN['friend'][create_path]['step'] == step:
    #             print(yourfriend_UPDOWN['friend'][create_path])

    #     step += 1
    









    # # Выстраивание путей кто кого знает
    # massive_for_path_1 = []
    # tmp_previous_id = start_id
    # tmp_step_len = 1
    # step = 1
    # while step <= depth:
    #     for create_path in range(1, len(yourfriend_DOWN['friend'])):
    #         if yourfriend_DOWN['friend'][create_path]['step'] == 1 and step == 1:
    #             print(yourfriend_DOWN['friend'][create_path]['previous_id'])
    #             print(tmp_previous_id)
    #             tmp = [tmp_previous_id,  yourfriend_DOWN['friend'][create_path]['previous_id']]
    #             massive_for_path_1.append(tmp)

    #         if yourfriend_DOWN['friend'][create_path]['step'] == step and step > 1:
    #             for i in range(0, tmp_step_len):
    #                 if yourfriend_DOWN['friend'][create_path]['previous_id'] in yourfriend_DOWN['friend'][i + 1]['people_friend']:
    #                     append_path(massive_for_path_1, i, yourfriend_DOWN['friend'][create_path]['previous_id'])
    #         tmp_step_len = create_path
    #     step += 1

    # for i in massive_for_path_1:
    #     for j in range(0, len(i)):
    #         if i[j] == start_id:
    #             i[j] = 'Я'
    #         else:
    #             i[j] = get_user_name(i[j])
    # # Выстраивание путей кто кого знает

    # massive_for_path = []
    # tmp_previous_id = start_id
    # tmp_step_len = 1
    # step = 1
    # while step <= depth:

    #     for create_path in range(0, len(yourfriend_UPDOWN['friend'])):
    #         if yourfriend_UPDOWN['friend'][create_path]['step'] == 1 and step == 1:
    #             tmp = [tmp_previous_id,  yourfriend_UPDOWN['friend'][create_path]['previous_id']]
    #             massive_for_path.append(tmp)
            
    #         if yourfriend_UPDOWN['friend'][create_path]['step'] == step and step > 1:
    #             for i in range(0, len(massive_for_path)):
    #                 if yourfriend_UPDOWN['friend'][create_path]['previous_id'] in yourfriend_UPDOWN['friend'][i]['people_friend']:

    #                     # print(yourfriend_UPDOWN['friend'][i]['people_friend'])
    #                     append_path(massive_for_path, i, yourfriend_UPDOWN['friend'][create_path]['previous_id'])

    #     step += 1

    # for i in massive_for_path:
    #     for j in range(0, len(i)):
    #         if i[j] == start_id:
    #             i[j] = 'Я'
    #         else:
    #             i[j] = get_user_name(i[j])
    # massive_for_path_1 = []
    # massive_for_path = []
    # print(massive_for_path_1)
    # print(len(yourfriend_DOWN['friend']))

    # print(massive_for_path_1)
    # print(yourfriend_DOWN['friend'])
    # print(massive_for_path)
    # print(yourfriend_UPDOWN['friend'])

    # r = remove_duplicates(yourfriend_DOWN['friend'], yourfriend_UPDOWN['friend'])
    # print(yourfriend_DOWN['friend'])
    # print(yourfriend_UPDOWN['friend'])
    # ИСПОЛЬЗУЕТСЯ yourfriend_DOWN
    # ИСПОЛЬЗУЕТСЯ find_friend_UP 

    # for find_people in range(1, len(yourfriend_DOWN['friend'])):
    #     select_people = InformationAboutUser.objects.filter(id=yourfriend_DOWN['friend'][find_people]['previous_id']).values('id', 'name', 'second_name', 'what_do', 'keywords', 'city', 'contact_information').first()
        # people['people'].append(json_string_people(select_people['id'], select_people['name'], select_people['second_name'], select_people['what_do'], select_people['keywords'], select_people['city'], select_people['contact_information'], massive_for_path_1[find_people-1]))

    # for find_people in range(0, len(yourfriend_UPDOWN['friend'])):
    #     select_people = InformationAboutUser.objects.filter(id=yourfriend_UPDOWN['friend'][find_people]['previous_id']).values('id', 'name', 'second_name', 'what_do', 'keywords', 'city', 'contact_information').first()
    #     people['people'].append(json_string_people(select_people['id'], select_people['name'], select_people['second_name'], select_people['what_do'], select_people['keywords'], select_people['city'], select_people['contact_information'], massive_for_path_1[find_people]))