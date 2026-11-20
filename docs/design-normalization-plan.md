# Hanim Korean 자료 디자인 정규화 계획

> 상태: 제안서 · 기존 자료 수정 전
>
> 범위: `korean-lessons` 저장소의 현재 HTML 자료 58개를 표본·구조 기준으로 분류하고, 기능과 교육 내용을 보존하면서 Hanim Korean 톤으로 점진적으로 통일하기 위한 계획
>
> 비범위: 이 문서는 기존 HTML을 수정하거나 중복본을 삭제하지 않는다. 카테고리·태그·canonical 결정이 먼저다.

## 1. 결론

58개 HTML을 한 번에 같은 CSS로 덮어쓰면 안 된다. 현재 자료에는 다음 네 종류가 섞여 있다.

1. CSS 변수와 단순 문서 구조가 이미 있어 **토큰 교체만으로 안전하게 바뀌는 자료**
2. 퀴즈·카드·탭 등의 기능은 유지하되 **컴포넌트 외형을 다시 잡아야 하는 자료**
3. 화면 전환, 고정 뷰포트, 대용량 인라인 이미지가 결합되어 **새 템플릿으로 옮겨야 하는 자료**
4. 중복 또는 개인화 버전이라 **canonical을 정하기 전에는 디자인 작업을 보류할 자료**

따라서 순서는 아래처럼 고정한다.

> 카테고리화 → 태그·레벨 부여 → 중복·버전군 canonical 결정 → 홈페이지에 manifest로 노출 → 저위험 자료부터 디자인 정규화 → 복잡한 자료 재설계

기존 상호작용과 학습 내용은 디자인보다 우선한다. 첫 디자인 패스에서는 문구, 정답, 문제 순서, DOM `id`, `data-*`, 이벤트 대상 선택자를 바꾸지 않는다.

---

## 2. 표본 조사에서 확인한 구조

### 2.1 현재 공통점

- 대부분의 자료가 CSS와 JavaScript를 한 파일에 포함한 독립형 HTML이다.
- 모든 HTML에 자체 `<style>`이 있으며, 외부 프레임워크 의존은 거의 없다.
- 다수 자료가 모바일 대응 또는 인쇄 CSS를 일부 갖고 있다.
- `:root` CSS 변수를 가진 자료가 많아, 색상 토큰 교체가 가능한 가족이 분명히 존재한다.
- 기능형 자료는 버튼, reveal, 점수, shuffle, reset, 탭 전환 등이 파일별 JavaScript와 강하게 결합되어 있다.
- 일부 자료는 이미지가 base64로 HTML 안에 포함되어 수백 KB에서 수 MB까지 커진다.
- `four_gates.html`, `kids_korean_lesson_generator.html`은 완전한 독립 페이지가 아니라 호스트 앱의 `--color-*`, `--font-sans` 변수를 기대하는 조각형 자료다.

### 2.2 디자인이 갈라진 대표 가족

| 가족 | 대표 파일 | 현재 특징 | 위험 |
| --- | --- | --- | --- |
| Teal/Warm 학습 가이드 | `kr_basic_vowels_es.html`, `linking_sound_easy.html` | 동일 계열 변수, 종이 배경, offset shadow | 낮음 |
| 다색 장문 가이드 | `kr_marker_guide.html`, `past_tense.html` | 많은 의미 색, 긴 문서, 일부 inline style | 중간 |
| 회색 UI형 문법/발음 | `double_final_consonants.html`, `verb_conjugation.html` | 단정한 카드 UI, 상호작용 포함 | 중간 |
| 플래시카드 | `numbers/Korean-Numbers-Flashcards2.html`, `Sejong_korean2_02.html` | 카드 전환·점수·키보드 조작 | 중간 |
| 게임 | `Abby_bingo.html`, `pronunciation_detective.html` | 상태·점수·reset이 JS와 결합 | 중간 |
| 어린이 슬라이드 | `Julia_6_A_v3.html`, `Julia_html/julia_lesson5_slides.html` | 고정 화면, 강한 원색, 이미지 내장 | 높음 |
| 대형 어린이 활동 앱 | `Julia_html/skz_vowel_lesson_codepen_bundle.html`, `Julia_html/index.html` | 버튼·상태가 많고 구조가 복잡 | 높음 |
| 조각형 도구 | `four_gates.html`, `kids_korean_lesson_generator.html` | 호스트 디자인 토큰에 의존 | 중간 |
| Hanim 기준 시안 | `Bonnie_skiz_name.html` | 현 팔레트와 절제된 카드 스타일 반영 | 참조 |

---

## 3. 적용 등급

### A. Wrapper + token-only — 낮은 위험

**방법:** DOM과 기능은 그대로 두고, Hanim 토큰 alias와 바깥 shell만 추가한다. 기존 의미색은 필요한 경우 유지하되 채도를 낮춘다.

대상 후보:

- `kr_basic_vowels_es.html`
- `kr_basic_consonants_es.html` — canonical 선정 후
- `linking_sound_easy.html`
- `kr_double_n.html`
- `korean_word_order_sov.html`
- `korean_honorifics_guide.html`
- `seoul-real-korean-guide.html`
- `kr_trendings.html`
- `kr_vote_system.html`
- `four_gates.html` — 독립 페이지가 아닌 host-token adapter 방식
- `Bonnie_skiz_name.html` — 변경 대상보다 디자인 기준선으로 사용

가능한 변화:

- 배경, 본문색, 테두리, radius, shadow, 제목 크기, 최대 너비
- 과도한 점무늬·동그라미·offset shadow 제거
- 동일한 상단 lesson label과 하단 review/action 영역 추가
- print, focus, reduced-motion 보완

변경하면 안 되는 것:

- `details`의 순서와 answer 내용
- 문장 색상으로 전달되는 문법 역할 구분
- 파일 내부의 교육 문구

### B. Component refactor — 중간 위험

**방법:** JavaScript와 상태 데이터는 보존하고, 카드·탭·버튼·피드백 컴포넌트의 마크업 또는 CSS를 Hanim 컴포넌트에 맞춘다. JS가 참조하는 `id`, `data-*`, class selector를 먼저 목록화한다.

대상 후보:

- `numbers/Korean-Number-System.html`
- `numbers/Korean-Numbers-Flashcards.html`
- `numbers/Korean-Numbers-Flashcards2.html` — canonical 선정 후
- `Sejong_korean2_02.html`
- `Sejong02-03.html` / `Anna_6.html` — 템플릿 가족으로 취급
- `verb_conjugation.html`
- `heyo_verb_conjugation.html`
- `double_final_consonants.html` — canonical 선정 후
- `gyeopbatchim_bingo.html`
- `pronunciation_detective.html`
- `korean_colors_flashcards_quiz.html`
- `kr_igeujeo_triangle.html`
- `kr_marker_guide.html`
- `placement_probe_app.html` — 학생 홈페이지가 아닌 `/studio`용
- `world_map_korean.html`
- `Abby_bingo.html`
- `sejong4a_le1.html`
- `julia_game2_whats_missing.html`
- `julia_game3_vowel_song_hunt_1.html`
- `julia_krfood/julia_game1_picture_reveal.html`
- `past_tense.html`, `past_tense_complet.html`, `Chloe_과거형_가이드.html` — canonical/개인화 관계 결정 후
- `kr_16_pronunciation_guide.html` — exact duplicate 정리 후
- `kr_ㄹguide.html`, `ㄹpronunciaion.html` — 버전 관계 결정 후
- `pronunciation_tips/index.html`
- `maddie_index.html`, `maddie_맞춤한국어_6과.html`
- `maelys_index.html`, `maelys_정규수업4_맞춤한국어1_11과.html`

주요 리팩터링 포인트:

- 장문 가이드는 `lesson-hero`, `concept-card`, `example-list`, `practice`, `review` 구조로 통일
- 퀴즈는 `question`, `choices`, `feedback`, `reset` 상태를 공통 컴포넌트로 표현
- 플래시카드는 `front/back`, `progress`, `shuffle`, `keyboard help`를 같은 위치에 배치
- 교사용 도구는 학생용 자료와 다른 `data-hk-template="studio-tool"`을 사용
- 긴 개인화 노트는 삭제하지 않고 `catalog: false` 또는 `audience: private-link`로 두며, 필요할 때 같은 장문 템플릿만 적용

### C. Full redesign — 높은 위험

**방법:** 기존 파일 위에 CSS를 덮지 않는다. 먼저 문제·문장·정답·이미지·상태 데이터를 추출하고, 새 템플릿으로 렌더링한 뒤 구버전과 기능을 대조한다. 원본은 `legacy` 보존본으로 남긴다.

대상 후보:

- `Julia_6.html`
- `Julia_6_A_v3.html`
- `Julia_6_B_v3.html`
- `Julia_html/julia_game_quiz_final (2).html`
- `Julia_html/julia_lesson5_slides.html`
- `Julia_html/pororo_flashcards_v5.html`
- `julia_lesson7_ohmykimchi.html`
- `Julia_bibimbap.html`
- `Julia_html/index.html`
- `Julia_html/skz_vowel_lesson_codepen_bundle.html`

이유:

- 화면 크기와 레이아웃이 고정된 슬라이드가 많다.
- 강한 원색, 대형 타이포, 그림과 내비게이션이 한 구조로 결합되어 있다.
- base64 이미지가 파일을 지나치게 크게 만들거나, 이미지와 콘텐츠를 분리하기 어렵다.
- 일부 앱은 버튼과 상태가 수십 개여서 범용 `.card`, `.button` override가 기능 회귀를 일으킬 가능성이 크다.

재설계 시에도 유지할 것:

- 문제와 정답
- 활동의 진행 순서와 교육 의도
- reveal, shuffle, score, reset, next/back, keyboard 조작
- 어린 학생을 위한 짧은 피드백과 성공 경험

### D. Hold — canonical 결정 전 디자인 금지

| 버전군 | 현재 확인 | 제안 |
| --- | --- | --- |
| 16가지 발음 가이드 | `kr_16_pronunciation_guide.html`과 한글 파일명이 exact duplicate | 영문 파일명 하나를 canonical로 하고 다른 경로는 redirect/alias 후보 |
| 숫자 Flashcards 2 | 루트와 `numbers/` 아래 파일이 exact duplicate | `numbers/` 경로를 canonical 후보로 지정 |
| 겹받침 | `double_final_consonants.html`과 `kr_double_final_consonants.html`이 사실상 같은 버전 | 내용·byte 차이 확인 후 하나만 디자인 |
| 기본 자음 ES | `kr_basic_consonants_es.html`과 `(1)` 버전 | diff 검토 후 최신 한 개 선정 |
| ㄹ 가이드 | `kr_ㄹguide.html`, `ㄹpronunciaion.html` | 단순 중복이 아니므로 내용 차이·대상 수준 확인 후 canonical/variant 결정 |
| 과거형 | generic, complete, Chloé 개인화본 | complete를 canonical로 자동 가정하지 말고 범위·정확성 검토 후 관계 지정 |
| 외모 플래시카드 | `Anna_6.html`, `Sejong02-03.html` | 공통 템플릿 + 데이터 variant로 전환 후보 |
| Maddie/Maelys | index와 긴 이름 파일 | 같은 회차 중복인지 확인 후 private variant 또는 legacy 지정 |

중복 파일은 즉시 삭제하지 않는다. manifest에서 `canonical_id`, `variant_of`, `superseded_by`를 먼저 기록하고, 홈페이지는 canonical만 기본 노출한다.

---

## 4. 공통 CSS 구조

### 4.1 파일 구조

```text
assets/theme/
├─ hanim-tokens.css
├─ hanim-base.css
├─ hanim-components.css
├─ hanim-print.css
└─ templates/
   ├─ guide.css
   ├─ flashcards.css
   ├─ quiz-game.css
   ├─ lesson-deck.css
   └─ studio-tool.css
```

각 HTML에는 템플릿을 표시한다.

```html
<body data-hk-theme="hanim" data-hk-template="guide">
```

범용 `.card`, `.button`을 페이지 전체에 무조건 덮어쓰지 않는다. 모든 공통 selector는 아래처럼 scope한다.

```css
[data-hk-theme="hanim"][data-hk-template="guide"] .concept-card { ... }
```

기존 파일 위치가 루트와 하위 폴더로 나뉘므로, 링크 경로는 파일마다 계산한다.

- 루트 HTML: `assets/theme/hanim-tokens.css`
- 하위 폴더 HTML: `../assets/theme/hanim-tokens.css`

GitHub Pages 절대 경로만 사용하면 로컬 `file://` 미리보기가 깨지므로 피한다.

### 4.2 색상 토큰

```css
:root {
  --hk-forest-deep: #0F2A1D;
  --hk-forest: #375534;
  --hk-olive: #41644A;
  --hk-muted-teal: #84A59D;
  --hk-sage: #AEC3B0;
  --hk-paper: #EBE1D1;
  --hk-eggshell: #F4F1DE;
  --hk-sheet: #FBF8ED;
  --hk-ink: #203426;
  --hk-muted: #5C6E60;
  --hk-line: #C5D0BD;
  --hk-peach: #D99A79;
  --hk-warning-bg: #F7F0DF;
  --hk-danger-bg: #F2DFD1;
  --hk-danger-text: #6D3D2D;
}
```

운영 규칙:

- 큰 강한 색 면은 한 화면에 Forest Deep 하나만 사용
- Peach는 작은 강조선·주의점에만 사용
- 기본 배경은 Paper, 카드와 입력창은 Sheet
- 정답/성공은 Forest/Sage, 오류는 Danger 계열
- 문법 역할색이 꼭 필요한 자료는 의미를 지키되 Hanim 채도에 맞춘 보조 팔레트로 제한
- 색만으로 정답과 오류를 구분하지 않고 아이콘 또는 텍스트를 함께 제공

### 4.3 타이포·공간·표면

```css
:root {
  --hk-font-sans: Pretendard, SUIT, "Apple SD Gothic Neo", "Noto Sans KR", system-ui, sans-serif;
  --hk-title: clamp(2rem, 4vw, 2.375rem); /* 최대 약 38px */
  --hk-section: clamp(1.35rem, 2.5vw, 1.75rem);
  --hk-body: clamp(1rem, 1.7vw, 1.125rem);
  --hk-radius-sm: 10px;
  --hk-radius-md: 16px;
  --hk-radius-lg: 24px;
  --hk-shadow-soft: 0 12px 28px rgba(15, 42, 29, .08);
  --hk-content-max: 940px;
}
```

- 큰 제목은 38px을 넘기지 않는다.
- 본문은 18px 안팎, 줄간격 1.65 이상을 기본으로 한다.
- 한 화면에는 주요 과제 하나, 카드 2~4개만 둔다.
- 장식용 큰 원, 점무늬 배경, 굵은 검정 테두리, 딱딱한 offset shadow를 제거한다.
- 그림자는 hover/selected/hero처럼 계층을 구분할 때만 아주 약하게 쓴다.
- 기본 콘텐츠 너비는 900~940px, 읽기 자료는 760~820px까지 좁힐 수 있다.

### 4.4 공통 컴포넌트

- `hk-shell`: 페이지 최대 너비와 바깥 여백
- `hk-lesson-label`: 교재·과·수준·예상 시간
- `hk-hero`: 작은 제목, can-do, 짧은 설명
- `hk-toolbar`: 핵심/전체, 영어 숨기기, reset
- `hk-card`: 기본 카드
- `hk-concept-card`: 규칙과 핵심 예문
- `hk-example-list`: 예문 묶음
- `hk-choice`: 선택지
- `hk-feedback`: 정답·재시도 피드백
- `hk-personalize`: 자기 문장
- `hk-roleplay`: 역할극
- `hk-review`: 마지막 회상 문제
- `hk-progress`: 플래시카드·슬라이드 진행

---

## 5. 기능 보존 규칙

### 5.1 디자인 변경 전 baseline

각 canonical 파일에 대해 아래를 저장한다.

- desktop 1440px screenshot
- mobile 390px screenshot
- 파일 SHA-256
- 버튼/키보드/정답/점수/리셋 목록
- console error 유무
- 로컬 `file://`과 GitHub Pages 양쪽 실행 여부

### 5.2 첫 패스 금지 사항

- 문제·정답·설명 문구 수정
- 문제 순서 변경
- `id`, `data-*`, inline `onclick` 제거
- JS가 찾는 class 이름 변경
- 이미지 경로 이동
- base64 이미지를 별도 파일로 분리

콘텐츠 교정과 디자인 정규화는 같은 커밋에서 하지 않는다. 그래야 회귀 원인을 찾을 수 있다.

### 5.3 상호작용 smoke test

모든 기능형 자료에서 다음을 확인한다.

- 첫 화면과 마지막 화면 이동
- 이전/다음
- 정답/오답 피드백
- reset 후 초기 상태
- shuffle 후 항목 수 보존
- 점수와 progress 정확성
- 영어 숨기기/보기
- 키보드 조작과 focus-visible
- 모바일에서 버튼 최소 44px
- `prefers-reduced-motion`에서 불필요한 모션 중지
- 인쇄 시 정답과 불필요한 조작 버튼 처리

---

## 6. 파일럿 순서

한 가족에서 하나씩만 먼저 고친다.

| 순서 | 파일 | 검증 목적 | 통과 조건 |
| --- | --- | --- | --- |
| 1 | `linking_sound_easy.html` | token-only 가이드 | 내용·details 그대로, Hanim 톤, mobile/print 정상 |
| 2 | `korean_word_order_sov.html` | 의미 색이 있는 정적 가이드 | S/O/V 구분 유지, 색 대비 통과 |
| 3 | `numbers/Korean-Numbers-Flashcards2.html` | 플래시카드 컴포넌트 | 앞뒤·shuffle·progress·키보드 동일 |
| 4 | `pronunciation_detective.html` | 작은 퀴즈/게임 | 정답·점수·reset 동일 |
| 5 | `kr_marker_guide.html` | 긴 다색 가이드 | 정보 밀도 감소, 모든 문법 역할 보존 |
| 6 | `Abby_bingo.html` | 게임 보드 | 선택·빙고·reset 동일, mobile 정상 |
| 7 | `Julia_6_A_v3.html` | full redesign 슬라이드 | 모든 슬라이드·문항·내비게이션 대조 통과 |

실용한국어 5·6과 새 파일럿에서 확정되는 `guide`, `lesson-deck`, `roleplay`, `review` 컴포넌트도 이 공통 체계에 합류시킨다. 단, 기존 58개에 일괄 적용하기 전 위 일곱 파일로 회귀 위험을 확인한다.

---

## 7. 실행 단계와 완료 기준

### 단계 0 · manifest와 canonical 확정

- 모든 자료에 category, level, tags, format, audience, status, canonical 관계 부여
- 학생 개인화 자료는 유지 가능하되, 현재 홈페이지에 쓸 이유가 없으면 `catalog: false`
- 중복은 삭제하지 않고 기본 노출만 canonical로 제한

**완료:** 홈페이지가 디렉터리를 자동 스캔하지 않고 manifest만 읽을 수 있다.

### 단계 1 · 홈페이지 먼저

- 한글·발음 / 문법·문장 / 어휘 / 회화·문화 / 교재별 코스
- 초급 / 중급 / 고급
- 형식·기능 태그 검색
- legacy 자료도 디자인 변경 없이 카드에서 열 수 있게 함

**완료:** 58개 HTML을 손대지 않고도 정돈된 입구가 생긴다.

### 단계 2 · A군 일괄 적용

- 토큰·shell·타이포·표면만 정규화
- 각 파일 전후 screenshot과 smoke test

**완료:** 기능/내용 diff 없이 Hanim 톤으로 보인다.

### 단계 3 · B군 가족별 리팩터링

- flashcards → quiz → guide → game → studio tool 순
- 공통 컴포넌트가 세 파일 이상에서 실제 재사용될 때만 확정

**완료:** 같은 기능은 같은 위치와 상태 언어를 사용한다.

### 단계 4 · C군 재설계

- 콘텐츠/상태 데이터를 HTML에서 분리
- 새 템플릿 렌더링
- 구버전과 항목 수·정답·기능 대조

**완료:** legacy 원본 없이도 새 파일이 같은 수업을 온전히 수행한다.

### 단계 5 · 전체 품질 점검

- desktop/mobile/print
- keyboard/focus/reduced-motion
- broken link/image
- console error
- 학습 내용 변경 여부

**완료:** 디자인 차이는 의도된 것만 남고, 기능 회귀는 0건이다.

---

## 8. 결정 원칙

1. **Less is more.** 모든 자료에 장식 요소를 추가하는 것이 통일이 아니다.
2. **일관성은 동일한 팔레트보다 동일한 위계에서 온다.** 제목, can-do, 활동, 피드백, 복습 위치를 먼저 맞춘다.
3. **의미색은 브랜드색보다 우선할 수 있다.** 단, 개수를 줄이고 채도를 맞춘다.
4. **개인화 자료는 존재해도 된다.** 공개 홈페이지의 기본 자료로 쓸 필요가 없으면 catalog에서 제외한다.
5. **구버전 링크를 바로 끊지 않는다.** canonical을 정한 뒤 redirect 또는 alias 기간을 둔다.
6. **디자인과 교육 내용 수정은 분리한다.** 기능 보존 검증이 가능해야 한다.
7. **한꺼번에 58개를 고치지 않는다.** 가족별 대표 하나가 통과한 뒤 같은 가족에 확장한다.

이 계획을 따르면, 자료의 개성이 완전히 사라지지 않으면서도 사용자는 모두 같은 Hanim Korean Studio 안에서 만들어진 자료라고 느낄 수 있다.
