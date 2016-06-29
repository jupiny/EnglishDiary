migrate:
	- python english_diary/manage.py makemigrations english_diary users diaries
	- python english_diary/manage.py migrate 
test:
	- pep8 . -v
	- python english_diary/manage.py test english_diary users diaries
