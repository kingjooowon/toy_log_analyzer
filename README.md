# toy_log_analyzer

서버 로그 파일을 읽어서 요청 수, 상태 코드 분포, 가장 많이 호출된 경로를 분석하는 프로그램입니다.

## Features

1. 로그 파일을 한 줄(yield사용)씩 읽어서 정보(status code, method, path) 추출하기
2. 총 요청 수 세기
3. HTTP 메서드별(GET, POST) 요청 수 세기
4. 상태 코드별(200, 404, 401) 요청 수 세기
5. 가장 많이 호출된 URL Top 3

## Tech Stack

1. python3
2. Standard Library

## Project Structure

toy_log_analyzer/
  - log_analyzer.py
  - sample.log
  - README.md

## How to Run

python log_analyzer.py sample.log

## Example Output

## Notes

## Status

- starting project