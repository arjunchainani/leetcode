from collections import deque

def check_in_bounds(x_coord, y_coord, image):
    return True if x_coord < len(image) and x_coord >= 0 and y_coord < len(image[0]) and y_coord >= 0 else False

def find_neighbors(coords, image, visited, initial_color):
    x = coords[0]
    y = coords[1]
    
    neighbors_x = [0, 0, 1, -1]
    neighbors_y = [1, -1, 0, 0]

    neighbors_list = []
    
    for (delta_x, delta_y) in zip(neighbors_x, neighbors_y):
        x_coord = x + delta_x
        y_coord = y + delta_y

        if check_in_bounds(x_coord, y_coord, image) and image[x_coord][y_coord] == initial_color and (x_coord, y_coord) not in visited:
            neighbors_list.append((x_coord, y_coord))
            visited.append((x_coord, y_coord))

    return neighbors_list, visited

class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        curr_nodes = deque([(sr, sc)]) 
        visited = [(sr, sc)]
        initial_color = image[sr][sc]
        
        while len(curr_nodes) != 0:
            neighbor_nodes, visited = find_neighbors(curr_nodes.popleft(), image, visited, initial_color)
            curr_nodes.extend(neighbor_nodes)

        for node in visited:
            image[node[0]][node[1]] = color
        
        return image
