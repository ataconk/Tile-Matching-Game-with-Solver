from statistics import mode
from getColorandSize import getColorandSize


# Finding neighbors of flooded tiles
def find_neighbours(arr, flooded):
    neighbors = []
    for i in range(len(arr)):
        for j, value in enumerate(arr[i]):
            if i == 0 or i == len(arr) - 1 or j == 0 or j == len(arr[i]) - 1:
                # corners
                new_neighbors = []
                if i != 0:
                    new_neighbors.append({
                        "value": arr[i - 1][j],
                        "location": "top",
                        "position": [i - 1, j]
                        })  # top neighbor
                if j != len(arr[i]) - 1:
                    new_neighbors.append({
                        "value": arr[i][j + 1],
                        "location": "right",
                        "position": [i, j+1]
                        })  # right neighbor
                if i != len(arr) - 1:
                    new_neighbors.append({
                        "value": arr[i + 1][j],
                        "location": "bottom",
                        "position": [i+1, j]
                        })  # bottom neighbor
                if j != 0:
                    new_neighbors.append({
                        "value": arr[i][j - 1],
                        "location": "left",
                        "position": [i, j-1]
                        })  # left neighbor

            else:
                # add neighbors
                new_neighbors = [
                    {
                        "value": arr[i - 1][j],
                        "location": "top",
                        "position": [i-1, j]
                    },  # top neighbor
                    {
                        "value": arr[i][j + 1],
                        "location": "right",
                        "position": [i, j+1]
                    },  # right neighbor
                    {
                        "value": arr[i + 1][j],
                        "location": "bottom",
                        "position": [i+1, j]
                    },  # bottom neighbor
                    {
                        "value": arr[i][j - 1],
                        "location": "left",
                        "position": [i, j-1]
                    }  # left neighbor
                ]
            not_flooded_neighbors = []
            for x in new_neighbors:
                if x['position'] not in flooded:
                    not_flooded_neighbors.append(x)
            if [i, j] in flooded:
                neighbors.append({
                    "position": [i, j],
                    "value": value,
                    "neighbors": not_flooded_neighbors})

    return neighbors


# Get the most common item in array, if tie get the lower
def get_most_common(my_list):
    my_list = sorted(my_list)
    return(mode(my_list))


# Get location of neighbors
def get_neighbors_loc(my_neighbours):
    neighbors_loc = []
    for neighbor in my_neighbours:
        [neighbors_loc.append(item['position']) for item in neighbor['neighbors']]  # noqa
    return neighbors_loc


# get highest number of repeated color in neighbors
def neighbors_count(my_neighbours):
    neigbors_loc = get_neighbors_loc(my_neighbours)
    count_num = []
    filled = False
    for point in my_neighbours:
        for neighbor in point['neighbors']:

            # Avoiding adding neighbor location more than one
            if neigbors_loc.count(neighbor['position']) > 1 and not filled:
                count_num.append(neighbor['value'])
                filled = True
            else:
                count_num.append(neighbor['value'])
    return get_most_common(count_num)


# Updating flooded coordinates
def update_flooded(flooded, my_neighbours, most_common):
    for point in my_neighbours:
        for neighbor in point['neighbors']:
            if neighbor['value'] == most_common:
                flooded.append(neighbor['position'])
    return flooded


# Updating board with new collors
def update_initial_board(initial_board, flooded, most_common):

    for indices in flooded:
        row = indices[0]
        col = indices[1]
        initial_board[row][col] = most_common
    return initial_board


# check if neighbors have already same color and add them to flooded
def check_same_value(initial_board, flooded):

    finisht = True
    my_neighbours = find_neighbours(initial_board, flooded)
    for n in my_neighbours:
        for neighbor in n['neighbors']:
            if n['value'] == neighbor['value']:
                flooded.append(neighbor['position'])
                finisht = False
    if not finisht:
        check_same_value(initial_board, flooded)


if __name__ == '__main__':

    # if the game is done
    is_done = False
    # get Initial boardsize and number of colors
    initial_board = getColorandSize()
    print("Starting...")
    print("Initial Board--->")
    print(initial_board)
    # setting the origin
    flooded = [[0, 0]]
    count = 0
    while not is_done:
        count += 1
        print("Iteration "+str(count)+" --->")
        check_same_value(initial_board, flooded)
        my_neighbours = find_neighbours(initial_board, flooded)
        # print(find_neighbours(initial_board))
        most_common = neighbors_count(my_neighbours)
        flooded = update_flooded(flooded, my_neighbours, most_common)

        initial_board = update_initial_board(initial_board,
                                             flooded,
                                             most_common)
        print('Choice of color: ' + str(most_common))
        print(initial_board)

        is_done = (initial_board == initial_board[0]).all()
