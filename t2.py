#division = ['Barishal', 'Chittagong', 'Dhaka', 'Khulna', 'Mymensingh', 'Rajshahi', 'Rangpur', 'Sylhet']

district={'barishal':['Barisal',	'Barguna',	'Bhola', 'Jhalokati', 'Patuakhali', 'Pirojpur'],

'chittagong':['Brahmanbaria','Comilla','Chandpur', 'Lakshmipur',	'Noakhali',	'Feni',	'Khagrachhari',	'Rangamati','Bandarban','Chittagong','Coxs Bazar'],

'dhaka':['Dhaka','Gazipur','Kishoreganj ','Manikganj','Munshiganj', 'Narayanganj', 'Narsingdi', 'Tangail','Faridpur', 'Gopalganj','Madaripur', 'Rajbari', 'Shariatpur'],

'khulna':['Bagerhat','Chuadanga', 'Jessore', 'Jhenaidah', 'Khulna', 'Kushtia','Magura', 'Meherpur', 'Narail', 'Satkhira'],

'mymensingh':['Jamalpur', 'Mymensingh', 'Netrokona', 'Sherpur'],

'rajshahi':['Bogura', 'Chapainawabganj','Joypurhat','Naogaon','Natore','Pabna', 'Rajshahi', 'Sirajgonj'],

'rangpur':['Thakurgaon','Rangpur', 'Panchagarh','Nilphamari', 'Lalmonirhat', 'Kurigram','Gaibandha', 'Dinajpur'],

'sylhet':['Habiganj', 'Moulvibazar','Sunamganj', 'Sylhet']
}

print ('Welcome to Bangladesh!')
print ('We have 8 Division:')
print(district.keys())

user_input=input("please enter division:").lower()
print(district.get(user_input,'not found'))
