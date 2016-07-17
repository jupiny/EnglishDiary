import os


MAILGUN_API_BASE_URL = os.environ.get("MAILGUN_API_BASE_URL")
MAILGUN_API_MESSAGE_URL = MAILGUN_API_BASE_URL+"messages"
MAILGUN_API_KEY = os.environ.get("MAILGUN_API_KEY")

ADMIN_SENDER_EMAIL = "noreply@eng_diary_in_hard_way.com"

SIGNUP_EMAIL_SUBJECT = "[깐깐하게 쓰는 영어일기] 회원가입을 축하드립니다."

SIGNUP_EMAIL_TEXT = "{username} 회원님, 저희 서비스에 가입해주셔서 정말 감사합니다.\n오늘 하루 있었던 일을 영어일기로 남겨보세요!"

WRITE_DIARY_EMAIL_SUBJECT = "[깐깐하게 쓰는 영어일기] {username}님, 아직 일기를 쓰지 않으셨어요!"
WRITE_DIARY_EMAIL_TEXT = "{username}님, 오늘 재미있는 일이 없으셨나요?\n오늘 하루가 얼마남지 않았습니다. 빨리 서둘러 주세요!"
