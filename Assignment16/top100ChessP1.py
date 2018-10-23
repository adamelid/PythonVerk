RANK = 0
NAME = 1
COUNTRY = 2
RATING = 3
BIRTH_YEAR = 4

def get_input(user_prompt):
    user_input = input(user_prompt)
    return user_input

def read_file(name):
    try:
        file_content = open(name, "r")
        return file_content

    except FileNotFoundError:
        print("Error")
        return None

def create_key(a_list):

    last_name, first_name = a_list.split(",")
    last_name = last_name.strip()
    first_name = first_name.strip()
    key = "{} {}".format(first_name, last_name)

    return key

def clean_data(a_list):

    rank = int(a_list[RANK].strip())
    country = a_list[COUNTRY].strip()
    points = int(a_list[RATING].strip())
    birth_year = int(a_list[BIRTH_YEAR].strip())

    return [rank, country, points, birth_year]


def create_dict_from_file(file_content):
    chess_players_dict = {}

    for line in file_content:
        line = line.split(";")
    
        key = create_key(line[1])
        chess_players_dict[key] = clean_data(line)
    
    return chess_players_dict

def print_header(header_str):

    print(header_str)
    print("-"*len(header_str))

def print_results(chess_players_dict, countries_dict):
    for country in sorted(countries_dict.keys()):
        number_of_players = countries_dict[country][0]
        total_points = countries_dict[country][1]
        average = total_points / number_of_players

        print("{} ({}) ({:.1f}): ".format(country, number_of_players, average))

        for player in chess_players_dict.keys():
            if chess_players_dict[player][1] == country:
                print("{:>40}{:>10d}".format(player, chess_players_dict[player][2]))

def get_points_per_country(chess_players_dict):
    my_dict = {}

    for chess_players_dict in chess_players_dict.items():
        country = chess_players_dict[1][1]
        if country in my_dict:
            my_dict[country][0] += 1
            my_dict[country][1] += chess_players_dict[1][2]

        else:
            data = [1, chess_players_dict[1][2]]
            my_dict[country] = data

    return my_dict

def main():
    file_name = get_input("Enter filename: ")
    file_content = read_file(file_name)

    if file_content:
        chess_players_dict = create_dict_from_file(file_content)
        file_content.close()
        countries_dict = get_points_per_country(chess_players_dict)
        print_header("Players by country:")
        print_results(chess_players_dict, countries_dict)
main()