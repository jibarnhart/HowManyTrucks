from py3dbp import Packer, Bin, Item
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

DRY_VAN = {
    "length": 631,
    "width": 100,
    "height": 111,
    "square_inches": 63100,
    "cubic_inches": 7004100
}

PIECES = [
  {
    "name": "MAIN CONSERVATOR",
    "weight": 6460,
    "depth": 171,
    "width": 86,
    "height": 106,
    "modified_height": 106
  },
  {
    "name": "CLTC CONSERVATOR",
    "weight": 950,
    "depth": 90,
    "width": 43,
    "height": 42,
    "modified_height": 106
  },
  {
    "name": "AIR VENT PIPE LINE",
    "weight": 2213,
    "depth": 153,
    "width": 74,
    "height": 31,
    "modified_height": 106
  },
  {
    "name": "HV BUSHING (HT)",
    "weight": 1512,
    "depth": 193,
    "width": 30,
    "height": 46,
    "modified_height": 106
  },
  {
    "name": "HV BUSHING (CT)",
    "weight": 1512,
    "depth": 193,
    "width": 30,
    "height": 46,
    "modified_height": 106
  },
  {
    "name": "HV BUSHING (HT)",
    "weight": 1512,
    "depth": 193,
    "width": 30,
    "height": 46,
    "modified_height": 106
  },
  {
    "name": "MVN BUSHING",
    "weight": 551,
    "depth": 70,
    "width": 23,
    "height": 28,
    "modified_height": 106
  },
  {
    "name": "XV & XVN BUSHING",
    "weight": 1076,
    "depth": 82,
    "width": 62,
    "height": 30,
    "modified_height": 106
  },
  {
    "name": "YV & YVN BUSHING",
    "weight": 1076,
    "depth": 82,
    "width": 62,
    "height": 30,
    "modified_height": 106
  },
  {
    "name": "HV BUSHING HOUSING",
    "weight": 6402,
    "depth": 122,
    "width": 51,
    "height": 53,
    "modified_height": 106
  },
  {
    "name": "MVN BUSHING HOUSING",
    "weight": 675,
    "depth": 33,
    "width": 33,
    "height": 34,
    "modified_height": 106
  },
  {
    "name": "XV & XVN BUSHING HOUSING",
    "weight": 2405,
    "depth": 121,
    "width": 41,
    "height": 40,
    "modified_height": 106
  },
  {
    "name": "XV & XVN BUSHING HOUSING",
    "weight": 2405,
    "depth": 121,
    "width": 41,
    "height": 40,
    "modified_height": 106
  },
  {
    "name": "RADIATOR",
    "weight": 4244,
    "depth": 114,
    "width": 74,
    "height": 59,
    "modified_height": 106
  },
  {
    "name": "RADIATOR",
    "weight": 4244,
    "depth": 114,
    "width": 74,
    "height": 59,
    "modified_height": 106
  },
  {
    "name": "RADIATOR",
    "weight": 4244,
    "depth": 114,
    "width": 74,
    "height": 59,
    "modified_height": 106
  },
  {
    "name": "RADIATOR",
    "weight": 4244,
    "depth": 114,
    "width": 74,
    "height": 59,
    "modified_height": 106
  },
  {
    "name": "RADIATOR",
    "weight": 4244,
    "depth": 114,
    "width": 74,
    "height": 59,
    "modified_height": 106
  },
  {
    "name": "RADIATOR",
    "weight": 4244,
    "depth": 114,
    "width": 74,
    "height": 59,
    "modified_height": 106
  },
  {
    "name": "RADIATOR",
    "weight": 4244,
    "depth": 114,
    "width": 74,
    "height": 59,
    "modified_height": 106
  },
  {
    "name": "RADIATOR",
    "weight": 4244,
    "depth": 114,
    "width": 74,
    "height": 59,
    "modified_height": 106
  },
  {
    "name": "RADIATOR BANK",
    "weight": 4835,
    "depth": 169,
    "width": 129,
    "height": 53,
    "modified_height": 106
  },
  {
    "name": "RADIATOR BANK PIPE LINE",
    "weight": 3706,
    "depth": 121,
    "width": 82,
    "height": 38,
    "modified_height": 106
  },
  {
    "name": "RADIATOR BANK OIL PUMP PIPE LINE",
    "weight": 692,
    "depth": 47,
    "width": 43,
    "height": 32,
    "modified_height": 106
  },
  {
    "name": "RADIATOR BANK SUPPORT (1)",
    "weight": 6495,
    "depth": 220,
    "width": 94,
    "height": 43,
    "modified_height": 106
  },
  {
    "name": "RADIATOR BANK SUPPORT (2)",
    "weight": 2921,
    "depth": 153,
    "width": 74,
    "height": 35,
    "modified_height": 106
  },
  {
    "name": "FAN SUPPORT & CABLE PIPE & ETC SUPPORT",
    "weight": 2452,
    "depth": 121,
    "width": 62,
    "height": 52,
    "modified_height": 106
  },
  {
    "name": "COOLING FAN",
    "weight": 1768,
    "depth": 100,
    "width": 68,
    "height": 60,
    "modified_height": 106
  },
  {
    "name": "PRESSURE RELIEF DEVICE PIPE LINE",
    "weight": 1411,
    "depth": 149,
    "width": 62,
    "height": 33,
    "modified_height": 106
  },
  {
    "name": "XV & YV LA SUPPORT",
    "weight": 2114,
    "depth": 137,
    "width": 66,
    "height": 32,
    "modified_height": 106
  },
  {
    "name": "ACCESORY",
    "weight": 1182,
    "depth": 62,
    "width": 54,
    "height": 30,
    "modified_height": 106
  }
]

def create_trailer_object(width, length, height, offset, truck_number):
    """ This creates a list of the 8 vertices that define a trailer's cuboid. This cuboid represents the trailer being packed.
    width: number. The width of the trailer
    length: number. The length of the trailer
    height: number. The height of the trailer
    offset: How far apart each trailer cuboid should be.
    truck_number: the number of the truck being packed
    """
    vertices = [
        (offset * truck_number, 0, 0),                      # Vertex 1
        (width + (offset * truck_number), 0, 0),                  # Vertex 2
        (width + (offset * truck_number), height, 0),             # Vertex 3
        (offset * truck_number, height, 0),                 # Vertex 4
        (offset * truck_number, 0, length),                 # Vertex 5
        (width + (offset * truck_number), 0, length),             # Vertex 6
        (width + (offset * truck_number), height, length),        # Vertex 7
        (offset * truck_number, height, length)             # Vertex 8
    ]
    return vertices

def find_piece(name):
    """ Finds the related piece that matches the name of the item.
    """
    for piece in PIECES:
        if piece['name'] == name:
            return piece

def create_box_object(truck_number, item, offset):
    """ This creates a list of the 8 vertices that define an item's cuboid. These cuboids represent the item being packed into the truck.
    truck_number: int. Which truck the item goes into.
    item: the item object from the bin.
    offset: how far each truck cuboid is from each other.
    """

    piece = find_piece(item.name)

    corner_1 = [float(item.position[0])+truck_number*offset, float(item.position[2]), float(item.position[1])] #width, depth, height
    corner_2 = [float(item.position[0])+float(item.width)+truck_number*offset, float(item.position[2]), float(item.position[1])]
    corner_4 = [float(item.position[0])+truck_number*offset, float(item.position[2])+float(item.depth), float(item.position[1])]
    corner_3 = [float(item.position[0])+truck_number*offset+float(item.width), float(item.position[2])+float(item.depth), float(item.position[1])]
    corner_5 = [float(item.position[0])+truck_number*offset, float(item.position[2]), float(item.position[1])+float(piece['height'])] #width, depth, height
    corner_6 = [float(item.position[0])+float(item.width)+truck_number*offset, float(item.position[2]), float(item.position[1])+float(piece['height'])]
    corner_8 = [float(item.position[0])+truck_number*offset, float(item.position[2])+float(item.depth), float(item.position[1])+float(piece['height'])]
    corner_7 = [float(item.position[0])+float(item.width)+truck_number*offset, float(item.position[2])+float(item.depth), float(item.position[1])+float(piece['height'])]

    vertices = np.array([corner_1, corner_2, corner_3, corner_4, corner_5, corner_6, corner_7, corner_8])

    return vertices

def plot_cuboids(vertices_list, names):
    """ Given a list of the vertices of cuboids and trailers, plot the cuboids and the trailers.
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for vertices, name in zip(vertices_list, names or ['']*len(vertices_list)):
        for i in range(0, 4):
            ax.plot([vertices[i][0], vertices[(i+1)%4][0]],
                    [vertices[i][1], vertices[(i+1)%4][1]],
                    [vertices[i][2], vertices[(i+1)%4][2]], 'r-')

            ax.plot([vertices[i+4][0], vertices[((i+1)%4)+4][0]],
                    [vertices[i+4][1], vertices[((i+1)%4)+4][1]],
                    [vertices[i+4][2], vertices[((i+1)%4)+4][2]], 'r-')

            ax.plot([vertices[i][0], vertices[i+4][0]],
                    [vertices[i][1], vertices[i+4][1]],
                    [vertices[i][2], vertices[i+4][2]], 'r-')
            
            centroid = np.mean(vertices, axis=0)
            
            ax.text(centroid[0], centroid[1], centroid[2], name, fontsize=5)
            
    ax.set_xlim([0,1000])
    ax.set_ylim([0,1000])
    ax.set_zlim([0,1000])
    
    plt.show()

def __main__():

    packer = Packer()

    for i in range(10):
        packer.add_bin(Bin(f'53-ft-dry-van-{i+1}', 100, 111, 631, 45000))

    for piece in PIECES:
        packer.add_item(Item(piece['name'], piece['width'], piece['modified_height'], piece['depth'], piece['weight']))

    packer.pack(distribute_items=True)

    vertices_list = []
    names = []
    
    j = 0
    for b in packer.bins:
        for item in b.items:
            if len(b.items) > 0:
                van = create_trailer_object(100, 111, 631, 210, j)
                vertices_list.append(van)
                names.append("")
                vertices = create_box_object(j, item, 210)
                vertices_list.append(vertices)
                names.append(item.name)
        j=j+1
    plot_cuboids(vertices_list, names)
        
    return

__main__()