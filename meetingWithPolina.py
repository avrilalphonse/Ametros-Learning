import datetime

def get_members():
  members = [[543, 'Eve', '1989-06-26'], [544, 'Alice', '1990-03-26'], [545, 'Bob','2001-09-15'], [546, 'Charlie', '1985-10-22'], [545, 'Ivan', '1987-04-09'], [546, 'Gerth', '1990-08-14'], [543, 'Leo', '1993-09-3'], [544, 'Hudson', '1984-11-08'], [545, 'Dylan', '1983-05-13'], [546, 'Ezra', '1992-01-27'], [545, 'Thomas', '1987-07-19'], [546, 'Charles', '1989-12-16'],[545, 'Maverick', '2003-02-25'], [546, 'Elias','1987-04-25']]
  return members

def sort_members(members):
  return sorted(members, key=lambda x: x[2])

def get_enterprise(members):
  days=[]
  date=[]
  for i in range(len(members)):
    days.append(datetime.datetime.strptime(members[i][2], '%Y-%m-%d').day)
  for i in range(len(days)):
    if days[i] > 1:
      for j in range(2,days[i]):
        if (days[i] % j) == 0:
          days[i] = False
          break
  for k in range(len(members)):
    if days[k] != False:
      date.append(members[k])
  return date

def get_managers(members):
  bday=[]
  name=[]
  final=[]
  for i in range(len(members)):
    bday.append(datetime.datetime.strptime(members[i][2], '%Y-%m-%d').day)
    name.append(members[i][1])
  for i in range(len(members)):
    if len(name[i]) <= 6:
      name[i] = False
    if (members[i][0]%2 == 0 or bday[i]%2 != 0):
      bday[i] = False
  for k in range(len(members)):
    if (name[k] != False or bday[k] != False):
      final.append(members[k])
  return final

if __name__ == "__main__":
  members = get_members()
  membersSorted = sort_members(members)
  print(membersSorted)
  enterprise = get_enterprise(membersSorted)
  print(enterprise)
  managers = get_managers(membersSorted)
  print(managers)