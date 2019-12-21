values = ['Guesthouse', 'House', 'Apartment', 'Guest suite', 'Condominium',
          'Townhouse', 'Bungalow', 'Loft', 'Bed and breakfast', 'Other',
          'Cabin', 'Cottage', 'Campsite', 'Tent', 'Villa', 'Camper/RV',
          'Nature lodge', 'Tiny house', 'Chalet', 'Farm stay', 'Boat',
          'Serviced apartment', 'Boutique hotel', 'Bus', 'Tipi',
          'Treehouse', 'Barn', 'Hostel', 'Yurt', 'Houseboat', 'Resort',
          'Dome house', 'Aparthotel', 'Hotel', 'Casa particular (Cuba)',
          'Earth house', 'Hut']
keys = ['property_type'] * len(values)

property_types_seed = [{k: v} for k, v in zip(keys, values)]
