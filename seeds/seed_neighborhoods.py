values = ['East Downtown', 'SW Williamson Co.', 'Travis Heights', 'Zilker',
          'East Riverside', 'West Campus', 'Balcones Civic Association',
          'Clarksville', 'Brentwood', 'Old West Austin', 'Cherry Creek',
          'Scofield Ridge', 'Bouldin Creek', 'Tarrytown', 'Northwest Hills',
          'McKinney', 'South Congress', 'Hyde Park', 'Barton Hills', 'Dawson',
          'Upper Boggy Creek', 'Rosedale', 'Angus Valley', 'South Lamar',
          'Govalle', 'Holly', 'South Manchaca', 'Steiner Ranch', 'Westgate',
          'Rosewood', 'Downtown', 'Galindo', 'Allendale', 'Windsor Park',
          'West Austin', 'Barton Creek', 'Highland', 'Wooten',
          'University of Texas', 'Rollingwood', 'Copperfield', 'St. Edwards',
          'West Congress', 'East Congress', 'Long Canyon', 'Georgian Acres',
          'South First', 'Westlake Hills', 'Parker Lane', 'MLK & 183',
          'Oak Hill', 'Mesa Park', 'Hancock', 'Circle C', 'Pleasant Valley',
          'North Loop', 'Montopolis', 'North Shoal Creek', 'Pecan Spings',
          'Mueller', 'Sunset Valley', 'Old Enfield', 'St. Johns', 'Crestview',
          'Walnut Creek', 'Bull Creek', 'Cat Mountian', 'Balcony Woods',
          'Gateway', 'Anderson Mill', 'Bryker Woods', 'Canyon Mesa',
          'Windsor Hills', 'Rainey Street', 'Gracywoods', 'Lamplight Village',
          'Milwood', 'University Hills'
          ]
keys = ['neighborhood'] * len(values)

neighborhoods_seed = [{k: v} for k, v in zip(keys, values)]
