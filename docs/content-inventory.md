# `korean-lessons` 콘텐츠 인벤토리 초안

기준일: 2026-08-20
범위: Git이 추적하는 111개 파일. 기존 자료는 수정·이동·삭제하지 않았다.

## 한눈에 보기

| 구분 | 수 |
| --- | ---: |
| HTML 자료 | 58 |
| 연결 자산(PNG/JPG/PDF) | 52 |
| 저장소 설명 파일(README) | 1 |
| 합계 | 111 |

58개 HTML은 모두 [`data/content-manifest.draft.json`](../data/content-manifest.draft.json)에 정확히 한 번씩 들어 있다. 초안 검증 결과는 오류 0건이다.

## 1차 카테고리

| 카테고리 | 수 | 홈페이지 기본 노출 |
| --- | ---: | --- |
| 한글·발음 (`hangul-pronunciation`) | 14 | 검수 뒤 노출 |
| 문법·문장 (`grammar-sentences`) | 8 | 검수 뒤 노출 |
| 어휘 (`vocabulary`) | 6 | 검수 뒤 노출 |
| 회화·문화 (`conversation-culture`) | 4 | 검수 뒤 노출 |
| 교재별 코스 (`textbook-courses`) | 3 | 인용·권리 검수 뒤 노출 |
| 개인화 (`personalized`) | 21 | 기본 목록에서 제외 |
| 스튜디오 도구 (`studio-tools`) | 2 | `/studio` 내부 전용 |

개인화 자료는 사용자의 결정에 따라 저장소에 그대로 유지한다. 다만 `visibility=student`는 카탈로그 동작을 위한 표시일 뿐 보안 장치가 아니다. 현재 저장소가 공개라면 URL을 아는 사람은 접근할 수 있다.

## 난이도

| 난이도 | 수 | 설명 |
| --- | ---: | --- |
| 초급 | 52 | A0 23개, A1 15개, A2 14개 |
| 중급 | 4 | B1 4개 |
| 고급 | 0 | 자료가 없으므로 억지로 채우지 않음 |
| 해당 없음 | 2 | 교사용 도구 |

현재 자료실은 초급 중심이다. 고급 필터는 홈페이지에 둘 수 있지만, 자료가 생길 때까지 빈 상태 안내를 보여 주는 편이 정확하다.

## 편집 상태

| 상태 | 수 | 의미 |
| --- | ---: | --- |
| `review` | 48 | 내용·디자인·권리 확인을 기다리는 대표본 후보 |
| `archived` | 10 | 완전 중복 또는 이전 버전. 아직 삭제하지 않음 |

대표본 후보는 48개, 비대표본은 10개다. 이 초안에서는 어떤 자료도 바로 `published`로 승격하지 않았다. 다음 단계에서 하님이 홈페이지 공개 후보를 확인한 뒤 상태를 바꾸면 된다.

## 중복·버전군

### SHA-256이 완전히 같은 파일

1. `Korean-Numbers-Flashcards2.html`
   → 대표본: `numbers/Korean-Numbers-Flashcards2.html`
2. `한국어_발음규칙_16가지_가이드.html`
   → 대표본: `kr_16_pronunciation_guide.html`

### 내용상 버전군

| 버전군 | 대표본 후보 | 이전본·주의점 |
| --- | --- | --- |
| 겹받침 가이드 | `double_final_consonants.html` | `kr_double_final_consonants.html`에는 `값 + 어요` 오타가 있음 |
| 스페인어 화자용 자음 | `kr_basic_consonants_es (1).html` | 새 예시가 추가됨. 최종적으로 괄호 없는 파일명 권장 |
| ㄹ 발음 가이드 | `ㄹpronunciaion.html` | `kr_ㄹguide.html`보다 도식과 설명이 확장됨. 파일명 철자 수정 필요 |
| 과거형 | `past_tense.html` 간결 K-pop판 + `past_tense_complet.html` 종합판 | 서로 범위가 달라 둘 다 대표본으로 유지. Chloé 파일은 간결판의 개인화 파생본 |
| 해요체 활용 | `heyo_verb_conjugation.html` | `verb_conjugation.html`은 축소 이전본 |
| Maddie 6과 | 긴 파일명의 완성본 | `maddie_index.html`은 이전 축약본 |
| Maelys 11과 | 긴 파일명의 완성본 | `maelys_index.html`은 이전 축약본 |

삭제는 아직 하지 않는다. 대표본을 승인하고, 기존 링크 사용 여부를 확인하고, 필요하면 redirect/alias를 만든 뒤 별도 단계에서 처리한다.

## 자산 연결

52개 자산은 별도 학습 자료로 카탈로그에 넣지 않고 HTML에 연결한다.

| 자산 묶음 | 수 | 연결 자료 |
| --- | ---: | --- |
| `Julia_html/images/*.png` | 8 | `Julia_html/index.html` |
| `julia_krfood/*.(png|jpg)` | 5 | `julia_krfood/julia_game1_picture_reveal.html` |
| `kr_vote_proof_vote.jpg`, `kr_vote_stamp.png` | 2 | `kr_vote_system.html` |
| `pronunciation_tips/*.png` | 14 | `pronunciation_tips/index.html` |
| `numbers/` PNG와 PDF | 23 | 숫자 자료군. 현재 HTML의 직접 참조가 확인되지 않아 orphan 여부 재검토 |

일부 대형 HTML은 이미지를 base64로 품고 있어 파일 크기가 매우 크다. 디자인 통일 단계에서 별도 자산으로 분리할 후보지만, 인벤토리 단계에서는 건드리지 않았다.

## 태그 원칙

- 카테고리는 자료의 **주된 학습 목적** 하나만 선택한다.
- `game`, `quiz`, `flashcards`, `slides`, `guide`, `role-play`, `review`는 카테고리가 아니라 형식이다.
- 태그는 주제·문법·대상·교재명을 3~6개 정도로 제한한다.
- 학생 이름은 검색 태그로 사용하지 않는다. 개인화 여부는 `primary_category`와 `audience`로 구분한다.
- 초급/중급/고급과 CEFR 하위 단계는 별도 필드로 관리한다.

## 홈페이지로 넘기는 첫 묶음

권리가 `owned`이고 대표본인 공개 후보 18개를 먼저 검수하면 작은 홈페이지를 빠르게 열 수 있다.

- 한글·발음: 겹받침, 연음, 16가지 발음 규칙, 스페인어권 자모, ㄴ 연결음, 발음 탐정, 쌍자음·격음
- 문법·문장: 어순, 조사, 이·그·저, 해요체, 높임말
- 어휘: 색깔, 숫자 플래시카드
- 회화·문화: 서울 사대문, 서울 여행 실전 회화

교재별 코스와 이미지가 많은 K-pop·어린이 자료는 두 번째 검수 묶음으로 두는 편이 안전하다.

## 인벤토리에서 제외한 현재 untracked HTML

아래 네 파일은 Git이 추적하지 않는 정규화된 이름의 복제본으로 보여 111개 기준 인벤토리에서 제외했다.

- `Chloe_과거형_가이드.html`
- `maddie_맞춤한국어_6과.html`
- `maelys_정규수업4_맞춤한국어1_11과.html`
- `한국어_발음규칙_16가지_가이드.html`

추적본과 내용·해시를 비교한 뒤 어느 쪽을 남길지 결정해야 한다.

## 다음 작업

1. manifest에서 하님이 공개할 대표본 1차 묶음을 승인한다.
2. 태그 표기를 한 번 더 합친다. 예: `은는`과 `은/는` 중 하나만 사용.
3. 버전군의 대표본과 새 파일명을 확정한다.
4. 기존 URL 보존 방식을 정한 뒤에만 중복 파일을 정리한다.
5. `canonical=true + status=published + visibility=public` 항목만 홈페이지가 읽게 한다.
