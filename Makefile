migrate:
	- python english_diary/manage.py makemigrations users diaries profiles
	- python english_diary/manage.py migrate 
test:
	- pep8 . -v
	- python english_diary/manage.py test users diaries profiles
