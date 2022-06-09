# This file MUST be configured in order for the code to run properly

# Make sure you put all your input images into an 'assets' folder. 
# Each layer (or category) of images must be put in a folder of its own.

# CONFIG is an array of objects where each object represents a layer
# THESE LAYERS MUST BE ORDERED.

# Each layer needs to specify the following
# 1. id: A number representing a particular layer
# 2. name: The name of the layer. Does not necessarily have to be the same as the directory name containing the layer images.
# 3. directory: The folder inside assets that contain traits for the particular layer
# 4. required: If the particular layer is required (True) or optional (False). The first layer must always be set to true.
# 5. rarity_weights: Denotes the rarity distribution of traits. It can take on three types of values.
#       - None: This makes all the traits defined in the layer equally rare (or common)
#       - "random": Assigns rarity weights at random. 
#       - array: An array of numbers where each number represents a weight. 
#                If required is True, this array must be equal to the number of images in the layer directory. The first number is  the weight of the first image (in alphabetical order) and so on...
#                If required is False, this array must be equal to one plus the number of images in the layer directory. The first number is the weight of having no image at all for this layer. The second number is the weight of the first image and so on...

# Be sure to check out the tutorial in the README for more details.                

CONFIG = [
    {
        'id': 1,
        'name': 'background',
        'directory': 'Background',
        'required': True,
        'rarity_weights': [
            80, # Abstract Blue
            50, # Abstract Cirtle
            25, # Abstract Green
            80, # Abstract Magenta
            55, # Abstract Mint
            50, # Abstract Pink
            100, # Blue Cubes
            100, # Blue Green Cubes
            35, # Blue Lights
            100, # Blue Purple Cubes
            65, # Blue Virtual Coins
            65, # Blue Watercolor
            25, # Cold Green Cubes
            10, # Colourful Abstract Circle
            5, # Colourful drops
            5, # Colorful Stripes
            2, # Copper Tint Cubes
            35, # Forest Drops
            2, # Golden Cubes
            2, # Golden Lines
            50, # Green Lights
            30, # Light Green Cubes
            50, # Magenta Cubes
            25, # Midnight Light
            65, # Mint Lights
            5, # Mint Lines
            2, # Monochrome Cubes
            40, # Monochrome Drops
            65, # Orange Cubes
            35, # Orange Pink Cubes
            15, # Orange Yellow Cubes
            50, # Pink Abstract Circle
            65, # Pink Cubes
            25, # Purple Blue Cubes
            10, # Purple Lights
            5, # Purple Lines
            35, # Purple Pink Cubes
            15, # Rainbow Stripes
            35, # Sunrise Virtual Coins
            5, # Tint Cubes
            35, # Virtual Coins
            45 # Warm Green Cubes
        ],
    },
    {
        'id': 2,
        'name': 'body',
        'directory': 'Body',
        'required': True,
        'rarity_weights': None,
    },
    {
        'id': 3,
        'name': 'clothes',
        'directory': 'Clothes',
        'required': True,
        'rarity_weights': [
            25, # Black Red Suit
            50, # Blue Asymmetric Majesty
            100, # Blue Cool Lines
            100, # Blue Fantasy
            65, # Blue Hemp
            80, # Blue Jacket
            35, # Blue Leather Badass
            80, # Blue Majesty
            75, # Blue Necklace
            10, # Blue Red Space Suit
            75, # Blue Triangle Straps
            50, # Brown Fantasy
            2, # Fire Soundwave
            5, # Golden Asymmetric Majesty
            2, # Golden Leather Badass
            65, # Green Action Hand Pocket
            15, # Green Action
            15, # Green Asymmetric Majesty
            100, # Green Cool Lines
            100, # Green Fantasy
            25, # Green Gothich Triangle
            45, # Green Hemp
            50, # Green Jacket
            50, # Green Majesty
            35, # Green Necklace
            5, # Green Pink Space Suit
            2, # Green Purple Space Suit
            15, # Green Soundwave
            35, # Green Suit
            50, # Green Triangle Straps
            5, # Mint Action
            15, # Mint Hemp
            25, # Pink Leather Badass
            35, # Pink Action Hand Pocket
            50, # Pink Action
            45, # Pink Asymmetric Majesty
            65, # Pink Majesty
            20, # Purple Action Hand Pocket
            25, # Purple Cool Lines
            10, # Purple Gothic Triangle
            5, # Purple Green Suit
            35, # Purple Jacket
            35, # Purple Necklace
            5, # Purple Soundwave
            10 # Purple Triangle Straps
        ],
    },
    {
        'id': 4,
        'name': 'hair',
        'directory': 'Hair',
        'required': True,
        'rarity_weights': [
            100, # Blond Buns
            100, # Blond Short
            100, # Blondy Asymmetric
            100, # Blondy Bun
            50, # Blue Braid
            80, # Blue Bun
            80, # Blue Hat
            70, # Blue Hippie
            100, # Brunette Bun
            80, # Brunette Buns
            100, # Dark Blond Hippie
            15, # Dark Blue Electric
            80, # Ginger Asymmetric
            50, # Ginger Braid
            80, # Gold Brown Asymmetric
            35, # Golden Bob
            70, # Golden Brown Shine
            10, # Golden Aerial
            70, # Green Bob
            70, # Light Blond Hippie
            35, # Magenta Buns
            10, # Mint Buns
            15, # Mint Hat
            2, # Monochrome Electric
            70, # Orange Short
            50, # Pink Aerial
            50, # Pink Braid
            50, # Pink Hat
            70, # Pink Hippie
            70, # Pink Short
            2, # Postmodern Monochrome White
            15, # Postmodern Pink White
            5, # Postmodern Purple White
            25, # Purple Aerial
            35, # Purple Asymmetric
            35, # Purple Bangs Tail
            60, # Purple Blue Hippie
            60, # Purple Bob
            70, # Purple Hippie
            60, # Purpl Shine
            5, # Sky Blue Electric
            15, # Sunrise Bangs Tail
            15, # Sunset Bangs Tail
            10 # Tint Shine
        ],
    },
    {
        'id': 5,
        'name': 'headwear',
        'directory': 'Headwear',
        'required': False,
        'rarity_weights': [
            100, # None
            70, # Blue Cirle AI Vision
            70, # Blue Cyberpunk Mechanic
            70, # Blue Light Triangles
            70, # Blue Line
            50, # Blue Mechanical
            70, # Blue Smart Assistant
            70, # Copper Mechanical
            2, # Golden Mechanical
            60, # Green Crosshair Crypto
            55, # Green Cyberpunk Mechanic
            50, # Green Light Triangles
            25, # Green Line
            60, # Green Ride Smart
            55, # Green Smart Assistant
            50, # Green Smart Cryptochecker
            45, # Magenta Circle AI Vision
            15, # Mint Circle AI Vision
            10, # Mint Crosshair Crypto
            5, # Mint Ride Smart
            2, # Mint Smart Cryptochecker
            35, # Orange Smart Assistant
            50, # Pink Circle AI Vision
            60, # Pink Crosshair Crypto
            60, # Pink Light Triangles
            20, # Pink Line
            50, # Pink Ride Smart
            50, # Pink Smart Assistant
            50, # Pink Smart Cryptochecker
            15, # Purple Circle AI Vision
            25, # Purple Crosshair Crypto
            35, # Purple Cyberpunk Mechanic
            25, # Purple Light Triangles
            15, # Purple Mechanical
            10, # Purple Smart Assistant
            25, # Purple Smart Cryptochecker
            15, # Silver Mechanical
            5, # Yellow Crosshair Crypto
            2, # Yellow Cyberpunk Mechanic
            15, # Yellow Light Triangles
            5, # Yellow Line
            15, # Yellow Ride Smart
            25 # Yellow Smart Cryptochecker
        ],
    },
]
