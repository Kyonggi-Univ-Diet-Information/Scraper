# 1. 베이스 이미지 선택
FROM python:3.11-slim

# 2. 작업 디렉터리 생성 및 설정
WORKDIR /app

# 3. 필요한 파일 복사
COPY requirements.txt requirements.txt
COPY . .

# 4. 의존성 설치
RUN pip install --no-cache-dir -r requirements.txt

# 5. 스크래피 스파이더 실행 명령어
CMD ["python", "main.py"]
