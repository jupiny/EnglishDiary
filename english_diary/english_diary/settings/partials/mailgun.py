import os


MAILGUN_API_BASE_URL = os.environ.get("MAILGUN_API_BASE_URL")
MAILGUN_API_MESSAGE_URL = MAILGUN_API_BASE_URL+"messages"
MAILGUN_API_KEY = os.environ.get("MAILGUN_API_KEY")
MAILGUN_SENDER_EMAIL = "noreply@eng_diary_in_hard_way.com"
MAILGUN_SUBJECT = "깐깐하게 쓰는 영어일기 회원가입을 축하드립니다."
MAILGUN_TEXT = " 회원님! 저희 서비스에 가입해주셔서 감사합니다.\n오늘 하루 있었던 일을 영어일기로 남겨보세요!"
