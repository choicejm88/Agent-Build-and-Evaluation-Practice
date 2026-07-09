---
name: search_stock_news
description: 기업 또는 종목의 최신 뉴스를 검색하고 정리한다.
---

# Search Stock News

## 목적

기업과 관련된 최신 뉴스를 검색한다.

## Input

- 종목명
- 조회기간(기본 7일)

## Tool

뉴스 검색은 아래 우선순위를 따른다.

① Web Search

기본 뉴스 검색

② Naver OpenAPI (Optional)

API Key가 설정된 경우 사용

③ Naver News MCP (Optional)

MCP Server가 구성된 경우 사용

## Workflow

1.

종목명 확인

↓

2.

뉴스 검색

↓

3.

중복 제거

↓

4.

관련 없는 기사 제거

↓

5.

최신순 정렬

## Output

뉴스 목록

- 제목

- 날짜

- 출처

- URL

- 요약

## Rules

출처가 없는 뉴스는 제외한다.