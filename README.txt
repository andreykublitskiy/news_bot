1. Login to your google account
2. In browser, navigate to https://myaccount.google.com/apppasswords
3. Create app password
4. Update python script to use the email and app password
5. Run install_libraries.py to install app libraries
	May need to install pip3 first
6. Run command(s):
	python3 scheduled_with_date.py 'Tesla earnings' --to <email>@gmail.com --from_date 2024-05-21 --to_date 2024-05-22
		This one runs on schedule and uses date range
	python3 better.py 'Tesla' --to <email>@gmail.com
		This one runs immediately and sends everything

ssh -i "email_server_free.pem" <ec2_instance>.compute-1.amazonaws.com



ssh -i "email_server_free.pem" <ec2_instance>.compute-1.amazonaws.com "python3 better.py 'Tesla earnings' --to <email>@gmail.com"

ssh -i "email_server_free.pem" <ec2_instance>.compute-1.amazonaws.com "python3 run_with_dates.py 'Tesla earnings' --to <email>@gmail.com --from_date 2024-06-20 --to_date 2024-06-21"

ssh -i "email_server_free.pem" <ec2_instance>.compute-1.amazonaws.com "python3 scheduled_time.py 'Tesla earnings' --to <email>@gmail.com </dev/null >/dev/null 2>&1 &"

