import os


MAILGUN_API_BASE_URL = os.environ.get("MAILGUN_API_BASE_URL")
MAILGUN_API_MESSAGE_URL = MAILGUN_API_BASE_URL+"messages"
MAILGUN_API_KEY = os.environ.get("MAILGUN_API_KEY")

ADMIN_SENDER_EMAIL = "noreply@engdiary.dsds101.info"

EMAIL_VERIFICATION_SUBJECT = "[깐깐하게 쓰는 영어일기] {username}님, 회원가입을 환영합니다. 이메일 주소를 인증해주세요."

WRITE_DIARY_EMAIL_SUBJECT = "[깐깐하게 쓰는 영어일기] {username}님, 아직 일기를 쓰지 않으셨어요!"

TEST_EMAIL = "test@example.com"
