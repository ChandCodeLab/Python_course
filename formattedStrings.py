#If you want to generate the text dynamically with your variable then formatted strings is come into the role 
first_name ='Manoj'
last_name ='Chand'
message = first_name + ' [' + last_name +'] is a coder.'  #complex form
print(message)

msg = f'{first_name} [{last_name}] is a coder.'
print(msg)