# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:

conversion = {"M": 1000000,
              "B": 1000000000}
              
#print(conversion["M"])
#print(conversion["B"])

# write your construct hurricane dictionary function here:

def updateDamages(datas):
  updated = []
  for data in datas:
    if data == 'Damages not recorded':
      updated.append(data)
    elif data[-1] == "M":
      #updated.append("M")
      updated.append(float(data[:-1]) * conversion["M"])
    else:
      #updated.append("B")
      updated.append(float(data[:-1]) * conversion["B"])
  return updated

new_damages = updateDamages(damages)
#print(new_damages)

# write your construct hurricane by year dictionary function here:

def create_dict(names, months, years, max_sustained_wind, areas_affected, damage, deaths):
  dict = {}
  for i in range(len(names)):
    dict[names[i]] = {}
    dict[names[i]].update({"Name" : names[i]})
    dict[names[i]].update({"Month" : months[i]})
    dict[names[i]].update({"Year" : years[i]})
    dict[names[i]].update({"Max Sustained Wind" : max_sustained_wind[i]})
    dict[names[i]].update({"Areas Affected" : areas_affected[i]})
    dict[names[i]].update({"Damage" : damage[i]})
    dict[names[i]].update({"Deaths" : deaths[i]})
  return dict

hurricane_dict = create_dict(names, months, years, max_sustained_winds, areas_affected, new_damages, deaths)
#print(hurricane_dict)

# write your hurricane by year function here:

def hurricane_year(dict):
    year_dict = {}
    for year in years:
        hurricanes = []
        for hurricane in hurricane_dict.values():
            if hurricane["Year"] == year:
                hurricanes.append(hurricane)
            year_dict[year] = hurricanes
    return year_dict

y_dict = hurricane_year(hurricane_dict)
#print(y_dict)

# write your count affected areas function here:

def affected_count(areas_affected):
  area_counter = {}
  for area in areas_affected:
    for location in area:
      if area_counter.get(location) is None:
        area_counter[location] = 1
      else:
        area_counter[location] += 1
  return area_counter

areas_affected_count = affected_count(areas_affected)
#print(areas_affected_count)

# write your find most affected area function here:

def most_affected(areas_affected_count):
  max_area = ""
  max_times = 0

  for area, times in areas_affected_count.items():
    if times > max_times:
      max_area = area
      max_times = times
  return max_area, max_times

#print(most_affected(areas_affected_count))

# write your greatest number of deaths function here:

def most_deaths(hurricane_dict):
  hur_name = ""
  max_deaths = 0
  for hurricane in hurricane_dict.values():
    if hurricane.get("Deaths") > max_deaths:
      hur_name = hurricane.get("Name")
      max_deaths = hurricane.get("Deaths")
  return hur_name, max_deaths

#print(most_deaths(hurricane_dict))

# write your catgeorize by mortality function here:

ms = { 0 : 0, 1 : 100, 2 : 500, 3 : 1000, 4 : 10000 }
hur_mort = { 0:[], 1:[], 2:[], 3:[], 4:[]}

def mortality_rate(hurricane_dict):
  for hurricane in hurricane_dict.values():
    deaths = hurricane.get("Deaths")
    if deaths >= ms[0] and deaths < ms[1]:
      hur_mort[0].append(hurricane.get("Name"))
    elif deaths >= ms[1] and deaths < ms[2]:
      hur_mort[1].append(hurricane.get("Name"))
    elif deaths >= ms[2] and deaths < ms[3]:
      hur_mort[2].append(hurricane.get("Name"))
    elif deaths >= ms[3] and deaths < ms[4]:
      hur_mort[3].append(hurricane.get("Name"))
    else:
      hur_mort[4].append(hurricane.get("Name"))
  return hur_mort

#print(mortality_rate(hurricane_dict))

# write your greatest damage function here:

def most_damage (hurricane_dict):
  hur_name = ""
  max_damage = 0
  for hurricane in hurricane_dict.values():
    damage = hurricane.get("Damage")
    if damage == "Damages not recorded":
      continue
    elif damage > max_damage:
      hur_name = hurricane.get("Name")
      max_damage = damage
  return hur_name, max_damage

hurricane, damage = most_damage(hurricane_dict)
#print("The most damage is for: ${damage} from hurricane {hurricane}".format(damage = damage, hurricane = hurricane))

# write your catgeorize by damage function here:

ds = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
  
hur_damage = { 0:[], 1:[], 2:[], 3:[], 4:[]}
def damage_rate(hurricane_dict):
  for hurricane in hurricane_dict.values():
    damage = hurricane.get("Damage")
    if damage == "Damages not recorded":
      continue
    if damage >= ds[0] and damage < ds[1]:
      hur_damage[0].append(hurricane.get("Name"))
    elif damage >= ds[1] and damage < ds[2]:
      hur_damage[1].append(hurricane.get("Name"))
    elif damage >= ds[2] and damage < ds[3]:
      hur_damage[2].append(hurricane.get("Name"))
    elif damage >= ds[3] and damage < ds[4]:
      hur_damage[3].append(hurricane.get("Name"))
    else:
      hur_damage[4].append(hurricane.get("Name"))
  return hur_damage

#print(damage_rate(hurricane_dict))