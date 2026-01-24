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

Totoal requests: 10


Status Code Summary

200 : 6

401 : 1

404 : 2

500 : 1

## Notes

 - 로그 한 줄에서 추출된 상태코드가 '200'이라서 당황했지만 int로 변형하여 처리
 - zip함수를 사용하여 추출된 키워드 리스트와 추출된 갯수를 하나의 딕셔너리로 묶음(dict(zip(~,~)))

## Status

- starting project
- completed number 2, 4 of Featurs