from instascrape import Profile

user_name = Profile.from_username('pycoders')
user_name.load()

recent = user_name.get_recent_posts()
profile_photos = [post for post in recent if not post.is_video]

for post in profile_photos:
	img = post.upload_date.strftime("%Y-%m-%d %Hh%Mm")
	post.download(f"{img}.png")