# korean-lessons 중복·버전 정리안

> 작성 목적: 공개 자료를 카테고리화하기 전에 **같은 파일, 이전 버전, 개인화 파생본**을 구분하고, 기존 URL을 깨뜨리지 않으면서 대표본(canonical)을 정하기 위한 읽기 전용 감사 기록입니다.
>
> 이 문서를 만들면서 기존 자료는 삭제·이동·수정하지 않았고, Git add/commit/push도 하지 않았습니다.

## 1. 판정 기준

- **완전 중복**: SHA-256이 같아 바이트 단위로 동일한 파일
- **근접 중복**: 본문과 기능이 사실상 같고 문구·예시·학생 이름만 조금 다른 파일
- **버전 묶음**: 같은 수업 목표를 구현한 이전판·확장판·분할판
- **파생본**: 공용본에서 학생 이름이나 관심사만 바꾼 개인화 자료
- **관련 자료**: 주제가 비슷해도 수업 범위나 활동이 달라 합치면 안 되는 파일

대표본은 현재 파일을 즉시 없앤다는 뜻이 아닙니다. 홈페이지와 향후 `content-manifest.json`이 우선 가리킬 자료를 뜻합니다.

## 2. 완전 중복: SHA-256 확인 결과

저장소 전체 파일을 SHA-256으로 비교했을 때 완전 중복은 두 묶음입니다.

| SHA-256 | 크기 | 파일 | 권장 대표본 | 처리 제안 |
| --- | ---: | --- | --- | --- |
| `a54d7881ce7ffab40c7b53d9da79fead132e3580811503ce42394b657db00a27` | 23,221 B | `Korean-Numbers-Flashcards2.html`<br>`numbers/Korean-Numbers-Flashcards2.html` | `numbers/Korean-Numbers-Flashcards2.html` | `numbers/Korean-Number-System.html`이 이미 이 경로를 링크합니다. 루트 파일은 당분간 URL 별칭으로 보존합니다. |
| `5e4f35fdfff4129ca7f861facf2bf5c778d073020963c680cf325861fd0d593c` | 44,036 B | `kr_16_pronunciation_guide.html`<br>`한국어_발음규칙_16가지_가이드.html` | `kr_16_pronunciation_guide.html` | ASCII 경로가 GitHub Pages·운영체제 간에 더 안정적입니다. 한글 파일명은 당분간 별칭으로 보존합니다. |

`Korean-Numbers-Flashcards2.html`이라는 문자열은 `numbers/Korean-Number-System.html` 982행의 절대 URL에도 등장하지만, 실제 링크 대상은 이미 권장 대표본인 `numbers/Korean-Numbers-Flashcards2.html`입니다.

## 3. 근접 중복·버전 묶음

### 3.1 기본 자음 스페인어판

| 항목 | 내용 |
| --- | --- |
| 파일 | `kr_basic_consonants_es.html` (17,060 B)<br>`kr_basic_consonants_es (1).html` (17,122 B) |
| 실제 차이 | 후자가 `파파야`를 빼고 `나초`, `부리토`를 넣었습니다. 나머지 구조는 동일합니다. |
| 권장 대표 경로 | `kr_basic_consonants_es.html` |
| 권장 내용 | `(1)`의 최신 예시가 정말 더 좋은지 검토한 뒤 깨끗한 파일명에 반영합니다. 자동으로 한쪽을 덮어쓰지 않습니다. |
| 이후 처리 | 내용 확정 → 대표 경로 갱신 → `(1)` 경로에 별칭/리디렉션 → 한 릴리스 이상 관찰 → 보관 여부 결정 |

### 3.2 겹받침 가이드

| 항목 | 내용 |
| --- | --- |
| 파일 | `double_final_consonants.html` (34,602 B)<br>`kr_double_final_consonants.html` (34,601 B) |
| 실제 차이 | 두 줄뿐입니다. `double_final_consonants.html`은 `밟다 [밥ː따]`의 장음 부호를 일관되게 쓰며, `없어요 (없 + 어요)`라고 적습니다. 다른 파일에는 `없어요 (값 + 어요)`라는 오기가 있습니다. |
| 권장 대표본 | `double_final_consonants.html` |
| 이후 처리 | `kr_double_final_consonants.html`은 기존 URL 별칭으로 유지하고 홈페이지에서는 노출하지 않습니다. |

### 3.3 과거형 자료

| 역할 | 파일 | 판단 |
| --- | --- | --- |
| 공용 간결판/K-pop판 | `past_tense.html` (36,040 B) | 이 범주의 대표본 |
| 학생 개인화 파생본 | `Chloe_과거형_가이드.html` (36,038 B) | 공용 간결판과 거의 같고 Chloé 이름, 회차, 일부 예시만 다릅니다. 홈페이지 기본 검색에서는 제외하되 보존합니다. |
| 공용 종합판 | `past_tense_complet.html` (45,398 B) | 불규칙·부정 과거형까지 포함한 별도 확장판입니다. 간결판을 무조건 대체시키지 않습니다. |

권장 구조는 하나로 억지 병합하는 것이 아니라 다음 두 상품으로 구분하는 것입니다.

- `past-tense-kpop` → 현재 `past_tense.html`
- `past-tense-complete` → 현재 `past_tense_complet.html`

`past_tense_complet.html`은 파일명에 철자 누락이 있으므로, 나중에 깨끗한 영구 경로를 만든 뒤 기존 경로를 별칭으로 남깁니다. 개인화본은 `derived_from: past-tense-kpop` 관계만 기록합니다.

### 3.4 해요체 동사 활용

| 항목 | 내용 |
| --- | --- |
| 파일 | `verb_conjugation.html` (14,930 B)<br>`heyo_verb_conjugation.html` (39,264 B) |
| 관계 | 후자가 같은 핵심 주제를 더 자세히 구현한 확장판입니다. 단순 바이트 중복은 아닙니다. |
| 권장 대표본 | `heyo_verb_conjugation.html` |
| 이후 처리 | 이전판에만 있는 설명·상호작용이 없는지 기능표로 한 번 확인한 뒤 `verb_conjugation.html`을 legacy 별칭/보관본으로 전환합니다. |

### 3.5 ㄹ 발음 가이드

| 항목 | 내용 |
| --- | --- |
| 파일 | `kr_ㄹguide.html` (199,304 B)<br>`ㄹpronunciaion.html` (96,915 B) |
| 관계 | 제목과 여섯 단원 구성이 같고, 후자가 “ㄹ은 독립적인 한국어 소리”와 혀의 동작을 더 정확하게 강조한 후속 개정판입니다. |
| 권장 내용 원본 | `ㄹpronunciaion.html` |
| 권장 최종 경로 | `rieul-pronunciation-guide.html` |
| 주의 | 현재 후속 파일명에는 `pronunciaion` 철자 오류가 있고 Unicode 파일명입니다. 새 경로를 만든 뒤 두 옛 경로 모두 별칭으로 남겨야 합니다. 이미지·연습·설명이 구판에만 남아 있지 않은지도 먼저 확인합니다. |

### 3.6 한국어 숫자 플래시카드

| 역할 | 파일 | 판단 |
| --- | --- | --- |
| 이전판 | `numbers/Korean-Numbers-Flashcards.html` (17,945 B) | legacy 후보 |
| 후속판 | `numbers/Korean-Numbers-Flashcards2.html` (23,221 B) | 모드 전환, 고유어 숫자 명명 정리, 서수 범주 등이 추가된 대표본 |
| 완전 중복 별칭 | `Korean-Numbers-Flashcards2.html` | 후속판과 SHA-256 동일 |

권장 대표본은 `numbers/Korean-Numbers-Flashcards2.html`입니다. 다만 `numbers/Korean-Numbers-Flashcards.html`에만 있는 카드나 동작이 없는지 브라우저 기능 비교 후 legacy 전환합니다.

`numbers/Korean-Number-System.html`과 `numbers/Korean-Number-System.pdf`는 삭제 대상 중복이 아니라 **같은 논리 자료의 웹판·PDF판**으로 등록합니다.

### 3.7 외모·색깔 플래시카드

| 항목 | 내용 |
| --- | --- |
| 파일 | `Anna_6.html` (11,323 B)<br>`Sejong02-03.html` (11,328 B) |
| 실제 차이 | 제목, 헤더, 코드 주석의 Anna 이름만 일반화되어 있습니다. 카드 데이터는 사실상 같습니다. |
| 권장 대표본 | `Sejong02-03.html` |
| 이후 처리 | `Anna_6.html`은 개인화 파생본으로 보존하고 홈페이지 기본 목록에서는 공용본만 노출합니다. |

### 3.8 Julia 6과

| 역할 | 파일 | 판단 |
| --- | --- | --- |
| 이전 단일판 | `Julia_6.html` (15,639 B) | 신체 부위 중심의 짧은 이전판 |
| 후속 A | `Julia_6_A_v3.html` (359,828 B) | 신체 부위 수업의 확장·이미지 포함판 |
| 후속 B | `Julia_6_B_v3.html` (323,478 B) | “이게 뭐예요?”를 다루는 후속 파트 |

권장 대표는 **A와 B의 한 쌍**입니다. B는 A의 중복이 아니라 다음 파트이므로 합치거나 하나를 지우면 안 됩니다. `Julia_6.html`은 A의 이전판으로 표시하고 홈페이지 기본 검색에서 제외하는 방향이 안전합니다.

### 3.9 Maddie 6과

| 항목 | 내용 |
| --- | --- |
| 파일 | `maddie_index.html` (21,390 B)<br>`maddie_맞춤한국어_6과.html` (34,429 B) |
| 관계 | `maddie_index.html`의 복습·5/6과 비교 내용이 긴 파일에 포함되며, 긴 파일에는 새 어휘·문법·대화·활동·플래시카드·숙제가 추가됩니다. |
| 권장 대표본 | `maddie_맞춤한국어_6과.html` |
| 이후 처리 | `maddie_index.html`이 외부에서 시작 페이지로 사용되지 않는지 확인한 뒤 legacy 별칭으로 전환합니다. |

### 3.10 Maelys 11과

| 항목 | 내용 |
| --- | --- |
| 파일 | `maelys_index.html` (23,021 B)<br>`maelys_정규수업4_맞춤한국어1_11과.html` (38,071 B) |
| 관계 | `maelys_index.html`의 복습 내용이 긴 수업 파일에 포함되며, 긴 파일에는 인사 어휘·문법·대화·활동·플래시카드·숙제가 추가됩니다. |
| 권장 대표본 | `maelys_정규수업4_맞춤한국어1_11과.html` |
| 이후 처리 | `maelys_index.html`이 별도 복습 활동으로 실제 사용되는지 확인한 뒤 legacy 여부를 정합니다. |

## 4. 비슷하지만 합치지 않을 자료

- `Julia_html/index.html`과 `Julia_html/skz_vowel_lesson_codepen_bundle.html`은 모두 Stray Kids·모음 자료지만, 전자는 가족 이름·이중모음까지 포함하고 후자는 기본 모음 미션 중심입니다. 서로 다른 수업 변형으로 보존합니다.
- `Sejong_korean2_02.html`과 `Sejong02-03.html`은 파일명이 비슷할 뿐 각각 세종 2권 2과 `-어/-아 보다`, 3과 외모·색깔 자료입니다.
- `double_final_consonants.html`과 `gyeopbatchim_bingo.html`은 같은 주제의 설명 자료와 게임 자료입니다. 형식 태그로 연결하되 중복 처리하지 않습니다.
- `past_tense.html`과 `past_tense_complet.html`은 간결판과 종합판으로 둘 다 남길 가치가 있습니다. 홈페이지에서 설명을 달리해 선택하게 합니다.

## 5. 비파괴 정리 순서

다음 순서를 건너뛰고 바로 파일을 지우지 않습니다.

1. **현재 스냅샷 기록**
   - 전체 경로, SHA-256, 파일 크기, Git commit을 기록합니다.
   - 현재 공개 URL도 함께 기록합니다.
2. **대표본만 manifest에 등록**
   - 홈페이지는 대표본만 보여 줍니다.
   - 이전판과 개인화본은 `status: legacy` 또는 `visibility: unlisted`로 표시합니다.
3. **참조 검사**
   - HTML의 `href`, `src`, JavaScript 문자열, README, manifest, Notion·Drive에 저장한 링크를 검색합니다.
   - 저장소 검색만으로 외부 북마크와 학생에게 보낸 링크를 확인할 수 없으므로 최소 한 릴리스 동안 옛 URL을 유지합니다.
4. **대표본 기능 비교**
   - 데스크톱·모바일에서 열기, 버튼, 뒤집기, 정답 보기, 오디오, 이미지, 키보드 동작을 비교합니다.
   - 이전판에만 있는 기능이나 문항은 대표본에 흡수하거나 별도 변형으로 보존합니다.
5. **보관본 생성**
   - 옛 실제 콘텐츠를 `archive/legacy/...`에 그대로 보관합니다.
   - 원래 공개 경로는 즉시 삭제하지 않습니다.
6. **옛 경로를 별칭으로 전환**
   - GitHub Pages에는 서버 리디렉션이 없으므로 원래 파일 위치에 작은 HTML 리디렉션 문서를 둘 수 있습니다.
   - 리디렉션에는 `<link rel="canonical">`, meta refresh, JavaScript 이동, 클릭 가능한 대체 링크를 함께 둡니다.
7. **한 릴리스 이상 관찰**
   - 홈페이지, 수업 노트, 학생 북마크에서 옛 주소 오류가 없는지 봅니다.
8. **최종 삭제는 별도 승인 후**
   - archive 사본, Git 이력, 참조 0건, 대표본 기능 검증을 모두 확인한 뒤에만 삭제를 검토합니다.

## 6. 삭제·이동 전 확인 명령

아래는 모두 읽기 전용 확인 예시입니다. 실제 파일명은 작은따옴표로 감싸 공백·한글을 보호합니다.

### 6.1 작업 트리와 기준 commit 확인

```bash
git status --short
git rev-parse HEAD
git ls-files -z | tr '\0' '\n' | wc -l
```

작업 트리가 깨끗하지 않으면 다른 작업자의 변경과 정리 작업을 섞지 않습니다.

### 6.2 SHA-256 재확인

```bash
shasum -a 256 \
  'Korean-Numbers-Flashcards2.html' \
  'numbers/Korean-Numbers-Flashcards2.html'

shasum -a 256 \
  'kr_16_pronunciation_guide.html' \
  '한국어_발음규칙_16가지_가이드.html'
```

두 줄의 해시가 같아야만 완전 중복으로 취급합니다.

저장소 전체 완전 중복 후보를 다시 찾으려면:

```bash
find . -type f -not -path './.git/*' -print0 \
  | xargs -0 shasum -a 256 \
  | sort
```

### 6.3 저장소 내부 참조 검색

```bash
git grep -n -F 'Korean-Numbers-Flashcards2.html'
rg -n --hidden --glob '!.git/**' --fixed-strings \
  'Korean-Numbers-Flashcards2.html' .
```

- `git grep`은 현재 추적 파일을 봅니다.
- `rg`는 아직 commit하지 않은 manifest·문서까지 확인합니다.
- basename, 상대 경로, 전체 GitHub Pages URL을 각각 검색합니다.
- URL 인코딩된 링크도 있을 수 있으므로 브라우저 히스토리·Notion 링크는 별도로 확인합니다.

### 6.4 두 버전 차이 확인

```bash
diff -u 'double_final_consonants.html' \
  'kr_double_final_consonants.html'

diff -u 'Anna_6.html' 'Sejong02-03.html'
```

출력이 길면 우선 `diff -q`로 동일 여부를 확인하고, 다를 때만 상세 diff를 봅니다.

### 6.5 HTML이 참조하는 로컬 자산 확인

파일을 옮기기 전에 `src`, `href`, CSS `url(...)` 상대 경로를 확인합니다.

```bash
rg -n 'src=|href=|url\(' '대상파일.html'
```

브라우저에서 로컬 서버를 열고 개발자 도구의 404도 확인합니다.

```bash
python3 -m http.server 8000
```

### 6.6 공개 URL 보존 확인

별칭을 배포한 뒤 이전 주소와 대표 주소가 모두 200 응답인지 확인합니다.

```bash
curl -I 'https://hanim-korean.github.io/korean-lessons/옛-경로.html'
curl -I 'https://hanim-korean.github.io/korean-lessons/대표-경로.html'
```

그다음 실제 브라우저에서 이전 주소가 대표 자료로 이동하고, 뒤로 가기·새로 고침도 정상인지 확인합니다.

## 7. macOS Unicode 정규화 주의

현재 `core.precomposeunicode=true`인 macOS 작업 트리에서 다음 네 파일이 **NFD로 추적되어 있지만 NFC 이름의 미추적 파일처럼 `git status`에 보이는 현상**이 관찰됐습니다.

- `Chloe_과거형_가이드.html`
- `maddie_맞춤한국어_6과.html`
- `maelys_정규수업4_맞춤한국어1_11과.html`
- `한국어_발음규칙_16가지_가이드.html`

이는 내용이 새로 생겼다는 뜻이 아니라, 한글 파일명의 NFC/NFD 표현 차이일 수 있습니다. 다음 행동을 하면 안 됩니다.

- Finder에서 보이는 NFC 파일을 새 파일이라고 생각하고 무심코 `git add .` 하기
- 한쪽을 중복이라고 생각해 Finder에서 삭제하기
- `mv`만으로 한글 파일명을 정리하고 바로 commit하기

먼저 코드포인트와 정규화 충돌을 확인합니다.

```bash
python3 - <<'PY'
from pathlib import Path
import subprocess, unicodedata

tracked = subprocess.check_output(['git', 'ls-files', '-z']).decode().split('\0')[:-1]
for name in tracked:
    nfc = unicodedata.normalize('NFC', name)
    if nfc != name:
        print('tracked NFD:', repr(name), '=> NFC:', repr(nfc))

seen = {}
for path in Path('.').rglob('*'):
    if not path.is_file() or '.git' in path.parts:
        continue
    nfc = unicodedata.normalize('NFC', str(path))
    seen.setdefault(nfc, []).append(str(path))
for nfc, paths in seen.items():
    if len(paths) > 1:
        print('normalization collision:', repr(nfc), paths)
PY
```

파일명 정규화는 중복 정리와 분리된 전용 commit에서, 백업과 경로 참조 검사를 마친 뒤 `git mv`를 사용해 처리해야 합니다. 이 문제가 해결되기 전에는 `git add .` 대신 추가할 경로를 정확히 지정하는 편이 안전합니다.

## 8. 권장 실행 묶음

실제 정리는 다음처럼 작은 단위로 나누는 것이 안전합니다.

1. 완전 중복 두 묶음에 대표본·별칭 metadata만 추가
2. `double_final_consonants.html`, `Sejong02-03.html` 대표 지정
3. 숫자 v1/v2 브라우저 기능 비교 후 v2 대표 지정
4. 기본 자음 ES 두 파일의 예시 문구를 사람이 선택
5. 과거형을 간결판·종합판·개인화 파생본으로 분류
6. ㄹ 가이드 구판/개정판의 이미지·설명 누락 비교
7. Julia·Maddie·Maelys 이전판을 legacy로 표시
8. 한 릴리스 뒤에도 필요하면 archive + 옛 경로 redirect
9. 실제 삭제는 그 이후 별도 승인

이 순서를 따르면 홈페이지에서는 중복이 즉시 사라지지만, 이미 공유한 링크와 원본 자료는 잃지 않습니다.
