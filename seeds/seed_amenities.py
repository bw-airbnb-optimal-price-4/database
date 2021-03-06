values = ["TV", "Cable TV", "Internet", "Wifi", "Air conditioning",
          "Wheelchair accessible", "Kitchen", "Free parking on premises",
          "Breakfast", "Pets live on this property", "Cat(s)", "Hot tub",
          "Heating", "Family/kid friendly", "Washer", "Dryer",
          "Smoke detector", "Carbon monoxide detector", "First aid kit",
          "Safety card", "Fire extinguisher", "Essentials", "Shampoo",
          "Lock on bedroom door", "24-hour check-in", "Hangers",
          "Hair dryer", "Iron", "Laptop friendly workspace",
          "Self check-in", "Keypad", "Private living room",
          "Private entrance", "Outlet covers", "High chair", "Stair gates",
          "Babysitter recommendations", "Pack n Play/travel crib",
          "Hot water", "Body soap", "Bath towel", "Toilet paper",
          "Bed linens", "Extra pillows and blankets",
          "Ethernet connection", "Microwave", "Coffee maker",
          "Refrigerator", "Dishwasher", "Dishes and silverware",
          "Cooking basics", "Oven", "Stove", "BBQ grill",
          "Patio or balcony", "Garden or backyard", "Beach essentials",
          "Luggage dropoff allowed", "Long term stays allowed",
          "Wide hallways", "No stairs or steps to enter",
          "Wide entrance for guests", "Flat path to guest entrance",
          "Well-lit path to entrance", "No stairs or steps to enter",
          "Wide entrance", "Extra space around bed",
          "Accessible-height bed", "No stairs or steps to enter",
          "Wide doorway to guest bathroom", "Accessible-height toilet",
          "Wide clearance to shower, toilet",
          "No stairs or steps to enter", "Wide entryway",
          "Handheld shower head", "Hot water kettle", "Ceiling fan",
          "Central air conditioning", "Smart TV", "DVD player",
          "Rain shower", "Balcony", "Outdoor kitchen", "Sound system",
          "Printer", "Exercise equipment", "Breakfast table",
          "Formal dining area", "Sun loungers", "Day bed",
          "Private hot tub", "Convection oven", "Netflix", "HBO GO",
          "Amazon Echo", "Memory foam mattress",
          "High-resolution computer monitor", "Outdoor seating",
          "Outdoor parking", "Walk-in shower", "Full kitchen",
          "Bedroom comforts", "Bathroom essentials"]
keys = ['amenity'] * len(values)

amenities_seed = [{k: v} for k, v in zip(keys, values)]
