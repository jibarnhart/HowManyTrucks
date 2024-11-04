from src.py3dbp.py3dbp import Packer, Bin, Item
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from clean_pieces import cleaning

def get_dimensions(equipment):

  if equipment in ['dry van', 'reefer']:
     
    return [100, 111, 631, 45000]
  
  elif equipment in ['flatbed']:    

    return [102, 102, 576, 46500]    

def create_trailer_object(trailer_dimensions, equipment, offset, truck_number):
    
    width = trailer_dimensions[0]
    height = trailer_dimensions[1]
    length = trailer_dimensions[2]
    
    if equipment in ['dry van', 'reefer']:

      vertices = [
        (offset * truck_number, 0, 0),                            # Vertex 1
        (width + (offset * truck_number), 0, 0),                  # Vertex 2
        (width + (offset * truck_number), length, 0),             # Vertex 3
        (offset * truck_number, length, 0),                       # Vertex 4
        (offset * truck_number, 0, height),                       # Vertex 5
        (width + (offset * truck_number), 0, height),             # Vertex 6
        (width + (offset * truck_number), length, height),        # Vertex 7
        (offset * truck_number, length, height)                   # Vertex 8
      ]

    elif equipment in ['flatbed']:

      vertices = [
        (offset * truck_number, 0, -12),                     
        (width + (offset * truck_number), 0, -12),                  
        (width + (offset * truck_number), length, -12),            
        (offset * truck_number, length, -12),                
        (offset * truck_number, 0, 0),                 
        (width + (offset * truck_number), 0, 0),            
        (width + (offset * truck_number), length, 0),     
        (offset * truck_number, length, 0)            
      ]

    return vertices

def find_piece(name, pieces):
    """ Finds the related piece that matches the name of the item.
    """
    for piece in pieces:
        if piece['name'] == name:
            return piece

def create_box_object(truck_number, item, width_offset, depth_offset, rotation_type, pieces):
    """ This creates a list of the 8 vertices that define an item's cuboid. These cuboids represent the item being packed into the truck.
    truck_number: int. Which truck the item goes into.
    item: the item object from the bin.
    offset: how far each truck cuboid is from each other.
    rotation_type: integer. 0 represents the depth of the object being parallel to the sides of the trailer. 1 is rotating it 90 degrees.
    """

    piece = find_piece(item.name, pieces)
    truck_offset = float(truck_number * width_offset)
    unfitted_offset = float(depth_offset)

    #The 'pivot' point is the bottom left corner, which is the corner closes to the passenger side of the trailer, closest to the cab.
    pivot_x_position = float(item.position[0]) + truck_offset 
    pivot_y_position = float(item.position[2]) + unfitted_offset
    pivot_z_position = float(item.position[1]) 

    if rotation_type == 0:
       
      width = float(piece['width'])
      depth = float(piece['depth'])
      height = float(piece['height'])

    elif rotation_type == 1:
       
      width = float(piece['depth'])
      depth = float(piece['width'])
      height = float(piece['height'])
    
    corner_1 = [pivot_x_position, pivot_y_position, pivot_z_position]
    corner_2 = [pivot_x_position + width, pivot_y_position, pivot_z_position]
    corner_4 = [pivot_x_position, pivot_y_position + depth, pivot_z_position]
    corner_3 = [pivot_x_position + width, pivot_y_position + depth, pivot_z_position]
    corner_5 = [pivot_x_position, pivot_y_position, pivot_z_position + height]
    corner_6 = [pivot_x_position + width, pivot_y_position, pivot_z_position + height]
    corner_8 = [pivot_x_position, pivot_y_position + depth, pivot_z_position + height]
    corner_7 = [pivot_x_position + width, pivot_y_position + depth, pivot_z_position + height]

    vertices = np.array([corner_1, corner_2, corner_3, corner_4, corner_5, corner_6, corner_7, corner_8])

    return vertices

def plot_cuboids(vertices_list, names):
    """ Given a list of the vertices of cuboids and trailers, plot the cuboids and the trailers.
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k']

    for vertices, name in zip(vertices_list, names or ['']*len(vertices_list)):
        
        for i in range(0, 4):

            ax.plot([vertices[i][0], vertices[(i+1)%4][0]],
                    [vertices[i][1], vertices[(i+1)%4][1]],
                    [vertices[i][2], vertices[(i+1)%4][2]], color='black')

            
            ax.plot([vertices[i+4][0], vertices[((i+1)%4)+4][0]],
                    [vertices[i+4][1], vertices[((i+1)%4)+4][1]],
                    [vertices[i+4][2], vertices[((i+1)%4)+4][2]], color='black')

            ax.plot([vertices[i][0], vertices[i+4][0]],
                    [vertices[i][1], vertices[i+4][1]],
                    [vertices[i][2], vertices[i+4][2]], color='black')
            
            centroid = np.mean(vertices, axis=0)
            
            ax.text(centroid[0], centroid[1], centroid[2], name, fontsize=8, horizontalalignment="center")
 
    ax.set_xlim([0,1000])
    ax.set_ylim([0,1000])
    ax.set_zlim([0,1000])
    
    plt.show()

def __main__(equipment, pieces):

    packer = Packer()
    pieces = cleaning(pieces, equipment)
    trailer_dimensions = get_dimensions(equipment)

    for i in range(25):
      packer.add_bin(Bin(f'{equipment} {i+1}', trailer_dimensions[0], trailer_dimensions[1], trailer_dimensions[2], trailer_dimensions[3]))

    for piece in pieces:
      packer.add_item(Item(piece['name'], piece['modified_width'], piece['modified_height'], piece['depth'], piece['weight']))

    packer.pack(distribute_items=True)

    vertices_list = []
    names = []
    j = 0
    
    for b in packer.bins:
      if len(b.items) > 0:
        print(f"The following items will go on {b.name}")
        for item in b.items:
          print("--->", item.name)
          trailer = create_trailer_object(trailer_dimensions, equipment, 210, j)
          vertices_list.append(trailer)
          names.append("") 
          vertices = create_box_object(j, item, 210, 0, item.rotation_type, pieces)
          vertices_list.append(vertices)
          names.append(item.name)
        unfitted = b.unfitted_items
      j=j+1
    print("The following items did not fit on any truck:")
    width = 0
    for item in unfitted:
      print("--->", item.name)
      unfitted_vertices = create_box_object(1, item, width, 700, 0, pieces)
      width += item.width
      names.append(item.name)
      vertices_list.append(unfitted_vertices)
    plot_cuboids(vertices_list, names)
        
    return

pieces = pd.read_csv('items.csv').to_dict('records')

__main__('flatbed', pieces)