division = ['Barishal', 'Chittagong', 'Dhaka', 'Khulna', 'Mymensingh', 'Rajshahi', 'Rangpur', 'Sylhet']
barishal=['Barisal',	'Barguna',	'Bhola', 'Jhalokati', 'Patuakhali', 'Pirojpur']
chittagong=['Brahmanbaria','Comilla','Chandpur', 'Lakshmipur',	'Noakhali',	'Feni',	'Khagrachhari',	'Rangamati','Bandarban','Chittagong','Coxs Bazar']
dhaka=['Dhaka','Gazipur','Kishoreganj ','Manikganj','Munshiganj', 'Narayanganj', 'Narsingdi', 'Tangail','Faridpur', 'Gopalganj',
'Madaripur', 'Rajbari', 'Shariatpur']
khulna=['Bagerhat','Chuadanga', 'Jessore', 'Jhenaidah', 'Khulna', 'Kushtia','Magura', 'Meherpur', 'Narail', 'Satkhira']
mymensingh=['Jamalpur', 'Mymensingh', 'Netrokona', 'Sherpur']
rajshahi=['Bogura', 'Chapainawabganj','Joypurhat','Naogaon','Natore','Pabna', 'Rajshahi', 'Sirajgonj']
rangpur=['Thakurgaon','Rangpur', 'Panchagarh','Nilphamari', 'Lalmonirhat', 'Kurigram','Gaibandha', 'Dinajpur']
sylhet=['Habiganj', 'Moulvibazar','Sunamganj', 'Sylhet']

print ('Welcome to Bangladesh!')
print ('We have 8 Division:')
for i in division:
  print(i)

choose = input('Enter a division name: ').lower()#to make any type of user input to lower for comapring.also can be add upper

if (choose=='barishal'):
    print("district:")
    for i in barishal:
      print(i)

elif(choose=='chittagong'):
    print("district:")
    for i in chittagong:
      print(i)


elif(choose=='dhaka'):
    print('All District name of Dhaka: ')
    for i in dhaka:
      print(i)


elif(choose=='khulna'):
    print('All District name of Khulna: ')
    for i in khulna:
      print(i)

elif(choose=='mymensingh'):
    print('All District name of Mymensingh: ')
    for i in mymensingh:
      print(i)

elif(choose=='rajshahi'):
    print('All District name of Rajshahi: ')
    for i in rajshahi:
      print(i)

elif(choose=='rangpur'):
    print('All District name of Rangpur: ')
    for i in rangpur:
      print(i)

elif(choose=='sylhet'):
    print('All District name of Sylhet: ')
    for i in sylhet:
      print(i)

else:
    print('Wrong District. Please try again.')
